"""
You are given the variable number. Use it to calculate the factorial of the
number.

Save your result in a variable called result.

Example Solution
Assume that
number is 5
Then
result is 120
Hint
Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120
"""

from to_do import TODO


def task3(number: int) -> int:

    result = 1
    for integer in range(1, number+1):
        result *= integer

    return result


if __name__ == "__main__":

    # number = 3
    print(task3(number=3))

    # number = 6
    print(task3(number=6))


