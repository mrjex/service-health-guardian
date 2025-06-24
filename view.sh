# Service management
sudo systemctl start service-guardian
sudo systemctl status service-guardian

# Log viewing
journalctl -u service-guardian -f

# Resource monitoring
top -p $(pgrep -f service-guardian)
htop -p $(pgrep -f service-guardian)