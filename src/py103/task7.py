"""
You are given the variables a and b. Find the result of raising a to the
power of b using loops.

Save your result in a variable called result

If a and b are 0, then result is equal to 1.
Example Solution
Assume that
a is 2
b is 3
Then
result is 8
Notes
You must use loops to find the solution.
"""
from to_do import TODO


def task7(a: int, b: int) -> int:

    if a and b == 0:
        return 1

    result = 1
    for integer in range(1, b+1):  #for integer in range(b):
        result = result * a

    return result


if __name__ == "__main__":

    # a=2 , b= 3
    print(task7(a=2, b=3))

    # a=3 , b= 5
    print(task7(a=3, b=5))

    # a=1 , b= 1
    print(task7(a=1, b=1))




