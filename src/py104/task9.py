"""
You are given the variable items. Create a new list by multiplying each
element of items by the previous element. For the element at index 0,
multiply it by itself.

Save your result in a variable called result.

If items is an empty list, then set result to be an empty list.

Example Solution
Assume that
items is [5, 2, 3, 4]
Then
result is [25, 10, 6, 12]
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO


def task9(items: list[int]) -> list[int]:

    if not items:  # if len(items) == []:
        return []

    result = []
    for index,item in enumerate(items):
        if index == 0:
            result.append(item * item)
        else:
            result.append(item * items[index - 1])
    return result

    """
    # solution 2: for loop (ternary operator)
    if not items:
        return []

    result = []
    for index,item in enumerate(items):
        value_to_transform =items[index] * items[index] if items[index] == items[0] else items[index] * items[index - 1]
        result.append(value_to_transform)

    return result

    # solution 3: list comprehension
    result = [items[index] * items[index] if items[index] == items[0] else items[index] * items[index - 1] for index,item in enumerate(items)]
    return result
    """

if __name__ == "__main__":

    # items = [5, 2, 3, 4] --- > [25, 10, 6, 12]
    print(task9(items = [5, 2, 3, 4]))

    # items = [6, 1, 8, 10] --- > [36, 6, 8, 80]
    print(task9(items=[6, 1, 8, 10]))