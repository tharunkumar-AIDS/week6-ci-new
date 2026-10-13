# Week 6 – Continuous Integration (CI) in Python Projects

Reused project: Week 3 `mymodule.py` utility library (13 pure functions) with 22 automated tests.
CI tool: **GitHub Actions** (`.github/workflows/ci.yml`).

## Project structure
```
Week6_CI/
  src/mymodule.py
  tests/test_mymodule.py
  .github/workflows/ci.yml
  requirements.txt
  README.md
  CI_SETUP.md
  ci_logs.txt
  test-report.xml
```

## What CI automates
1. Linting – flake8 (fails on E9,F63,F7,F82; style gate max-line 100)
2. Tests – pytest -v --junitxml=test-report.xml (22 tests)
3. Report – JUnit XML uploaded as artifact
4. Pipeline fails if any test fails (pytest exit != 0).

## Run locally
pip install -r requirements.txt
python -m flake8 src tests --count --select=E9,F63,F7,F82 --show-source --statistics
python -m flake8 src tests --count --max-complexity=10 --max-line-length=100 --statistics
python -m pytest tests/ -v --junitxml=test-report.xml

## Trigger CI on GitHub
git init, commit, push to main. Every push/pull_request triggers workflow.
Check: repo Actions tab -> Python CI -> logs -> download test-report artifact.
