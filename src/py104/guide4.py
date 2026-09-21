"""
You are given the variables a and b.

Create a collection that contains all the odd numbers between a and b, inclusive. Additionally, for every odd number that is divisible by 5, raise it to the second power before adding it to the list.

In the case that a is greater than or equal to b, set result to be an empty collection.

Save your result in a variable called result

Example Solution
Assume that
a is 5
b is 10
Then
result is [25, 7, 9]
Notes
Do not use any built-in function, like indexOf(), to solve the problem.
"""

from to_do import TODO


def guide4(a: int, b: int) -> list[int]:

    if a >= b:
        return []

    result = []
    for number in range(a, b + 1):
        if number % 2 != 0 and number % 5 == 0:
            value = number ** 2
            result.append(value)
        elif number % 2 != 0:
            result.append(number)

    return result

if __name__ == "__main__":

    # a = 5, b = 10
    print(guide4(a = 5, b = 10))

    # a = 10, b = 5
    print(guide4(a=10, b=5))




