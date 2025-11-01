import game

def play_game():
    a = game.main_game_loop()
    if a == 's':
        game.secondary_game()

play_game()








