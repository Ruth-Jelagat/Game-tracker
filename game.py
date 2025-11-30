from player import Player
from result import GameResult
from debug import debug_log

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        debug_log(f"Created game between {player1_name} and {player2_name}")

    def play(self, winner_name):
        if winner_name == self.player1.name:
            winner = self.player1
            loser = self.player2
        elif winner_name == self.player2.name:
            winner = self.player2
            loser = self.player1
        else:
            raise ValueError("Winner must be one of the players")

        winner.score += 1
        debug_log(f"{winner.name} won the match")

        return GameResult(winner, loser)

    def get_scores(self):
        return {
            self.player1.name: self.player1.score,
            self.player2.name: self.player2.score
        }
