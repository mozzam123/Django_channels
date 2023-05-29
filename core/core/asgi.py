import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from home.consumers import *


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_asgi_application()


ws_patterns = [
    path('ws/test/', TestConsumer())

]


application = ProtocolTypeRouter({
        'websocket': URLRouter(ws_patterns)
    })