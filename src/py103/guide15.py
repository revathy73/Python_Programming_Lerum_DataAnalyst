"""
You are given the variables a and b, which represent integers.
Multiply all the odd numbers between a and b, inclusive.

Save your result in a variable called result

In the case that a is greater than or equal to b, set result to equal -1.

Example Solution
Assume that
a is 1
b is 5
Then
result is 15
"""

from to_do import TODO


def guide15(a: int, b: int) -> int:

    if a >= b:
        return -1

    result = 1
    for number in range(a, b + 1):
        if number % 2 != 0:
            result *= number

    return result

if __name__ == "__main__":

    # a=1, b=6
    print(guide15(a=1,b=6))

    # a=7, b=2
    print(guide15(a=7, b=2))

    #a= 7, b=7
    print(guide15(a=7, b=7))

    # a= 2, b= 9
    print(guide15(a=2, b=9))