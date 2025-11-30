# lib/classes/many_to_many.py

from typing import List

class Game:
    def __init__(self, title: str):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = title
        self._results: List[Result] = []

    @property
    def title(self):
        return self._title

    def results(self) -> List['Result']:
        return [res for res in Result.all if res.game == self]

    def players(self) -> List['Player']:
        # unique players from results
        players = [res.player for res in self.results()]
        return list(set(players))

    def average_score(self, player: 'Player') -> float:
        player_results = [res.score for res in self.results() if res.player == player]
        if not player_results:
            return 0.0
        return sum(player_results) / len(player_results)


class Player:
    def __init__(self, username: str):
        self._username = None
        self.username = username  # validation via setter

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_name: str):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Username must be a string between 2 and 16 chars")
        self._username = new_name

    def results(self) -> List['Result']:
        return [res for res in Result.all if res.player == self]

    def games_played(self) -> List['Game']:
        return list({res.game for res in self.results()})

    def played_game(self, game: 'Game') -> bool:
        return game in self.games_played()

    def num_times_played(self, game: 'Game') -> int:
        return sum(1 for res in self.results() if res.game == game)


class Result:
    all: List['Result'] = []

    def __init__(self, player: Player, game: Game, score: int):
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be int between 1 and 5000")
        self._score = score
        self.player = player
        self.game = game
        Result.all.append(self)

    @property
    def score(self):
        return self._score



