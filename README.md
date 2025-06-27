# Service Health Guardian

[![CI](https://github.com/mrjex/service-health-guardian/actions/workflows/ci.yml/badge.svg)](https://github.com/mrjex/service-health-guardian/actions)
[![codecov](https://img.shields.io/badge/codecov-100%25-brightgreen)](https://codecov.io/gh/mrjex/service-health-guardian)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Codespell](https://img.shields.io/badge/codespell-enabled-brightgreen)](https://github.com/codespell-project/codespell)
[![Pytest](https://img.shields.io/badge/pytest-enabled-brightgreen)](https://docs.pytest.org/)
[![PEP8](https://img.shields.io/badge/pep8-compliant-brightgreen)](https://peps.python.org/pep-0008/)

> A CLI tool that monitors `systemd` services using `systemctl` and `journalctl` commands.


## Get Started

1. Check the available services on your system:

```bash
# List all active services
systemctl list-units --type=service --state=active

# List ALL services (including inactive)
systemctl list-units --type=service --all
```

2. Add services to `config/guardian.yaml`

```yaml
services:
  - cron
  - snapd
  - sshd
  - nginx
  - ...
```

3. Setup virtual environment:

```bash
poetry lock

poetry install
```

4. Run service:

```bash
poetry run service-health-guardian --help
poetry run service-health-guardian --config config/guardian.yaml
```


## Tests

*CI pipeline artifacts in **CodeCov**:*

![codecov-artifacts](assets/codecov-coverage.PNG)


*Code coverage tests **locally**:*

![unit-tests](assets/unit-tests.jpg)
