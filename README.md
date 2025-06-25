# Service Health Guardian

This tool monitors `systemd` services (background processes/daemons that run on Linux systems), handling everything from your network stack to databases to web servers. Common examples include nginx (web server), postgresql (database), docker.service (container runtime), or ssh.service (secure shell).

- a Python CLI tool that monitors systemd services defined in a YAML configuration file
- It uses systemctl commands under the hood to interact with systemd services, with configuration managed by Poetry and testing handled by tox.

## Get Started


1. Install *poetry*

```
sudo apt install python3-poetry
```



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


```bash
# Check status of a service
service-health-guardian postgresql

# With custom config file
service-health-guardian --config /path/to/config.yaml postgresql
```
