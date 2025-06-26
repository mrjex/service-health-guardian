# Package Distribution Guide

This document outlines how Service Health Guardian is distributed and deployed.

## Build Process

We use Poetry for package management and distribution. Poetry handles both dependency management and package building.

### Building the Package

To build distribution packages, run:
```bash
poetry build
```

This produces two files in the `dist/` directory:
- `*.tar.gz` - Source distribution (sdist)
- `*.whl` - Built distribution (wheel)

## Distribution Methods

### 1. PyPI Distribution
The package can be shared on the Python Package Index (PyPI), allowing users to install it via pip:
```bash
pip install service-health-guardian
```

### 2. Production Deployment
- Supports direct installation in production environments
- Enables version control of releases
- Can be installed via pip from a private package repository
- Supports installation from local distribution files:
  ```bash
  pip install dist/service-health-guardian-*.whl
  ```

### 3. Testing and Verification
- Distribution packages can be tested in isolated environments
- Verify installation process works as expected

## Best Practices
- Always update version numbers in pyproject.toml before building
- Test the built package in a clean virtual environment