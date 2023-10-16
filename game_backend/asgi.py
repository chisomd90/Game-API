"""
ASGI config for game_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# asgi.py

import os
from django.core.asgi import get_asgi_application
from game.routing import ProtocolTypeRouter, URLRouter # Import your routing configuration

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter,  # Use your WebSocket routing configuration
})
