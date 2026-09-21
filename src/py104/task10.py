"""
You are given the variable items. For each element in items that has an
even value, multiply it by 2 and for every element with an odd value,
multiply it by 3.

Save your result in a variable called result.

Example Solution
Assume that
items is [1, 2, 3, 4, 5]
Then
result is [3, 4, 9, 8, 15]
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO


def task10(items: list[int]) -> list[int]:
    """
    result = []
    for item in items:
        if item % 2 != 0:
           result.append(item * 3)
        else:
            result.append(item * 2)

    return result

    # solution 2: for loop (ternary operator)
    result = []
    for item in items:
        value = item * 3 if item % 2 != 0 else item * 2
        result.append(value)
    return  result

    # solution 3: list comprehension
    result = [item * 3 if item % 2 != 0 else item * 2 for item in items]
    return result

    # solution 4: transform a list
    result = map(lambda item: item * 3 if item % 2 != 0 else item * 2, items)
    return list(result)
    """
    # solution 4: transform a list
    return list(map(lambda item: item * 3 if item % 2 != 0 else item * 2, items))


if __name__ == "__main__":

    # items =  [1, 2, 3, 4, 5]  --- > [3, 4, 9, 8, 15]
    print(task10(items = [1, 2, 3, 4, 5]))
