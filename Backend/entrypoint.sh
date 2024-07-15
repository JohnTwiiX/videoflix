#!/usr/bin/env bash
set -e

echo "Waiting for postgres to connect ..."
while ! nc -z videoflix-db 5432; do
  sleep 0.1
done
echo "PostgreSQL is active"

# Warten Sie, bis die Django-Anwendung vollständig initialisiert ist
python manage.py check --deploy  # Dies prüft, ob die App bereit ist
echo "Django application is ready"

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# Start Gunicorn mit 3 Arbeitern
gunicorn videoflix.wsgi:application --bind 0.0.0.0:8000 --timeout 300 --workers 3 &

# Start RQ Worker
python manage.py rqworker default
