import pytest
from classes.many_to_many import Game, Player, Result

class TestGame:

    def test_game_initialization(self):
        game = Game("Skribbl.io")
        assert game.title == "Skribbl.io"

    def test_title_is_immutable_string(self):
        game = Game("Skribbl.io")
        assert isinstance(game.title, str)
        with pytest.raises(AttributeError):
            game.title = "New Title"

    def test_title_length(self):
        game = Game("Skribbl.io")
        assert len(game.title) > 0

    def test_game_has_results(self):
        game = Game("Skribbl.io")
        player = Player("Alice")
        res = Result(player, game, 100)
        assert res in game.results

    def test_game_players_are_unique(self):
        game = Game("Skribbl.io")
        player1 = Player("Nick")
        player2 = Player("Ari")
        Result(player1, game, 5000)
        Result(player2, game, 5000)
        players = game.players()
        assert len(players) == len(set(players))

    def test_game_average_score(self):
        game = Game("Skribbl.io")
        player = Player("Alice")
        Result(player, game, 100)
        Result(player, game, 200)
        avg = game.player_average(player)
        assert avg == 150


