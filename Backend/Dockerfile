FROM python:3.12

WORKDIR /app

# Copy the directory
COPY . $WORKDIR

RUN apt-get update && \
    apt-get install -y ffmpeg build-essential gcc netcat-openbsd

# Install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# WORKDIR /app/videoflix

# Run migrations and collect static files
# RUN python manage.py makemigrations && \
#     python manage.py migrate && \
#     python manage.py collectstatic --noinput

# Create a superuser using environment variables
# ARG DJANGO_SUPERUSER_USERNAME
# ARG DJANGO_SUPERUSER_EMAIL
# ARG DJANGO_SUPERUSER_PASSWORD
# RUN python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --password $DJANGO_SUPERUSER_PASSWORD

EXPOSE 8060
# Start Django

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]