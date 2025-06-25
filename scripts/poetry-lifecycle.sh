###   POETRY LIFECYCLE   ##
#
# -  Prerequesite: Poetry installed


poetry install


poetry run service-guardian --help


poetry run service-guardian list
poetry run service-guardian check sshd

poetry build  # Creates both .whl and .tar.gz


poetry lock # Fix the lock file


# poetry env info

# eval $(poetry env activate)


