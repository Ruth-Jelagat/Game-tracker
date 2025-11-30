import pytest
from classes.many_to_many import Player, Game, Result

class TestPlayer:

    def test_player_initialization(self):
        player = Player("Saaammmm")
        assert player.username == "Saaammmm"

    def test_username_is_mutable_string(self):
        player = Player("Saaammmm")
        player.username = "ActuallyTopher"
        assert player.username == "ActuallyTopher"

        with pytest.raises(ValueError):
            player.username = 2  # must be string
        with pytest.raises(ValueError):
            player.username = "y"  # too short

    def test_username_length(self):
        player = Player("Saaammmm")
        assert 2 <= len(player.username) <= 16

    def test_player_results_and_games(self):
        player = Player("Alice")
        game = Game("Skribbl.io")
        result = Result(player, game, 100)
        assert result in player.results
        assert game in player.games_played()
        assert all(isinstance(r, Result) for r in player.results)


