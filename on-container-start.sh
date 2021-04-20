python3 manage.py migrate
gunicorn --reload app.wsgi:application -b 0.0.0.0:8000