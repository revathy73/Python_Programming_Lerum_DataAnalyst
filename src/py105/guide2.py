"""
Create a map called result in which the keys are all the letters of the
alphabet in lowercase.

For the letters located at even positions, its value is the same letter
written in uppercase.

For the letters located at odd positions, its value is the same letter but
written twice.

Example Solution
Assume that
a is at position 0
Then
result is
{
    "a" to "A",
    "b" to "bb",
    "c" to "C",
    ...
}
"""
import string
from operator import index

from to_do import TODO


def guide2() -> dict[str, str]:

    """
    # solution 1:
    alphabet = string.ascii_lowercase
    result = {}
    for index,letter in enumerate(alphabet):
        if index % 2 == 0:
            result[letter] = letter.upper()
        else:
            result[letter] = letter + letter

    return result

    # solution 2: (Ternary operator)
    alphabet = string.ascii_lowercase

    result = {}
    for index,letter in enumerate(alphabet):
        result[letter] = letter.upper() if index % 2 == 0 else letter * 2

    return result

    # solution 3: (dictionary comprehension)
    alphabet = string.ascii_lowercase
    result = {}
    result = {letter: letter.upper() if index % 2 == 0 else letter + letter for index, letter in enumerate(alphabet)}
    return result
    """

    # solution 3: (dictionary comprehension -- Refactoring)
    alphabet = string.ascii_lowercase

    result = {}
    return {letter : letter.upper() if index % 2 == 0 else letter * 2 for index,letter in enumerate(alphabet)}


if __name__ == "__main__":

    print(guide2())




