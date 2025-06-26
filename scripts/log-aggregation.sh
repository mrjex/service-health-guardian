#!/bin/bash

##  LOG AGGREGATION  ##
#
# - Functions for checking service status and logs
# - Each function takes a service name as its only argument

serviceIsActive() {
    local service_name="$1"
    systemctl is-active "$service_name.service"
}

getServiceDetails() {
    local service_name="$1"
    # Get detailed status of the service
    systemctl status "$service_name.service"
    
    # View resource usage
    ps aux | grep "$service_name"
    top -p $(pgrep "$service_name")
}

getServiceLogs() {
    local service_name="$1"
    # View logs with timestamps
    journalctl -u "$service_name.service" --output=short-precise -n 50 -f
}
