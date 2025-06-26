"""Configuration handling for service health guardian."""

import yaml
from typing import List

DEFAULT_CONFIG_PATH = "/etc/service-guardian/guardian.yaml"

class Config:
    """Configuration for service monitoring."""

    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH) -> None:
        """Initialize with path to config file."""
        self.config_path = config_path
        self.services = []
        self.load_config()

    def load_config(self) -> None:
        """Load services from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f) or {}  # Handle empty files
                self.services = config.get('services', [])
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        except yaml.YAMLError:
            raise ValueError(f"Invalid YAML in config file: {self.config_path}")

    def get_monitored_services(self) -> List[str]:
        """Return list of services to monitor."""
        return self.services