"""Tests for configuration handling."""

import pytest

from src.config import Config


def test_load_config(sample_config):
    """Test loading a valid configuration file."""
    config = Config(config_path=sample_config)
    services = config.get_monitored_services()
    assert len(services) == 2
    assert "test-service" in services
    assert "another-service" in services


def test_config_file_not_found():
    """Test handling of missing config file."""
    with pytest.raises(FileNotFoundError):
        Config(config_path="nonexistent.yaml")


def test_invalid_yaml_config(tmp_path):
    """Test handling of invalid YAML."""
    config_file = tmp_path / "invalid.yaml"
    config_file.write_text("invalid: [\nyaml: content")

    with pytest.raises(ValueError):
        Config(config_path=str(config_file))


def test_empty_config(tmp_path):
    """Test handling of empty config file."""
    config_file = tmp_path / "empty.yaml"
    config_file.write_text("")

    config = Config(config_path=str(config_file))
    assert config.get_monitored_services() == []
