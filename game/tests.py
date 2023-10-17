# from django.test import TestCase
# from .models import Game

# class GameModelTestCase(TestCase):
#     def test_create_game(self):
#         game = Game.objects.create(name="Test Game", description="This is a test game.")
#         self.assertEqual(game.name, "Test Game")
#         self.assertEqual(game.description, "This is a test game.")
#         self.assertTrue(game.is_active)

#     def test_game_str_method(self):
#         game = Game.objects.create(name="Another Game", description="Description")
#         self.assertEqual(str(game), "Another Game")

from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from channels.testing import ChannelsLiveServerTestCase
from asgiref.testing import ApplicationCommunicator
from game.models import Game
import json

from game.consumers import GameConsumer

class WebSocketTestCase(ChannelsLiveServerTestCase):

    @database_sync_to_async
    def create_game(self):
        # Create a test game
        return Game.objects.create(name="Test Game", description="This is a test game.")

    async def connect_ws(self, game_id):
        communicator = ApplicationCommunicator(
            GameConsumer,
            f"/ws/game/{game_id}/",
        )
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected, "WebSocket connection failed.")
        return communicator

    async def disconnect_ws(self, communicator):
        await communicator.disconnect()

    async def test_websocket_connection(self):
        # Replace this with your game_id retrieval logic
        game_id = await self.create_game().id
        communicator = await self.connect_ws(game_id)
        await self.disconnect_ws(communicator)

    async def test_send_and_receive_message(self):
        game = await self.create_game()
        game_id = game.id
        communicator = await self.connect_ws(game_id)

        # Define the message you want to send
        message = {"type": "game.update", "message": {"your": "data"}}

        # Send the message
        await communicator.send_json_to(message)

        # Receive the response
        response = await communicator.receive_json_from()
        self.assertEqual(response, message, "Received message does not match sent message.")

        await self.disconnect_ws(communicator)
