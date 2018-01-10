#!/bin/sh
cd /var/projects/mywebsite && python manage.py migrate --no-input
#cd /var/projects/mywebsite && python manage.py collectstatic --no-input
echo `whoiam`
echo `namei -mo /var/log/supervisor/supervisord.log`
supervisord -n -u mywebsiteuser -c /etc/supervisor/supervisord.conf
