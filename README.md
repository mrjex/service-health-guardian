# Service Health Guardian


- The guardian service starts up through `systemd`

- It reads configuration for which services to monitor

- Checks status using `systemctl`

- Collects metrics using `ps/top`

- Monitors logs using `journalctl`