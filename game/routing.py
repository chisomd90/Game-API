# game/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from game import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/game/<int:game_id>/", consumers.GameConsumer.as_asgi()),
    ]),
})
