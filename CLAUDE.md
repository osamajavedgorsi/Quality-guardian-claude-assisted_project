# Project Rules for Code Quality Guardian
Always use `python -m pytest tests/ -v` from the project root. Never use bare pytest. Do not create conftest.py.

## Non-Negotiable Conventions
- All functions in `src/` MUST have Python type hints (e.g., `def add(a: int, b: int) -> int:`).
- NEVER use `print()` inside `src/`. Use logging if needed.
- All new utility functions go in `src/utils.py`.
- Unit tests go in `tests/` and must be named `test_*.py`.

## Emphasis Budget (HIGHEST PRIORITY)
- **IMPORTANT:** The Stop hook will block your turn if `pytest` or `flake8` fails. Do not claim "done" until you have fixed these errors.