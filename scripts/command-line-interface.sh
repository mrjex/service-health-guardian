# Check status of all monitored services
service-guardian status

# Check specific service
service-guardian check docker

# List all monitored services
service-guardian list

# Add new service to monitor
service-guardian add --service postgresql --check-interval 60

# View metrics
service-guardian metrics docker