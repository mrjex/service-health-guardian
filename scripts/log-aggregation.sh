##  LOG AGGREGATION  ##
#
# - Takes a systemd service as input argument and returns corresponding real-time logs



SERVICE_NAME="docker"


getServiceDetails() {
    # Get detailed status of a specific service (example: nginx)
    systemctl status $SERVICE_NAME.service

    # View real-time resource usage of a service
    ps aux | grep $SERVICE_NAME
    top -p $(pgrep $SERVICE_NAME)
}


getServiceLogs() {
    # View logs of any service (example: nginx)
    journalctl -u $SERVICE_NAME.service

    # View last 50 lines
    journalctl -u $SERVICE_NAME.service -n 50

    # Follow logs in real-time
    journalctl -u $SERVICE_NAME.service -f

    # View logs with timestamps
    journalctl -u $SERVICE_NAME.service --output=short-precise
}


getServiceDetails
getServiceLogs
