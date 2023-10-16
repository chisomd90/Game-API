from django.test import TestCase
from .models import Game

class GameModelTestCase(TestCase):
    def test_create_game(self):
        game = Game.objects.create(name="Test Game", description="This is a test game.")
        self.assertEqual(game.name, "Test Game")
        self.assertEqual(game.description, "This is a test game.")
        self.assertTrue(game.is_active)

    def test_game_str_method(self):
        game = Game.objects.create(name="Another Game", description="Description")
        self.assertEqual(str(game), "Another Game")
