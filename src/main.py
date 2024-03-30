from SnakeGame import SnakeGame

if __name__ == "__main__":
    game = SnakeGame()

    while True:
        game_over, score = game.play_game()

        if game_over:
            break
