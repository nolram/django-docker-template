#!/bin/sh
cd /var/projects/mywebsite && python manage.py migrate --no-input
#cd /var/projects/mywebsite && python manage.py collectstatic --no-input
sudo supervisord -n -c /etc/supervisor/supervisord.conf
