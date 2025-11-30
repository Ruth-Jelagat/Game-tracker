import pytest
from lib.classes.many_to_many import Game, Player, Result

class TestGame:

    def test_game_initialization(self):
        game = Game("Skribbl.io")
        assert game.title == "Skribbl.io"

    def test_title_is_immutable_string(self):
        game = Game("Skribbl.io")
        with pytest.raises(AttributeError):
            game.title = "New Title"

    def test_title_length(self):
        game = Game("Skribbl.io")
        assert len(game.title) > 0

    def test_has_many_results(self):
        game = Game("Skribbl.io")
        player = Player("Saaammmm")
        Result(player, game, 2000)
        Result(player, game, 3500)
        assert len(game.results()) == 2

    def test_results_of_type_result(self):
        game = Game("Skribbl.io")
        player = Player("Saaammmm")
        Result(player, game, 2000)
        Result(player, game, 3500)
        assert isinstance(game.results()[0], Result)

    def test_has_many_players(self):
        game = Game("Skribbl.io")
        player1 = Player("Nick")
        player2 = Player("Ari")
        Result(player1, game, 5000)
        Result(player2, game, 4999)
        assert player1 in game.players()
        assert isinstance(game.players()[0], Player)

    def test_has_unique_players(self):
        game = Game("Skribbl.io")
        player1 = Player("Nick")
        player2 = Player("Ari")
        Result(player1, game, 5000)
        Result(player2, game, 5000)
        players = game.players()
        assert len(players) == len(set(players))

    def test_average_score(self):
        game = Game("Skribbl.io")
        player = Player("Nick")
        Result(player, game, 5000)
        Result(player, game, 4999)
        assert game.average_score(player) == 4999.5


