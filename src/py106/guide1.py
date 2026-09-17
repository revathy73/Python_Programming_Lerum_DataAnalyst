"""
You are given a variable called script, which represents a function that returns a collection of numbers; however, the function may also produce a FileNotFound exception.

Call the function to retrieve the numbers and transform them by multiplying each number by its position.

In case an exception is produced, return an empty collection.

Save your result in a variable called result

Example Solution 1
Assume that::
a) script() returns [1, 2, 3, 4]
Then
a) result is [0, 2, 6, 12]
Example Solution 2
Assume that::
b) script() produces a FileNotFound exception
Then
b) result is []
"""
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




