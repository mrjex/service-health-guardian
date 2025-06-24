# Service Health Guardian

This tool monitors `systemd` services (background processes/daemons that run on Linux systems), handling everything from your network stack to databases to web servers. Common examples include nginx (web server), postgresql (database), docker.service (container runtime), or ssh.service (secure shell).


- The guardian service starts up through `systemd`

- It reads configuration for which services to monitor

- Checks status using `systemctl`

- Collects metrics using `ps/top`

- Monitors logs using `journalctl`


To check all available services on your system:

```bash
# List all active services
systemctl list-units --type=service --state=active

# List ALL services (including inactive)
systemctl list-units --type=service --all
```




## Linux Management / Administration


Configuration in the **/etc** directory:

```bash
sudo mkdir -p /etc/service-guardian/
sudo cp config/guardian.yaml /etc/service-guardian/
sudo cp systemd/service-guardian.service /etc/systemd/system/
```

Service file in the **/etc/systemd/system** directory



Logs in the **/var/log** directory






## Configuration

Periodically checks the configured `systemd` services and their correspodning status

**TODO:** Refer to the specific *.yaml* file here
