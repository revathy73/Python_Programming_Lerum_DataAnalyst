"""
You are given the variable items. Find the element with the smallest value.

Save your result in a variable called result.

If items is empty, then set result to 0.
Example Solution
Assume that
items is [10, 5, 11]
Then
result is 5
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO


def task7(items: list[int]) -> int:

    if not items:
        return 0

    result = items[0]
    for item in items:
        if item < result:
            result = item

    return result

if __name__ == "__main__":

    # items=[10, 2, 5]
    print(task7(items=[10, 2, 5]))