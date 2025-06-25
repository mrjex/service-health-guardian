###   POETRY LIFECYCLE   ##
#
# -  This script is intended for developers or colleagues who want to work on the project



setupPoetry() {
    echo "---   1. SETUP POETRY   ---"
    poetry lock # Fix the lock file
    poetry install
}

runServiceGuardian() {
    echo "---   2. RUN SERVICE GUARDIAN   ---"
    poetry run service-health-guardian --help
    poetry run service-health-guardian --config config/guardian.yaml cron
}

packageServiceGuardian() {
    echo "---   3. PACKAGE SERVICE GUARDIAN   ---"
    poetry build  # Creates both .whl and .tar.gz
}



##  MAIN  ##

setupPoetry
runServiceGuardian
packageServiceGuardian
