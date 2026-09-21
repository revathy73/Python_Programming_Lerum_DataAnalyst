"""
You are given the values a and b, which represent integers. Calculate the
sum of all the even numbers between a and b, inclusive.

Save your result in a variable called result

In the case that a is greater than or equal to b, set result to equal -1.

Example Solution
Assume that
a is 1
b is 5
Then
result is 6
"""

from to_do import TODO


def guide14(a: int, b: int) -> int:

    if a >= b:
        return -1

    result = 0
    for number in range(a, b + 1):
        if number % 2 == 0:
        #    result = result + number
             result += number

    return result

if __name__ == "__main__":

    # a=1, b=6
    print(guide14(a=1,b=6))

    # a=1, b=5
    print(guide14(a=1, b=5))

    # a=7, b=3
    print(guide14(a=7, b=5))

    # a=5, b=5
    print(guide14(a=5, b=5))



