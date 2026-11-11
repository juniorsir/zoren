#!/usr/bin/env python3
import os
import sys
import re
import time
import subprocess
import argparse
import tempfile

COLOR_RESET = "\x1b[0m"
COLOR_BOLD = "\x1b[1m"
COLOR_RED = "\x1b[1;31m"
COLOR_GREEN = "\x1b[1;32m"
COLOR_YELLOW = "\x1b[1;33m"
COLOR_CYAN = "\x1b[1;36m"
COLOR_GRAY = "\x1b[90m"

class ExampleMetadata:
    def __init__(self):
        self.expect_status = "SUCCESS"
        self.expect_code = None
        self.expected_output = []
        self.skip = False
        self.timeout = 5

def parse_code_metadata(code_text):
    meta = ExampleMetadata()
    capture_out = False
    for line in code_text.splitlines():
        stripped = line.strip()
        if capture_out:
            if stripped.startswith("#") or stripped.startswith("//"):
                comment = stripped.lstrip("#/").strip()
                if comment.startswith("EXPECT:") or comment.startswith("SKIP") or comment.startswith("TIMEOUT:"):
                    capture_out = False
                else:
                    meta.expected_output.append(comment)
                    continue
            else:
                capture_out = False

        if stripped.startswith("#") or stripped.startswith("//"):
            comment = stripped.lstrip("#/").strip()
            if comment == "SKIP":
                meta.skip = True
            elif comment.startswith("TIMEOUT:"):
                try: meta.timeout = int(comment.split(":")[1].strip())
                except: pass
            elif comment.startswith("EXPECT:"):
                parts = comment.split(":")[1].strip().split()
                if parts:
                    if parts[0] == "SUCCESS": meta.expect_status = "SUCCESS"
                    elif parts[0] == "ERROR":
                        meta.expect_status = "ERROR"
                        if len(parts) > 1: meta.expect_code = parts[1].strip()
            elif comment == "OUTPUT:":
                capture_out = True
    return meta

def extract_code_blocks_from_md(md_path):
    blocks = []
    if not os.path.exists(md_path): return blocks
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    pattern = r"```zoren\n(.*?)```"
    matches = re.findall(pattern, content, re.DOTALL)
    for idx, code in enumerate(matches):
        blocks.append((f"{os.path.basename(md_path)}#block{idx+1}", code.strip()))
    return blocks

def verify_single_snippet(name, code, compiler_bin, verbose=False, show_out=False):
    meta = parse_code_metadata(code)
    if meta.skip or "shell" in code or code.startswith("# Verify"):
        return True, "SKIPPED", 0.0, "", True

    with tempfile.NamedTemporaryFile(suffix=".zor", mode="w", delete=False, encoding="utf-8") as tmp_src:
        tmp_src.write(code)
        tmp_src_path = tmp_src.name

    tmp_bin = tmp_src_path + ".bin"
    t0 = time.time()

    try:
        res = subprocess.run([compiler_bin, tmp_src_path, "-o", tmp_bin], capture_output=True, text=True, timeout=meta.timeout)
        compile_time = time.time() - t0
    except subprocess.TimeoutExpired:
        if os.path.exists(tmp_src_path): os.remove(tmp_src_path)
        if os.path.exists(tmp_bin): os.remove(tmp_bin)
        return False, f"Compilation Timeout ({meta.timeout}s)", 0.0, "", False
    except Exception as e:
        if os.path.exists(tmp_src_path): os.remove(tmp_src_path)
        if os.path.exists(tmp_bin): os.remove(tmp_bin)
        return False, f"Runner Error: {e}", 0.0, "", False

    if os.path.exists(tmp_src_path): os.remove(tmp_src_path)

    compile_success = (res.returncode == 0)
    stderr_out = res.stderr.strip()

    if meta.expect_status == "SUCCESS":
        if not compile_success:
            if os.path.exists(tmp_bin): os.remove(tmp_bin)
            return False, f"Expected SUCCESS, but compilation failed.\nCompiler Stderr:\n{stderr_out}", compile_time, "", False

        try:
            run_res = subprocess.run([tmp_bin], capture_output=True, text=True, timeout=meta.timeout)
        except subprocess.TimeoutExpired:
            if os.path.exists(tmp_bin): os.remove(tmp_bin)
            return False, f"Execution Timeout ({meta.timeout}s)", compile_time, "", False
        finally:
            if os.path.exists(tmp_bin): os.remove(tmp_bin)

        if run_res.returncode != 0:
            return False, f"Runtime failure (Exit Code {run_res.returncode})", compile_time, "", False

        if meta.expected_output:
            actual = [l.strip() for l in run_res.stdout.strip().splitlines() if l.strip()]
            expected = [l.strip() for l in meta.expected_output if l.strip()]
            if actual != expected:
                diff = f"Runtime Output Mismatch.\nExpected:\n  " + "\n  ".join(expected) + f"\nActual:\n  " + "\n  ".join(actual)
                return False, diff, compile_time, run_res.stdout.strip(), False

        return True, "PASS", compile_time, run_res.stdout.strip(), False
    else:
        if os.path.exists(tmp_bin): os.remove(tmp_bin)
        if compile_success:
            return False, "Expected Compilation Error, but compilation SUCCEEDED.", compile_time, "", False

        if meta.expect_code and meta.expect_code not in stderr_out:
            return False, f"Diagnostic Mismatch. Expected {meta.expect_code}\nStderr:\n{stderr_out}", compile_time, "", False

        return True, "PASS", compile_time, "", False

