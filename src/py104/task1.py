import random

from to_do import TODO


def task1(items: list[str]) -> str:

    if len(items) == 0:
        return  ""

    first_index = 0
    last_index = len(items) - 1
    random_index = random.randint(first_index,last_index)
    #random_element = items[random_index]
    return items[random_index]

