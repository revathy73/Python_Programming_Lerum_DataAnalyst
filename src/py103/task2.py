"""
You are given the variable number. Use it to determine if its value is a
prime number or not.

Save your result in a variable called result.

Example Solution
Assume that
number is 5
Then
result is true
Hint
A prime number is a positive integer greater than 1 with only two factors:
itself and one.

Examples of prime numbers: 2, 3, 5, 7, 11, 17, 19, 23
"""

from to_do import TODO


def task2(number: int) -> bool:

    if number <= 1:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True


    """
    result = False
    if number > 1:
        for integer in range(2, number+1):
            if number % integer == 0:
                if number == integer:
                    result = True
                else:
                    result = False

    return result
    """

if __name__ =="__main__":

    # number = 5
    print(task2(number = 5))

    # number = 6
    print(task2(number = 6))