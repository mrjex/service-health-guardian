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

def check_service(args: argparse.Namespace) -> None:
    """Check status of a service."""
    try:
        monitor = ServiceMonitor(args.config)
        status = monitor.check_service_status(args.service_name)
        print(f"\nService: {args.service_name}")
        print(f"Status: {status}")
    except Exception as e:
        logger.error(f"Error checking service: {e}")
        sys.exit(1)

def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Service Health Guardian - Simple service status monitor"
    )
    parser.add_argument(
        '--config', '-c',
        help='Path to configuration file',
        default=None
    )
    parser.add_argument(
        'service_name',
        help='Name of the service to check'
    )
    
    args = parser.parse_args()
    check_service(args) 