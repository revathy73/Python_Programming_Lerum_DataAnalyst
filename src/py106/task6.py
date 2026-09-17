"""
You are given the variable items. Multiply each element by its index.

Save your result in a variable called result.

In the case that an element in items is null, assign a value of null in the
new list.
Set result to be an empty list if items is an empty list
Example Solution
Assume that
items is [1, 2, null]
Then
result is [0, 2, null]
"""
from to_do import TODO


def task6(items: list[int]) -> list[int]:

    if items is None or len(items) == 0:
        return []

    result = []
    for index,item in enumerate(items):
        if item is not None:
            result.append(index * item)
        else:
            result.append(None)

    return result

if __name__ == "__main__":

    # items = [1, 2, null]
    print(task6(items= [1, 2, None]))
