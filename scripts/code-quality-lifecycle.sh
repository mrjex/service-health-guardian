
runUnitTests() {
    poetry run pytest
}

runRuffChecks() {
    poetry run ruff check .

    # isort (import sorting) - via Ruff
    poetry run ruff check . --select I  # Check import sorting
    poetry run ruff --fix .             # Fix import sorting

    # PEP 8 naming - via Ruff
    poetry run ruff check . --select N  # Check naming conventions
}

runCodeSpellChecks() {
    poetry run codespell                 # Check spelling
    poetry run codespell --write-changes # Fix spelling
}

runBlackChecks() {
    poetry run black --check .          # in lint
    poetry run black .                  # in format
}

runToxChecks() {
    poetry run tox -e lint             # Run all linting checks
    poetry run tox -e format           # Run all formatters
}
