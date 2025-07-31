#!/bin/bash

echo "Starting Django application..."

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the server
echo "Starting Gunicorn server..."
exec gunicorn myproject.wsgi:application 