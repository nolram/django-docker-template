#!/bin/sh

# prepare init migration
# su -m myuser -c "python manage.py makemigrations"
# migrate db, so we have the latest db schema
# su -m myuser -c "python manage.py migrate"
# start development server on public ip interface, on port 8000
su -m root -c "python manage.py test helloapp"