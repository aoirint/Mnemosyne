#!/bin/bash

set -eu

echo "Waiting Database"
if [ "${DJANGO_DATABASE_ENGINE}" = "django.db.backends.mysql" ]; then
  wait-for-it "${DJANGO_DATABASE_HOST:-localhost}:${DJANGO_DATABASE_PORT:-3306}"
fi

python3 /code/manage.py collectstatic --no-input
python3 /code/manage.py migrate --no-input

if [ $? != 0 ]; then
  echo 'Failed to migrate DB.'
  exit 1
fi

exec "$@"
