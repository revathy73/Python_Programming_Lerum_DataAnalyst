"""
You are given the variable items, which represents a collection of numbers.

Remove all the numbers that are not multiples of 10

Example Solution
Assume that
items is [1, 5, 10, 60, 77, 71, 80, 9]
Then
result is [10, 60, 80]
"""

from to_do import TODO


def guide9(items: list[int]) -> list[int]:
    """
    # solution 1: for loop no ternary operator
    result = []
    for number in items:
        if number % 10 == 0:
            result.append(number)

    return result


    # solution 2: list comprehension
    result = [number for number in items if number % 10 == 0]
    return result

    """
    # solution 2: filtering a list
    result = filter(lambda number: number % 10 == 0 ,items)
    return list(result)



if __name__ == "__main__":

    # items = [2, 3, 5, 10, 45, 60, 71]
    print(guide9(items = [2, 3, 5, 10, 45, 60, 71]))

    # items = [4, 8, 16, 5, 45, 62, 71]
    print(guide9(items = [4, 8, 16, 5, 45, 62, 71]))


