#!/bin/bash

python3 manage.py migrate --noinput
python3 manage.py collectstatic
python3 manage.py loaddata all
gunicorn architecture_archaeology.wsgi --bind 0.0.0.0:8000 --access-logfile - --error-logfile - --capture-output --enable-stdio-inheritance --log-level debug