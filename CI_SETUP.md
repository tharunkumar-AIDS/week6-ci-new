# CI Pipeline Documentation

## 1. Tool choice – why GitHub Actions
Public, free for public repos, native to GitHub, YAML, matrix builds, artifact upload, Actions logs. Alternatives: Travis CI (limited free), CircleCI (external account).

## 2. Config (.github/workflows/ci.yml)
on push/pull_request to main/master. jobs.build runs ubuntu-latest, matrix python 3.10/3.11.
Steps: checkout v4, setup-python v5, pip install -r requirements, flake8 critical then style (max-line 100), pytest -v --junitxml=test-report.xml (non-zero fails job), upload-artifact v4 always.

## 3. Tests
TestMathOps (12), TestStrings (4), TestParsing (4), TestIntegration (2). Total 22 passing.

## 4. Replicate
Python 3.10+, pip install -r requirements.txt. No DB/secrets. Same 3 local commands as README.

## 5. Logs
Local: pytest -v console + ci_logs.txt + test-report.xml. GitHub: push -> Actions tab -> run -> per-step logs -> Artifacts.

## 6. Challenges
Missing pytest/flake8 fixed via pip. Import path fixed with src/__init__.py and from src.mymodule import. E302 fixed with blank lines. Cross-OS via relative paths. Report preserved with if:always().

## 7. Quality gate
Lint blocks syntax errors, full suite blocks regressions, matrix ensures 3.10/3.11 compat.
