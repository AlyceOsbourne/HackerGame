import random

from decorators import logger_decorator


@logger_decorator
def roll_dice(sides):
    return random.choice(range(1, sides + 1))


@logger_decorator
def roll_dice_generator(sides, rolls: int = 1):
    for i in range(rolls):
        yield roll_dice(sides)
