###   POETRY LIFECYCLE   ##
#
# -  This script is intended for developers or colleagues who work on the project

# 1. Setup virtual environment
setupPoetry() {
    echo "---   1. SETUP POETRY   ---"
    poetry lock
    poetry install
}

# 2. Run the service
runServiceGuardian() {
    echo "---   2. RUN SERVICE GUARDIAN   ---"
    poetry run service-health-guardian --help
    poetry run service-health-guardian --config config/guardian.yaml
}

# 3. Package the service
packageServiceGuardian() {
    echo "---   3. PACKAGE SERVICE GUARDIAN   ---"
    poetry build  # Creates both .whl and .tar.gz
}

##  MAIN  ##

setupPoetry
runServiceGuardian
packageServiceGuardian
