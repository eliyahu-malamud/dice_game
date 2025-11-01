import utils


def tie_breaker(roller) -> int:
    while True:
        roll1 = roller()
        roll2 = roller()
        sum1 = sum(roll1)
        sum2 = sum(roll2)
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return 2

def create_game_dict() -> dict:
    return {'player1': 0, 'player2': 0}

def play_round(main_player, other_player, game_dict) -> int | None:
         print(f'is {main_player} turn!')
         print(f'your score is: {game_dict[main_player]}! your enemy score is {game_dict[other_player]}!')
         decision = utils.turn_decision(input)
         if decision == 'r':
             result = utils.roll_two_d6()
             sum_all = sum(result)
             game_dict[main_player] += sum_all
             print(f'the result is {result}. sum: {sum_all}. your score now is: {game_dict[main_player]}')
             return None
         else:
             return 1


def main_game_loop():
    game_dict = create_game_dict()
    flag1 = 0
    flag2 = 0
    while True:
        if flag1 % 2 == 0:
            a = play_round('player1', 'player2', game_dict)
            if utils.is_bust(game_dict['player1']):
                return print('player2 wind because of bust!')
            elif utils.is_exact_100(game_dict['player1']):
                return print('player1 wind because of exact 100!')
            flag1 += 1
        else:
            a = play_round('player2', 'player1', game_dict)
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
                return 's'

def secondary_game():
    if tie_breaker(utils.roll_two_d6) == 1:
        print('player1 wind because tie breaker!')
        return None
    else:
        print('player2 wind because tie breaker!')
        return None