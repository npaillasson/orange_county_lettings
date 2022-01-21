#!/bin/bash

if [ "$ENV" == "PRODUCTION" ]; then
  if [ "$SECRET_KEY" == "" ]; then
    echo "
WARNING! no environment variable containing the secret key was found, please read README.md for more information!
" ; exit 1
  fi
  gunicorn orange_county_project.wsgi:application --bind 0.0.0.0:$PORT
else
  python manage.py runserver 0.0.0.0:8000
fi