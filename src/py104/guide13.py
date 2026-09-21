"""
You are given the variables a and b. Each represents a word.

Create a collection containing the letters that are present in both given
words.

Example Solution
Assume that
a is "Panama"
b is "Sweden"
Then
result is [n]
Notes
Your solution must be case-sensitive
"""

from to_do import TODO


def guide13(a: str, b: str) -> list[str]:
    """
      # solution 1: for loop no ternary operator
    result = []

    for letter in a:
        if letter in b:
            result.append(letter)

    return result

    # solution 2: List comprehension
    result = [letter for letter in a if letter in b]
    return  result
    """
    # solution 2: List comprehension(refactoring)
    return [letter for letter in a if letter in b]

if __name__ == "__main__":

    # a= "Panama", b ="Sweden"  ---> ['n']
    print(guide13(a= "Panama", b ="Sweden"))

    # a= "PANAMA", b ="Sweden" ---> ['n']
    print(guide13(a="PANAMA", b="Sweden"))




