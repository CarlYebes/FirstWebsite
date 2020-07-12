import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

web: gunicorn SecondWebsite.wsgi --log-file -
python manage.py makemigrations
python manage.py migrate