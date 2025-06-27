##  CODE QUALITY LIFECYCLE  ##
#
# -  This script is intended for developers or colleagues who work on the project


# Debug specific rulesets configured for Ruff (more info in pyproject.toml)
debugRuffRules() {
    poetry run ruff check . --select I      # Check import sorting (isort library)
    poetry run ruff check . --select N      # Check naming conventions (pep8-naming library)
}

runCodeSpellChecks() {
    poetry run codespell                    # Check spelling
    poetry run codespell --write-changes    # Fix spelling
}

# Run tox checks for CI pipeline. Refer to tox.ini for more details on the different environments
runToxCI() {
    poetry run tox -e format               # Run all formatters
    poetry run tox -e lint                 # Run all linting checks
    poetry run tox -e test                 # Run all tests
}
