from classes.many_to_many import Game, Player, Result

def debug_game_tracker():
    # Create Games
    game1 = Game("Skribbl.io")
    game2 = Game("Codenames")

    # Create Players
    player1 = Player("Nick")
    player2 = Player("Ari")

    # Create Results
    Result(player1, game1, 5000)
    Result(player2, game1, 4999)
    Result(player1, game2, 10)

    # Debug outputs
    print("Game1 Results:", [r.score for r in game1.results()])
    print("Game1 Players:", [p.username for p in game1.players()])
    print("Player1 average in Game1:", game1.average_score(player1))
    print("Player1 Results:", [r.score for r in player1.results()])
    print("Player1 Games Played:", [g.title for g in player1.games_played()])
    print("Has Player1 played Game2?", player1.played_game(game2))
    print("How many times Player1 played Game1?", player1.num_times_played(game1))

    # Try to change immutable attributes
    try:
        game1.title = "New Title"
    except AttributeError as e:
        print("Cannot change game title:", e)

    try:
        player1.username = 123
    except ValueError as e:
        print("Cannot change username:", e)

    # Highest scored player
    highest = Player.highest_scored(game1)
    print("Highest scored player in Game1:", highest.username if highest else None)

if __name__ == "__main__":
    debug_game_tracker()
