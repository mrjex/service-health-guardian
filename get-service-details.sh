SERVICE_NAME="docker"

# Get detailed status of a specific service (example: nginx)
systemctl status $SERVICE_NAME.service

# View real-time resource usage of a service
ps aux | grep $SERVICE_NAME
top -p $(pgrep $SERVICE_NAME)