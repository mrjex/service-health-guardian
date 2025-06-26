#!/bin/bash

##  SHELL SOLUTION  ##
#
# - Shell implementation of service monitoring using functions from log-aggregation.sh

# Source the functions
source "$(dirname "$0")/log-aggregation.sh"

# Read and parse services from guardian.yaml
while IFS=': ' read -r line; do
    if [[ $line =~ ^[[:space:]]*-[[:space:]]*([^#[:space:]]+) ]]; then
        service="${BASH_REMATCH[1]}"
        echo "Checking service: $service"
        status=$(serviceIsActive "$service")
        echo "Status: $status"
    fi
done < "../config/guardian.yaml"

# Example of how to use individual functions:
# serviceIsActive "nginx"
# getServiceDetails "postgresql"
# getServiceLogs "docker"
