import pytest
from lib.classes.many_to_many import Game, Player, Result

class TestPlayer:

    def test_player_initialization(self):
        player = Player("Saaammmm")
        assert player.username == "Saaammmm"

    def test_username_is_mutable_string(self):
        player = Player("Saaammmm")
        player.username = "ActuallyTopher"
        assert player.username == "ActuallyTopher"
        with pytest.raises(ValueError):
            player.username = 2

    def test_username_length(self):
        player = Player("Saaammmm")
        with pytest.raises(ValueError):
            player.username = "y"
        assert 2 <= len(player.username) <= 16

    def test_has_many_results(self):
        player = Player("Saaammmm")
        game = Game("Skribbl.io")
        Result(player, game, 2000)
        Result(player, game, 3500)
        assert len(player.results()) == 2
        assert isinstance(player.results()[0], Result)

    def test_has_many_games(self):
        player = Player("Nick")
        game1 = Game("Skribbl.io")
        game2 = Game("Codenames")
        Result(player, game1, 5000)
        Result(player, game2, 10)
        assert game1 in player.games_played()
        assert isinstance(player.games_played()[0], Game)

    def test_games_are_unique(self):
        player = Player("Nick")
        game1 = Game("Skribbl.io")
        game2 = Game("Codenames")
        Result(player, game1, 5000)
        Result(player, game2, 19)
        Result(player, game1, 100)
        assert len(set(player.games_played())) == len(player.games_played())

    def test_has_played_game(self):
        player = Player("Saaammmm")
        game = Game("Skribbl.io")
        Result(player, game, 2000)
        assert player.played_game(game) is True

    def test_num_times_played(self):
        player = Player("Saaammmm")
        game = Game("Skribbl.io")
        Result(player, game, 2000)
        Result(player, game, 1900)
        assert player.num_times_played(game) == 2

