"""
You are given a list called items. Use it to count the number of elements
that are null.

Save your result in a variable called result.

Assign a value of 0 to result if items is null.
Example Solution
Assume that
items is [1, null, 2, null, 3]
Then
result is 2
"""
from to_do import TODO


def task2(items: list[int]) -> int:

    if items is None:
        return  0

    result = 0
    for number in items:
        if number is None:
            result += 1

    return result


if __name__ == "__main__":

    # items  = [1, null, 2, null, 3]
    print(task2(items  = [1, None, 2, None, 3]))
