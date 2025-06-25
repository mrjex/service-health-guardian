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



## Metrics Collected

- CPU usage percentage

- Memory usage percentage

- Disk I/O

- Process status (running/stopped/failed)

- Error logs

- Restart counts


Sample log output:

```
[INFO] nginx.service: CPU: 2.5%, Memory: 125MB, Status: active
[INFO] postgresql.service: CPU: 4.1%, Memory: 450MB, Status: active
[WARN] mongodb.service: Memory usage above threshold (92%)
[ERROR] docker.service: Service stopped unexpectedly, attempting restart
```
