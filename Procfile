import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

web: gunicorn SecondWebsite.wsgi --log-file -
release: python manage.py makemigrations
release: python manage.py migrate --noinput
