"""
You are given a variable called script, which represents a function that returns a non-empty collection of names; however, the function may also produce a ZeroDivision exception.

Call the function to retrieve the names and determine which name is the longest one.

In case an exception is produced, return an empty string.

Save your result in a variable called result

Example Solution 1::
Assume that
script() returns
["Jane", "John", "Humberto"]
Then
result is "Humberto"
Example Solution 2::
Assume that
script() produces a ZeroDivision exception
Then
result is ""
Notes
Assume the collection is never empty.
"""
from typing import Callable

from to_do import TODO


def guide2(script: Callable[[], list[str]]) -> str:

    try:
        names = script()
        result = ""

        for name in names:
            if len(name) > len(result):
                result = name

        return  result

    except ZeroDivisionError:
        return ""