"""Core monitoring functionality."""

import time
import logging
from typing import Dict, Any
from .config import Config
from .metrics import ServiceMetrics
from .actions import ServiceActions

logger = logging.getLogger(__name__)

class ServiceMonitor:
    """Main service monitoring class."""
    
    def __init__(self, config_path: str = None):
        self.config = Config(config_path) if config_path else Config()
        self.services: Dict[str, Dict[str, Any]] = {}
        self._initialize_services()
    
    def _initialize_services(self) -> None:
        """Initialize monitoring for configured services."""
        for service_name in self.config.get_monitored_services():
            service_config = self.config.get_service_config(service_name)
            self.services[service_name] = {
                'config': service_config,
                'metrics': ServiceMetrics(service_name),
                'actions': ServiceActions(service_name)
            }
    
    def check_service_health(self, service_name: str) -> Dict[str, Any]:
        """Check health of a specific service."""
        if service_name not in self.services:
            raise KeyError(f"Service {service_name} not configured for monitoring")
        
        service = self.services[service_name]
        metrics = service['metrics'].get_metrics()
        status = service['metrics'].get_service_status()
        config = service['config']
        
        health_status = {
            'status': status,
            'metrics': metrics,
            'alerts': []
        }
        
        # Check thresholds
        if metrics['cpu_percent'] > config.get('cpu_threshold', 80):
            health_status['alerts'].append(f"CPU usage ({metrics['cpu_percent']}%) exceeds threshold")
            
        if metrics['memory_percent'] > config.get('memory_threshold', 80):
            health_status['alerts'].append(f"Memory usage ({metrics['memory_percent']}%) exceeds threshold")
        
        # Auto-restart if configured and service is not active
        if status != 'active' and config.get('auto_restart', False):
            logger.warning(f"Service {service_name} is {status}, attempting restart")
            if service['actions'].restart_service():
                health_status['alerts'].append("Service was automatically restarted")
        
        return health_status
    
    def monitor_services(self) -> None:
        """Continuous monitoring of all services."""
        while True:
            for service_name in self.services:
                try:
                    health = self.check_service_health(service_name)
                    
                    if health['alerts']:
                        logger.warning(f"Service {service_name} alerts: {', '.join(health['alerts'])}")
                    else:
                        logger.info(
                            f"Service {service_name} - Status: {health['status']}, "
                            f"CPU: {health['metrics']['cpu_percent']}%, "
                            f"Memory: {health['metrics']['memory_percent']}%"
                        )
                    
                except Exception as e:
                    logger.error(f"Error monitoring {service_name}: {e}")
                
                # Use service-specific check interval or global default
                check_interval = self.services[service_name]['config'].get('check_interval', 60)
                time.sleep(check_interval)
    
    def get_service_logs(self, service_name: str, num_lines: int = 100) -> list[str]:
        """Get recent logs for a service."""
        if service_name not in self.services:
            raise KeyError(f"Service {service_name} not configured for monitoring")
        
        return self.services[service_name]['metrics'].get_service_logs(num_lines) 