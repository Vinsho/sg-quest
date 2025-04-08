#!/bin/sh

echo "Running database migrations..."
flask db upgrade

echo "Starting application..."
exec gunicorn app:create_app\(\) -w 4 --bind 0.0.0.0:8000
