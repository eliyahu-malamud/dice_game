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

