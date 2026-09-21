"""
You are given the variables a and b, which represent numbers.

Create a collection that contains all the numbers between a and b, but not
including a and b.

The following conditions need to be satisfied:

The numbers that are odd and divisible by 5 must be multiplied by 3
The numbers that are even and divisible by 5 must be multiplied by 5
All other numbers just need to be added to the list
Set result to be an empty list in the scenario that b is smaller than a

Example Solution
Assume that
a is 5
b is 16
Then
result is
[6, 7, 8, 9, 50, 11, 12, 13, 14, 45]
"""

from to_do import TODO


def guide12(a: int, b: int) -> list[int]:

    if a > b:
        result = []

    result = []
    for integer in range(a, b):
        if integer == a:  # we can give instead of this statement (a+1)
            continue
        elif integer % 2 != 0 and integer % 5 == 0:
            result.append(integer * 3)
        elif integer % 2 == 0 and integer % 5 == 0:
            result.append(integer * 5)
        else:
            result.append(integer)

    return result

if __name__ == "__main__":

    # a= 3, b= 10 ---> [4, 15, 6, 7, 8, 9]
    print(guide12(a= 3, b= 10))

    # a= 12, b= 2 ---> []
    print(guide12(a=12, b=2))

    # a= 12, b= 12 ---> []
    print(guide12(a=12, b=12))




