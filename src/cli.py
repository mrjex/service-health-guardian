"""Command-line interface for service monitoring."""

import argparse
import logging
import sys

from .core import ServiceMonitor

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def check_services(args: argparse.Namespace) -> None:
    """Check status of all configured services."""
    try:
        monitor = ServiceMonitor(args.config)
        services = monitor.check_all_services()

        logger.info("Service Statuses:")
        logger.info("-----------------")
        for service_name, status in services.items():
            logger.info(f"{service_name}: {status}")

    except Exception as e:
        logger.error(f"Error checking services: {e}")
        sys.exit(1)


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Service Health Guardian - Monitor service statuses",
    )
    parser.add_argument(
        "--config", "-c", help="Path to configuration file", default=None,
    )

    args = parser.parse_args()
    check_services(args)
