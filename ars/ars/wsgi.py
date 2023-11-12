# -*- coding: utf-8 -*-
import os
import sys
import platform
#путь к проекту, там где manage.py
sys.path.insert(0, '/home/d/dsmast0f/ars-76.ru/public_html/ars')
#путь к фреймворку, там где settings.py
sys.path.insert(0, '/home/d/dsmast0f/ars-76.ru/public_html/ars/ars')
#путь к виртуальному окружению myenv
sys.path.insert(0, '/home/d/dsmast0f/ars-76.ru/myenv/lib/python3.11/site-packages')
#sys.path.insert(0, '/home/c/cx53558/newsite/myenv/lib/python3.6/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "ars.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
