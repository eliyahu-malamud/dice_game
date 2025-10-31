import game, utils
def play_game():
        game_dict = game.create_game_dict()
        flag1 = 0
        flag2 = 0
        while True:
            if flag1 % 2 == 0:
                a = game.play_round('player1', 'player2', game_dict)
                if utils.is_bust(game_dict['player1']):
                    return print('player2 wind because of bust!')
                elif utils.is_exact_100(game_dict['player1']):
                    return print('player1 wind because of exact 100!')
                flag1 += 1
            else:
                a = game.play_round('player2', 'player1', game_dict)
                if utils.is_bust(game_dict['player2']):
                    return print('player1 wind because of bust!')
                elif utils.is_exact_100(game_dict['player2']):
                    return print('player2 wind because of exact 100!')
                flag1 += 1
            if a == 1:
                flag2 += 1
            elif a != 1:
                flag2 = 0
            if flag2 == 2:
                if utils.closer_to_target(game_dict['player1'], game_dict['player2']) == 1:
                    print('player1 wind because he is closer to 100')
                    return None
                elif utils.closer_to_target(game_dict['player1'], game_dict['player2']) == 2:
                    print('player2 wind because he is closer to 100')
                    return None
                else:
                    print('hello')
                    if game.tie_breaker(utils.roll_two_d6) == 1:
                        print('player1 wind because tie breaker!')
                        return None
                    elif game.tie_breaker(utils.roll_two_d6) == 2:
                        print('player2 wind because tie breaker!')
                        return None



play_game()





