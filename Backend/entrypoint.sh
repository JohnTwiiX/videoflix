set -e

echo "Waiting for postgres to connect ..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL is active"

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn videoflix.wsgi:application --bind 0.0.0.0:8000 --timeout 300 --workers 3