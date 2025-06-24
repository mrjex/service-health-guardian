# Service Health Guardian

- The guardian service starts up through `systemd`

- It reads configuration for which services to monitor

- Checks status using `systemctl`

- Collects metrics using `ps/top`

- Monitors logs using `journalctl`



## Linux Management / Administration


In the **/etc** directory:

```bash
sudo mkdir -p /etc/service-guardian/
sudo cp config/guardian.yaml /etc/service-guardian/
sudo cp systemd/service-guardian.service /etc/systemd/system/
```


## Configuration

Periodically checks the configured `systemd` services and their correspodning status

**TODO:** Refer to the specific *.yaml* file here
