import pytest
from classes.many_to_many import Player, Game, Result

class TestResults:

    def test_result_initialization(self):
        player = Player("Nick")
        game = Game("Skribbl.io")
        result = Result(player, game, 2000)
        assert result.score == 2000
        assert result.player == player
        assert result.game == game

    def test_score_is_immutable_int(self):
        player = Player("Nick")
        game = Game("Skribbl.io")
        result = Result(player, game, 2000)
        assert isinstance(result.score, int)

        with pytest.raises(AttributeError):
            result.score = 5000

    def test_score_bounds(self):
        player = Player("Nick")
        game = Game("Skribbl.io")
        with pytest.raises(ValueError):
            Result(player, game, 0)      # too low
        with pytest.raises(ValueError):
            Result(player, game, 5001)   # too high


