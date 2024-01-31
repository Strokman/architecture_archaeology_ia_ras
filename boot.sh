#!/bin/bash

python3 manage.py migrate --noinput
python3 manage.py collectstatic
python3 manage.py loaddata countries regions building_parts colors buildings filetypes materials pigments preservations storages arch_sites
gunicorc architecture_archaeology.wsgi --bind 0.0.0.0:8000 --log-level debug