# set async_mode to 'threading', 'eventlet', 'gevent' or 'gevent_uwsgi' to
# force a mode else, the best mode is selected automatically from what's
# installed
async_mode = None

import os

from django.http import JsonResponse
from .socket import sio, background_thread

thread = None


def index(request):
    global thread

    if thread is None:
        thread = sio.start_background_task(background_thread)

    return JsonResponse({'status': 'ok'})
