"""
PyZoren: Official Production Python SDK for the Zoren Programming Language.

Provides zero-overhead execution, compilation, expression evaluation,
and native interop between Python and the Zoren Toolchain Platform.
"""

from __future__ import annotations

import os
import sys
import shutil
import subprocess
import time
from dataclasses import dataclass
from typing import Any, List, Optional, Union

__version__ = "1.0.0"
__all__ = [
    "ZorenResult",
    "ZorenSession",
    "run",
    "eval_expr",
    "compile_file",
    "doctor",
    "format_code",
    "find_zoren_binary",
]


def find_zoren_binary() -> str:
    """Locate the Zoren compiler executable."""
    env_path = os.environ.get("ZOREN_BIN")
    if env_path and os.path.exists(env_path) and os.access(env_path, os.X_OK):
        return env_path

    # Check common system & local locations
    candidates = [
        "/root/Zoren_lang/bin/zoren",
        "/usr/local/bin/zoren",
        os.path.expanduser("~/.zoren/bin/zoren"),
        shutil.which("zoren") or "",
    ]

    for cand in candidates:
        if cand and os.path.exists(cand) and os.access(cand, os.X_OK):
            return cand

    raise FileNotFoundError(
        "Zoren compiler executable not found. Ensure 'zoren' is in your PATH or set ZOREN_BIN."
    )


@dataclass(frozen=True)
class ZorenResult:
    """Result of a Zoren execution."""
    stdout: str
    stderr: str
    exit_code: int
    duration_ms: float

    @property
    def success(self) -> bool:
        return self.exit_code == 0

    def unwrap(self) -> str:
        if not self.success:
            raise RuntimeError(
                f"Zoren execution failed (exit code {self.exit_code}):\n{self.stderr or self.stdout}"
            )
        return self.stdout.strip()


def run(
    source_or_file: str,
    *args: str,
    timeout: float = 30.0,
    cwd: Optional[str] = None,
) -> ZorenResult:
    """
    Run a Zoren script file or inline Zoren code.
    
    Example:
        >>> import pyzoren
        >>> res = pyzoren.run("/path/to/script.zor")
        >>> print(res.stdout)
    """
    zoren_bin = find_zoren_binary()
    is_file = os.path.isfile(source_or_file)

    temp_file: Optional[str] = None
    target_file = source_or_file

    if not is_file:
        import tempfile
        fd, temp_file = tempfile.mkstemp(suffix=".zor", prefix="pyzoren_run_")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(source_or_file)
        target_file = temp_file

    cmd = [zoren_bin, "run", target_file, *args]

    t0 = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            cwd=cwd,
        )
        duration_ms = (time.perf_counter() - t0) * 1000.0
        return ZorenResult(
            stdout=proc.stdout,
            stderr=proc.stderr,
            exit_code=proc.returncode,
            duration_ms=duration_ms,
        )
    finally:
        if temp_file and os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except OSError:
                pass


def eval_expr(expression: str, timeout: float = 10.0) -> Any:
    """
    Evaluate a single Zoren expression and parse its returned value.
    
    Example:
        >>> import pyzoren
        >>> pyzoren.eval_expr("100 / 4")
        25
        >>> pyzoren.eval_expr("sqrt(144)")
        12
    """
    zoren_bin = find_zoren_binary()
    proc = subprocess.Popen(
        [zoren_bin, "repl"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    
    try:
        stdout, _ = proc.communicate(input=f"{expression}\n:quit\n", timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        raise TimeoutError(f"Zoren eval timed out for expression: {expression}")

    for line in stdout.splitlines():
        line_clean = line.strip()
        if "=>" in line_clean:
            # Format: => [Type]: Value
            parts = line_clean.split("=>", 1)[1].strip()
            if ":" in parts:
                _, val_str = parts.split(":", 1)
                val_str = val_str.strip()
                # Attempt standard Python conversions
                if val_str == "true":
                    return True
                if val_str == "false":
                    return False
                if val_str == "null":
                    return None
                if val_str.startswith('"') and val_str.endswith('"'):
                    return val_str[1:-1]
                try:
                    if "." in val_str:
                        return float(val_str)
                    return int(val_str)
                except ValueError:
                    return val_str
            return parts

    return None


def compile_file(
    source_file: str,
    output_binary: Optional[str] = None,
    fast: bool = True,
    secure: bool = True,
    timeout: float = 60.0,
) -> ZorenResult:
    """
    Compile a Zoren source file into an optimized AArch64 executable binary.
    """
    zoren_bin = find_zoren_binary()
    cmd = [zoren_bin, source_file]
    if output_binary:
        cmd.extend(["-o", output_binary])
    if fast:
        cmd.append("--fast")
    if secure:
        cmd.append("--secure")

    t0 = time.perf_counter()
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout,
    )
    duration_ms = (time.perf_counter() - t0) * 1000.0
    return ZorenResult(
        stdout=proc.stdout,
        stderr=proc.stderr,
        exit_code=proc.returncode,
        duration_ms=duration_ms,
    )


def doctor(source_file: str) -> ZorenResult:
    """Run Zoren Doctor diagnostics on a source file."""
    zoren_bin = find_zoren_binary()
    proc = subprocess.run(
        [zoren_bin, "doctor", source_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return ZorenResult(
        stdout=proc.stdout,
        stderr=proc.stderr,
        exit_code=proc.returncode,
        duration_ms=0.0,
    )


def format_code(code: str) -> str:
    """Format Zoren code string using the native formatter."""
    import tempfile
    fd, temp_file = tempfile.mkstemp(suffix=".zor", prefix="pyzoren_fmt_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(code)
        zoren_bin = find_zoren_binary()
        subprocess.run([zoren_bin, "fmt", temp_file], check=True, stdout=subprocess.PIPE)
        with open(temp_file, "r", encoding="utf-8") as f:
            return f.read()
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)


class ZorenSession:
    """
    Persistent interactive Zoren REPL session for Python applications.
    """
    def __init__(self) -> None:
        self.zoren_bin = find_zoren_binary()
        self._proc: Optional[subprocess.Popen] = None
        self._start()

    def _start(self) -> None:
        self._proc = subprocess.Popen(
            [self.zoren_bin, "repl"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )

    def execute(self, command: str) -> str:
        """Send a statement or expression to the active session."""
        if not self._proc or self._proc.poll() is not None:
            self._start()
        assert self._proc and self._proc.stdin and self._proc.stdout
        self._proc.stdin.write(f"{command}\n")
        self._proc.stdin.flush()
        # Read lines until prompt or output settles
        out_lines = []
        time.sleep(0.05)
        while True:
            line = self._proc.stdout.readline()
            if not line:
                break
            out_lines.append(line)
            if "❯" in line or "=>" in line:
                break
        return "".join(out_lines).strip()

    def close(self) -> None:
        if self._proc and self._proc.poll() is None:
            try:
                assert self._proc.stdin
                self._proc.stdin.write(":quit\n")
                self._proc.stdin.flush()
                self._proc.wait(timeout=2.0)
            except Exception:
                self._proc.kill()
        self._proc = None

    def __enter__(self) -> ZorenSession:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()
