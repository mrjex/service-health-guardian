


# Alternative 1
systemWideConfig() {
    # Create system config directory
    sudo mkdir -p /etc/service-guardian

    # Copy the config file
    sudo cp config/guardian.yaml /etc/service-guardian
}


# Alternative 2
localConfig() {
    service-guardian -c config/guardian.yaml list
    service-guardian -c config/guardian.yaml check docker
}
