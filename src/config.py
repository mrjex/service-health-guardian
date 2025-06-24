"""Configuration handling for Service Health Guardian."""

import os
from typing import Dict, Any
import yaml

DEFAULT_CONFIG_PATH = "/etc/service-guardian/guardian.yaml"

class Config:
    """Configuration manager for the service guardian."""
    
    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML configuration: {e}")
    
    def get_global_settings(self) -> Dict[str, Any]:
        """Get global configuration settings."""
        return self.config.get('global', {})
    
    def get_service_config(self, service_name: str) -> Dict[str, Any]:
        """Get configuration for a specific service."""
        services = self.config.get('services', {})
        if service_name not in services:
            raise KeyError(f"Service '{service_name}' not found in configuration")
        
        # Merge global defaults with service-specific config
        global_defaults = self.get_global_settings()
        service_config = services[service_name]
        
        return {**global_defaults, **service_config}
    
    def get_monitored_services(self) -> list[str]:
        """Get list of services to monitor."""
        return list(self.config.get('services', {}).keys())
    
    def get_alert_config(self) -> Dict[str, Any]:
        """Get alert configuration."""
        return self.config.get('alerts', {}) 