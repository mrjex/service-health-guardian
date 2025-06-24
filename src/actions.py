"""Service management actions."""

import subprocess
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class ServiceActions:
    """Handle service management actions."""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
    
    def restart_service(self) -> bool:
        """Restart the service."""
        try:
            subprocess.run(
                ['systemctl', 'restart', self.service_name],
                check=True,
                capture_output=True
            )
            logger.info(f"Successfully restarted {self.service_name}")
            return True
        except subprocess.SubprocessError as e:
            logger.error(f"Failed to restart {self.service_name}: {e}")
            return False
    
    def stop_service(self) -> bool:
        """Stop the service."""
        try:
            subprocess.run(
                ['systemctl', 'stop', self.service_name],
                check=True,
                capture_output=True
            )
            logger.info(f"Successfully stopped {self.service_name}")
            return True
        except subprocess.SubprocessError as e:
            logger.error(f"Failed to stop {self.service_name}: {e}")
            return False
    
    def start_service(self) -> bool:
        """Start the service."""
        try:
            subprocess.run(
                ['systemctl', 'start', self.service_name],
                check=True,
                capture_output=True
            )
            logger.info(f"Successfully started {self.service_name}")
            return True
        except subprocess.SubprocessError as e:
            logger.error(f"Failed to start {self.service_name}: {e}")
            return False
    
    def adjust_priority(self, nice_value: int) -> bool:
        """Adjust service process priority."""
        try:
            pid = self._get_service_pid()
            if pid:
                subprocess.run(
                    ['renice', '-n', str(nice_value), '-p', str(pid)],
                    check=True,
                    capture_output=True
                )
                logger.info(f"Adjusted priority of {self.service_name} to {nice_value}")
                return True
            return False
        except subprocess.SubprocessError as e:
            logger.error(f"Failed to adjust priority for {self.service_name}: {e}")
            return False
    
    def _get_service_pid(self) -> Optional[int]:
        """Get the main PID of the service."""
        try:
            result = subprocess.run(
                ['systemctl', 'show', self.service_name, '-p', 'MainPID'],
                capture_output=True,
                text=True,
                check=True
            )
            pid = int(result.stdout.split('=')[1].strip())
            return pid if pid > 0 else None
        except (subprocess.SubprocessError, ValueError, IndexError):
            return None 