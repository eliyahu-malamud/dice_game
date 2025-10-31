import random
def roll_two_d6() -> tuple[int, int]:
    return random.randint(1, 6), random.randint(1, 6)

def is_bust(score: int) -> bool:
    if score > 100:
        return True
    else:
        return False

def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    else:
        return False

def closer_to_target(a: int, b: int, target: int = 100) -> int |None:
    if a > b:
        return 1
    elif a < b:
        return 2
    else:
        return None

def turn_decision(input_fn) -> str:
    while True:
        decision = input_fn("Enter 'p' to pass or 'r' to roll:")
        if decision == 'r' or decision == 'p':
            return decision
        else:
            print("Invalid input. Please enter p or r.")


