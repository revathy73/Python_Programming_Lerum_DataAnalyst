"""
You are given the variable number. Add all of its digits.

Save your result in a variable called result.

Example Solution
Assume that
number is 123
Then
result is 6
Hint
123 = 1 + 2 + 3 = 6
"""
from to_do import TODO


def task8(number: int) -> int:

    result = 0
    while number > 0:
        add_digit = number % 10
        result += add_digit
        number //= 10

    return result

if __name__ == "__main__":

    # number = 234
    print(task8(number=234))

    # number = 4512
    print(task8(number=4512))



