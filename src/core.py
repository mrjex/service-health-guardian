"""Core service monitoring functionality."""

import subprocess
import logging
from .config import Config

logger = logging.getLogger(__name__)

class ServiceMonitor:
    """Simple service status monitor."""
    
    def __init__(self, config_path: str = None):
        self.config = Config(config_path) if config_path else Config()
    
    def check_service_status(self, service_name: str) -> str:
        """Check status of a service using systemctl."""
        if service_name not in self.config.get_monitored_services():
            raise KeyError(f"Service {service_name} not configured for monitoring")
        
        try:
            result = subprocess.run(
                ['systemctl', 'is-active', service_name],
                capture_output=True,
                text=True,
                check=False
            )
            return result.stdout.strip()
        except subprocess.SubprocessError as e:
            logger.error(f"Error getting status for {service_name}: {e}")
            return "unknown" 