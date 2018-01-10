#!/bin/sh
cd /var/projects/mywebsite && python manage.py migrate --no-input
#cd /var/projects/mywebsite && python manage.py collectstatic --no-input
service supervisor restart
supervisord -n -u mywebsiteuser -c /etc/supervisor/supervisord.conf
supervisorctl reread
supervisorctl update
