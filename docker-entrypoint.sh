#!/bin/bash

python3 /code/manage.py migrate

exec "$@"

