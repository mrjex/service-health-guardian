"""Configuration handling for service monitoring."""

from pathlib import Path
from typing import List
import yaml

DEFAULT_CONFIG_PATH = "/etc/service-guardian/guardian.yaml"


class Config:
    """Simple configuration manager."""

    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.services: List[str] = []
        self.load_config()

    def load_config(self) -> None:
        """Load services from YAML file."""
        try:
            with self.config_path.open() as f:
                config = yaml.safe_load(f) or {}  # Handle empty files by defaulting to empty dictionary
                self.services = config.get('services', [])
        except FileNotFoundError as err:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}") from err
        except yaml.YAMLError as err:
            raise ValueError(f"Invalid YAML configuration: {err}") from err

    def get_monitored_services(self) -> List[str]:
        """Get list of services to monitor."""
        return self.services
