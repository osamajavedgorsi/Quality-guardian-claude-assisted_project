---
name: verify-quality
description: Run when code is edited to verify tests pass and no test was weakened.
---

# Verification Procedure

1. 1. Run `python -m pytest tests/ -v` and `python -m flake8 src/`.
2. Read the `git diff` of the current session.
3. Check that no test has been weakened (e.g., `assert True` replacing a real assertion).
4. Report pass/fail with evidence.
5. If any test was weakened, flag it as a critical failure.