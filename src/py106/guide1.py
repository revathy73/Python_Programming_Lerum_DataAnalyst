from typing import Callable

from to_do import TODO


def guide1(script: Callable[[], list[int]]) -> list[int]:
    """
    # solution 1:
    try:

        #numbers = script()
        #result = [index * item for index, item in enumerate(numbers)]

        result = [index * item for index, item in enumerate(script())]
        return result
    except FileNotFoundError:
        return []
    """
    # solution 2:

    try:
        numbers = script()
        result = map(lambda item: item[0] * item[1],enumerate(numbers))
        return list(result)
    except FileNotFoundError:
        return []




