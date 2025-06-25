"""Command-line interface for service monitoring."""

import sys
import argparse
import logging
from .core import ServiceMonitor

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_services(args: argparse.Namespace) -> None:
    """Check status of all configured services."""
    try:
        monitor = ServiceMonitor(args.config)
        services = monitor.check_all_services()
        
        print("\nService Statuses:")
        print("-----------------")
        for service_name, status in services.items():
            print(f"{service_name}: {status}")
            
    except Exception as e:
        logger.error(f"Error checking services: {e}")
        sys.exit(1)

def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Service Health Guardian - Monitor service statuses"
    )
    parser.add_argument(
        '--config', '-c',
        help='Path to configuration file',
        default=None
    )
    
    args = parser.parse_args()
    check_services(args) 