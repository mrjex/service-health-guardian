"""Command-line interface for Service Health Guardian."""

import sys
import argparse
import logging
from typing import Optional, List
from .core import ServiceMonitor
from .config import Config

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_monitor(args: argparse.Namespace) -> None:
    """Run the service monitor daemon."""
    try:
        monitor = ServiceMonitor(args.config)
        logger.info("Starting service monitoring...")
        monitor.monitor_services()
    except Exception as e:
        logger.error(f"Error running monitor: {e}")
        sys.exit(1)

def check_service(args: argparse.Namespace) -> None:
    """Check health of a specific service."""
    try:
        monitor = ServiceMonitor(args.config)
        health = monitor.check_service_health(args.service_name)
        
        print(f"\nService: {args.service_name}")
        print(f"Status: {health['status']}")
        print("\nMetrics:")
        print(f"  CPU Usage: {health['metrics']['cpu_percent']}%")
        print(f"  Memory Usage: {health['metrics']['memory_percent']}%")
        print(f"  Network Connections: {health['metrics']['connections']}")
        
        if health['alerts']:
            print("\nAlerts:")
            for alert in health['alerts']:
                print(f"  - {alert}")
            
    except Exception as e:
        logger.error(f"Error checking service: {e}")
        sys.exit(1)

def list_services(args: argparse.Namespace) -> None:
    """List all monitored services."""
    try:
        config = Config(args.config)
        services = config.get_monitored_services()
        
        print("\nMonitored Services:")
        for service in services:
            print(f"  - {service}")
            
    except Exception as e:
        logger.error(f"Error listing services: {e}")
        sys.exit(1)

def view_logs(args: argparse.Namespace) -> None:
    """View service logs."""
    try:
        monitor = ServiceMonitor(args.config)
        logs = monitor.get_service_logs(args.service_name, args.lines)
        
        print(f"\nLast {args.lines} log lines for {args.service_name}:")
        for log in logs:
            print(log)
            
    except Exception as e:
        logger.error(f"Error getting logs: {e}")
        sys.exit(1)

def main() -> None:
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Service Health Guardian - Monitor and manage system services"
    )
    parser.add_argument(
        '--config', '-c',
        help='Path to configuration file',
        default=None
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')
    subparsers.required = True

    # Run command
    run_parser = subparsers.add_parser(
        'run',
        help='Run the service monitor daemon'
    )
    run_parser.set_defaults(func=run_monitor)

    # Check command
    check_parser = subparsers.add_parser(
        'check',
        help='Check health of a specific service'
    )
    check_parser.add_argument(
        'service_name',
        help='Name of the service to check'
    )
    check_parser.set_defaults(func=check_service)

    # List command
    list_parser = subparsers.add_parser(
        'list',
        help='List all monitored services'
    )
    list_parser.set_defaults(func=list_services)

    # Logs command
    logs_parser = subparsers.add_parser(
        'logs',
        help='View service logs'
    )
    logs_parser.add_argument(
        'service_name',
        help='Name of the service to view logs for'
    )
    logs_parser.add_argument(
        '--lines', '-n',
        type=int,
        default=50,
        help='Number of log lines to show'
    )
    logs_parser.set_defaults(func=view_logs)

    # Parse arguments and call appropriate function
    args = parser.parse_args()
    args.func(args) 