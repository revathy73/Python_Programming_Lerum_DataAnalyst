"""
You are given the variables items and factor. Identify all the elements
in items which are multiples of factor.

Save your result in a variable called result.

Example Solution
Assume that
items is [1, 2, 4, 5, 6]
factor is 2
Then
result is [2, 4, 6]
Notes
result cannot contain repeated elements.
At least one of your solutions must use a loop
"""

from to_do import TODO


def task4(items: list[int], factor: int) -> list[int]:
    result = []
    for item in items:
        if item % factor == 0 and item not in result:
            result.append(item)

    return result

if __name__ == "__main__":
    # items = [1, 2, 4, 5, 6], factor = 2
    print(task4(items = [1, 2, 4, 5, 6], factor = 2))

    # items = [25, 15, 25, 15, 30], factor = 5
    print(task4(items=[25, 15, 25, 15, 30], factor=5))