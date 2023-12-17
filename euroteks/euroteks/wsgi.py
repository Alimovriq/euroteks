"""
Настройки для локального сервера.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'euroteks.settings')

application = get_wsgi_application()


"""
//////////////////////////////
Настройки для хостинга timeweb.
"""

"""
import os
import sys
import platform

#путь к проекту, где manage.py
sys.path.insert(0, '/home/e/euroteks/django_1/public_html/euroteks')
#путь к фреймворку, где settings.py
sys.path.insert(0, '/home/e/euroteks/django_1/public_html/euroteks/euroteks')
#путь к виртуальному окружению venv
sys.path.insert(0, '/home/e/euroteks/django_1/venv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "euroteks.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""

