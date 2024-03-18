"""
WSGI config for api_saude project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import socketio

from django.core.wsgi import get_wsgi_application

from socketio_app.views import sio
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_saude.settings")



# application = get_wsgi_application()
django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)