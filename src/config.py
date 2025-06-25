"""Configuration handling for service monitoring."""

import yaml
from typing import List

DEFAULT_CONFIG_PATH = "/etc/service-guardian/guardian.yaml"

class Config:
    """Simple configuration manager."""
    
    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH):
        self.config_path = config_path
        self.services: List[str] = []
        self.load_config()
    
    def load_config(self) -> None:
        """Load services from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
                self.services = config.get('services', [])
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML configuration: {e}")
    
    def get_monitored_services(self) -> List[str]:
        """Get list of services to monitor."""
        return self.services