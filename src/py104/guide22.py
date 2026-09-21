"""
You are given the variable a, which represents a number.

Create a collection containing the first ten numbers that are multiples
of a

Save your result in a variable called result

Assume that
a is 5
Then
result is
{5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
Notes
Do not use any built-in function
"""

from to_do import TODO


def guide22(a: int) -> set[int]:
    result = set()
    number = a

    while len(result) < 10:
        if number % a == 0:
            result.add(number)
        number += 1

    return result
if __name__ == "__main__":

    # a = 5 ---> {5,10,15,20,25,30,35,40,45,50}
    print(guide22( a = 5))
