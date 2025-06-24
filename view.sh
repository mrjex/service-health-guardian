# Enable and start the service
sudo systemctl enable service-guardian
sudo systemctl start service-guardian

# Check status
sudo systemctl status service-guardian

# View logs
journalctl -u service-guardian -f


resourceMonitoring() {
    top -p $(pgrep -f service-guardian)
    htop -p $(pgrep -f service-guardian)
}

