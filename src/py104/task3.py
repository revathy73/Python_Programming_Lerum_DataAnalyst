"""
You are given the variable items. Identify all the elements that appear
more than once.

Save the repeated elements in a variable called result.

Example Solution
Assume that
items is [1, 1, 1, 2, 2, 3]
Then
result is [1, 2]
Notes
result cannot contain repeated elements.
At least one of your solutions must use a loop
"""

from to_do import TODO


def task3(items: list[int]) -> list[int]:
    result = []
    for item in items:
        number_counter = items.count(item)
        if number_counter > 1 and item not in result:
            result.append(item)

    return result

if __name__ == "__main__":

    # items = [1, 1, 1, 2, 2, 3]
    print(task3(items = [1, 1, 1, 2, 2, 3]))
