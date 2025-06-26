"""Tests for core service monitoring functionality."""

import subprocess
from unittest.mock import patch

import pytest

from src.core import ServiceMonitor

EXPECTED_SERVICE_COUNT = 2


@pytest.fixture
def service_monitor(sample_config):
    """Create a ServiceMonitor instance for testing."""
    return ServiceMonitor(config_path=sample_config)


@pytest.fixture
def mock_config():
    """Mock configuration with test services."""
    with patch("src.core.Config") as mock:
        mock.return_value.get_monitored_services.return_value = [
            "test-service",
            "another-service",
        ]
        yield mock


def test_check_service_status_active(service_monitor):
    """Test checking an active service."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "active\n"
        status = service_monitor.check_service_status("test-service")
        assert status == "active"
        mock_run.assert_called_once_with(
            ["systemctl", "is-active", "test-service"],
            capture_output=True,
            text=True,
            check=False,
        )


def test_check_service_status_inactive(service_monitor):
    """Test checking an inactive service."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "inactive\n"
        status = service_monitor.check_service_status("test-service")
        assert status == "inactive"


def test_check_service_status_error(service_monitor):
    """Test handling subprocess errors."""
    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.SubprocessError()
        status = service_monitor.check_service_status("test-service")
        assert status == "unknown"


def test_check_all_services(service_monitor, mock_config):
    """Test checking multiple services."""
    with patch.object(service_monitor, "check_service_status") as mock_check:
        mock_check.side_effect = ["active", "inactive"]

        results = service_monitor.check_all_services()
        
        assert len(results) == EXPECTED_SERVICE_COUNT
        assert results == {"test-service": "active", "another-service": "inactive"}
        assert mock_check.call_count == EXPECTED_SERVICE_COUNT
