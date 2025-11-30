class GameResult:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

    def __repr__(self):
        return f"{self.winner.name} defeated {self.loser.name}"
