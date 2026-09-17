"""
You are given a variable called script, which represents a function that returns a non-empty collection of ages; however, the function may also produce an exception.

Call the function to retrieve the ages and filter it to only include the ages that are 18 and above.

In case an exception of type InvalidAge is produced, then set [0, 0, 0] as the result.

In case an exception of type MissingAge is produced, then set [1, 1, 1] as the result.

Save your result in a variable called result

Example Solution 1::
Assume that
script() returns [10, 45, 17, 18, 20, 21]
Then
result is [45, 18, 20, 21]
Example Solution 2::
Assume that
script() produces an InvalidAge exception
Then
result is [0, 0, 0]
Notes
Assume the collection is never empty.
"""
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




