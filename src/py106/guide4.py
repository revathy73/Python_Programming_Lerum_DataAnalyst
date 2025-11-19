from typing import Callable

from linero_tech_errors import InvalidAgeError, MissingAgeError
from to_do import TODO


def guide4(script: Callable[[], list[int]]) -> list[int]:
    """
    Use the code `from linero_tech_errors import InvalidAgeError, MissingAgeError`
    to import the necessary errors
    """
    """
    try:
        ages = script()
        result = []

        for age in ages:
            if age >= 18:
                result.append(age)

        return result
    except InvalidAgeError:
        return [0, 0, 0]
    except MissingAgeError:
        return [1, 1, 1]

    # solution 2:
    try:
        ages = script()
        result = [age for age in ages if age > 17]
        return result
        # return [age for age in script() if age > 17]
    except InvalidAgeError:
        return [0, 0, 0]
    except MissingAgeError:
        return [1, 1, 1]
    """
    # Solution 3:
    try:
        ages = script()
        return list(filter(lambda age: age > 17,ages))
        # return list(filter(lambda age: age > 17,script()))
    except InvalidAgeError:
        return [0, 0, 0]
    except MissingAgeError:
        return [1, 1, 1]




