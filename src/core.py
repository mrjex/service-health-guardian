"""Core service monitoring functionality."""

import logging
import subprocess
from typing import Dict, Optional

from .config import Config

logger = logging.getLogger(__name__)


class ServiceMonitor:
    """Simple service status monitor."""

    def __init__(self, config_path: Optional[str] = None):
        self.config = Config(config_path) if config_path else Config()

    def check_service_status(self, service_name: str) -> str:
        """Check status of a service using systemctl."""
        try:
            result = subprocess.run(
                ["systemctl", "is-active", service_name],
                capture_output=True,
                text=True,
                check=False,
            )
            return result.stdout.strip()
        except subprocess.SubprocessError as e:
            logger.error(f"Error getting status for {service_name}: {e}")
            return "unknown"

    def check_all_services(self) -> Dict[str, str]:
        """Check status of all configured services."""
        services = self.config.get_monitored_services()
        return {service: self.check_service_status(service) for service in services}
