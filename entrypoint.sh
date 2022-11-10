python manage.py makemigrations --noinput
python manage.py migrate --noinput

gunicorn project.asgi:application -k uvicorn.workers.UvicornWorker -w $GUNICORN_WORKERS -b 0.0.0.0:8000