def main():
    parser = argparse.ArgumentParser(description="Zoren Executable Documentation Verification Engine")
    parser.add_argument("--compiler", default="Zoren_lang/zoren/target/release/zorenv1", help="Path to compiler binary")
    parser.add_argument("--docs-dir", default="Zoren_lang/docs", help="Path to docs directory")
    parser.add_argument("--filter", default="", help="Filter examples by substring")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--show-output", action="store_true", help="Display runtime stdout")
    parser.add_argument("--only-failed", action="store_true", help="Show failed tests only")

    args = parser.parse_args()

    compiler_bin = os.path.abspath(args.compiler)
    if not os.path.exists(compiler_bin):
        compiler_bin_debug = os.path.abspath("Zoren_lang/zoren/target/debug/zorenv1")
        if os.path.exists(compiler_bin_debug): compiler_bin = compiler_bin_debug
        else:
            print(f"{COLOR_RED}Error: Compiler binary not found at '{compiler_bin}'.{COLOR_RESET}")
            sys.exit(2)

    docs_dir = os.path.abspath(args.docs_dir)
    snippets = []

    # 1. Discover standalone .zor examples
    examples_dir = os.path.join(docs_dir, "examples")
    if os.path.exists(examples_dir):
        for f in sorted(os.listdir(examples_dir)):
            if f.endswith(".zor"):
                fp = os.path.join(examples_dir, f)
                with open(fp, "r", encoding="utf-8") as file_obj:
                    snippets.append((f"docs/examples/{f}", file_obj.read()))

    # 2. Discover markdown embedded code blocks
    for root, _, files in os.walk(docs_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                md_p = os.path.join(root, f)
                rel_p = os.path.relpath(md_p, docs_dir)
                for name, code in extract_code_blocks_from_md(md_p):
                    snippets.append((f"docs/{rel_p}:{name}", code))

    filtered = [s for s in snippets if args.filter in s[0]]

    print(f"{COLOR_BOLD}{COLOR_CYAN}=== Zoren Documentation Verification Engine ==={COLOR_RESET}")
    print(f"Compiler: {COLOR_GRAY}{compiler_bin}{COLOR_RESET}")
    print(f"Discovered {len(filtered)} documentation code snippets.\n")

    passed = 0
    failed = 0
    skipped = 0
    start_t = time.time()

    for name, code in filtered:
        ok, msg, ctime, stdout_str, is_skip = verify_single_snippet(name, code, compiler_bin, args.verbose, args.show_output)
        if is_skip:
            skipped += 1
            if not args.only_failed:
                print(f"{COLOR_YELLOW}SKIP{COLOR_RESET} {name}")
        elif ok:
            passed += 1
            if not args.only_failed:
                print(f"{COLOR_GREEN}PASS{COLOR_RESET} {name} {COLOR_GRAY}({ctime*1000:.1f}ms){COLOR_RESET}")
                if args.show_output and stdout_str:
                    for l in stdout_str.splitlines():
                        print(f"  {COLOR_CYAN}>{COLOR_RESET} {l}")
        else:
            failed += 1
            print(f"{COLOR_RED}FAIL{COLOR_RESET} {COLOR_BOLD}{name}{COLOR_RESET}")
            if msg:
                for l in msg.splitlines():
                    print(f"  {COLOR_GRAY}|{COLOR_RESET} {l}")
            print()

    total_time = time.time() - start_t

    print("
" + "="*70)
    print(f"{COLOR_BOLD}Zoren Documentation Verification Report{COLOR_RESET}")
    print("="*70)
    print(f"Total Snippets: {len(filtered)}")
    print(f"Passed:         {COLOR_GREEN}{passed}{COLOR_RESET}")
    print(f"Failed:         {COLOR_RED if failed > 0 else COLOR_GREEN}{failed}{COLOR_RESET}")
    print(f"Skipped:        {COLOR_YELLOW}{skipped}{COLOR_RESET}")
    print(f"Duration:       {total_time:.2f}s")
    print("="*70)

    if failed > 0: sys.exit(1)
    else: sys.exit(0)

if __name__ == "__main__":
    main()
