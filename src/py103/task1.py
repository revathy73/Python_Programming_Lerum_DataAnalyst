"""
You are given the variables a and b. Add the numbers between a and b,
inclusive.

Save your result in a variable called result.

If a >= b, then result is equal to 0
Example Solution #1
Assume that
a is 1
b is 5
Then
result is 15
Example Solution #2
Assume that
a is 3
b is 3
Then
result is 0
Notes
You must use loops to find the solution.
"""
from to_do import TODO


def task1(a: int, b: int) -> int:

    if a >= b:
       return 0

    result = 0
    for number in range(a, b+1):
        result += number

    return result

if __name__ == "__main__":

    # a = 1,  b = 1
    print(task1(a=1, b=1))

    # a = 1,  b = 5
    print(task1(a=1, b=5))

    # a= 2, b = 20
    print(task1(a=2, b=20))

