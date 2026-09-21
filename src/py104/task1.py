"""
You are given the variable items. Select a random element from it.

Save your result in a variable called result.

If items is empty, then set result to an empty string.
"""

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

