poetry run tox -e lint

poetry run tox -e format

poetry run ruff check .


runUnitTests() {
    poetry run pytest
}