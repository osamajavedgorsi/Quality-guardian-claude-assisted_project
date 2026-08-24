import subprocess
import sys
import os

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result

def main():
    # Run flake8
    print("Running flake8...")
    flake8_result = run_command("python -m flake8 src/")

    # Run pytest
    print("Running pytest...")
    pytest_result = run_command("python -m pytest tests/ -v")

    # Print outputs for Claude to see
    if flake8_result.stdout:
        print(flake8_result.stdout)
    if flake8_result.stderr:
        print(flake8_result.stderr)
    if pytest_result.stdout:
        print(pytest_result.stdout)
    if pytest_result.stderr:
        print(pytest_result.stderr)

    # If either failed, block the turn with exit code 2
    if flake8_result.returncode != 0 or pytest_result.returncode != 0:
        print("Quality gates failed. Please fix the issues above.", file=sys.stderr)
        sys.exit(2)  # CRITICAL: Exit 2 blocks Claude
    else:
        print("All quality gates passed.", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()