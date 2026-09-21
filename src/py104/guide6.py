"""
You are given the variable items, which represents a collection of numbers.

Create a new collection that only contains the elements in items that are divisible by 5 and greater than 10.

Save your result in a variable called result

Example Solution
Assume that
items is [5, 6, 7, 8, 10, 15, 25, 5, 25]
Then
result is [15, 25, 25]
"""

from to_do import TODO


def guide6(items: list[int]) -> list[int]:

    result = []
    for number in items:
        if number % 5 == 0 and number > 10:
            result.append(number)

    return result

    # solution : List comprehension
    # result = [number for number in items if number % 5 == 0 and number > 10]
    # return result

if __name__ == "__main__":

    # items = [5, 10, 15, 20, 25, 30]
    print(guide6(items=[5,11,12, 10, 15, 20, 25,26,28, 30]))

    print(guide6(items = []))
