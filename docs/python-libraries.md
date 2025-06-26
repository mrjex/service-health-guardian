# Python Libraries Used In This Project

**TODO:**

- isort
- codespell
- pep8-naming


- Black
- flake8, flake8-docstrings, flake8-copyright, flake8-builtins, pyproject-flake8


- coverage.run
- coverage.report

coverage run -m pytest
coverage report

poetry add --group dev coverage

setup using pyproject.toml and tox.ini?

tox.ini:

```
[testenv]
deps =
    pytest
    coverage
commands =
    coverage run -m pytest
    coverage report

```