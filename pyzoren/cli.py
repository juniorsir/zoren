"""Command-line interface for pyzoren."""

import sys
import pyzoren

def main() -> None:
    if len(sys.argv) < 2:
        print("PyZoren CLI - Python Bridge for Zoren Language Platform")
        print("Usage:")
        print("  python3 -m pyzoren run <file.zor> [args...]")
        print("  python3 -m pyzoren eval <expr>")
        print("  python3 -m pyzoren doctor <file.zor>")
        print("  python3 -m pyzoren fmt <file.zor>")
        sys.exit(1)

    subcmd = sys.argv[1]
    if subcmd == "run":
        if len(sys.argv) < 3:
            print("Error: missing file path for 'run'")
            sys.exit(1)
        res = pyzoren.run(sys.argv[2], *sys.argv[3:])
        print(res.stdout, end="")
        if res.stderr:
            print(res.stderr, file=sys.stderr, end="")
        sys.exit(res.exit_code)
    elif subcmd == "eval":
        if len(sys.argv) < 3:
            print("Error: missing expression to eval")
            sys.exit(1)
        expr = " ".join(sys.argv[2:])
        val = pyzoren.eval_expr(expr)
        print(val)
    elif subcmd == "doctor":
        if len(sys.argv) < 3:
            print("Error: missing file path for 'doctor'")
            sys.exit(1)
        res = pyzoren.doctor(sys.argv[2])
        print(res.stdout, end="")
        sys.exit(res.exit_code)
    elif subcmd == "fmt":
        if len(sys.argv) < 3:
            print("Error: missing file path for 'fmt'")
            sys.exit(1)
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            content = f.read()
        formatted = pyzoren.format_code(content)
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(formatted)
        print(f"Formatted '{sys.argv[2]}'")
    else:
        print(f"Unknown command: {subcmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
