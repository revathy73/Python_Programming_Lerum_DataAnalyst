"""
You are given the variable number. Find the reversed version of the number.

Save your result in a variable called result.

Example Solution #1
Assume that
number is 678
Then
result is 876
Example Solution #2
Assume that
number is 1
Then
result is 1
Notes
Assume number will always be a positive integer.

Assume number will always be an integer not divisible by 10.

You must use loops to find the solution.
"""

from to_do import TODO


def task6(number: int) -> int:

    """
    rev_num = int(str(number)[::-1])
    return rev_num
    """
    result = 0
    while number > 0:
        digit = number % 10
        result = result * 10 + digit
        number //= 10
    
    return result

if __name__ == "__main__":

    # number = 678
    print(task6(number=678))

    # number = 100026
    #print(task6(number=100026))

