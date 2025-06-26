"""Shared test fixtures."""

import pytest
import yaml


@pytest.fixture
def mock_systemctl_output():
    """Mock systemctl output for different states."""
    return {
        "active": "active\n",
        "inactive": "inactive\n",
        "failed": "failed\n",
        "unknown": "unknown\n",
    }


@pytest.fixture
def sample_config(tmp_path):
    """Create a temporary config file for testing."""
    config_file = tmp_path / "guardian.yaml"
    config_content = {"services": ["test-service", "another-service"]}
    config_file.write_text(yaml.dump(config_content))
    return str(config_file)
