"""Service metrics collection functionality."""

import subprocess
from typing import Dict, Optional, List
import psutil
import logging

logger = logging.getLogger(__name__)

class ServiceMetrics:
    """Collect and analyze service metrics."""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
    
    def get_service_pid(self) -> Optional[int]:
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
        except (subprocess.SubprocessError, ValueError, IndexError) as e:
            logger.error(f"Failed to get PID for {self.service_name}: {e}")
            return None

    def get_metrics(self) -> Dict[str, float]:
        """Collect comprehensive service metrics."""
        metrics = {
            'cpu_percent': 0.0,
            'memory_percent': 0.0,
            'read_bytes': 0,
            'write_bytes': 0,
            'connections': 0
        }

        pid = self.get_service_pid()
        if not pid:
            return metrics

        try:
            process = psutil.Process(pid)
            
            # CPU and Memory
            metrics['cpu_percent'] = process.cpu_percent(interval=1)
            metrics['memory_percent'] = process.memory_percent()

            # I/O statistics
            io_counters = process.io_counters()
            metrics['read_bytes'] = io_counters.read_bytes
            metrics['write_bytes'] = io_counters.write_bytes

            # Network connections
            metrics['connections'] = len(process.connections())

            # Include child processes
            for child in process.children(recursive=True):
                try:
                    metrics['cpu_percent'] += child.cpu_percent(interval=0)
                    metrics['memory_percent'] += child.memory_percent()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            logger.error(f"Error collecting metrics for {self.service_name}: {e}")

        return metrics

    def get_service_status(self) -> str:
        """Get service status from systemd."""
        try:
            result = subprocess.run(
                ['systemctl', 'is-active', self.service_name],
                capture_output=True,
                text=True,
                check=False
            )
            return result.stdout.strip()
        except subprocess.SubprocessError as e:
            logger.error(f"Error getting status for {self.service_name}: {e}")
            return "unknown"

    def get_service_logs(self, num_lines: int = 100) -> List[str]:
        """Get recent service logs."""
        try:
            result = subprocess.run(
                ['journalctl', '-u', self.service_name, '--no-pager', '-n', str(num_lines)],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.splitlines()
        except subprocess.SubprocessError as e:
            logger.error(f"Error getting logs for {self.service_name}: {e}")
            return [] 