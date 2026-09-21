"""
You are given the variable items. Multiply each element by its index.

Save your result in a variable called result.

Example Solution
Assume that
items is [1, 5, 11]
Then
result is [0, 5, 22]
Notes
At least one of your solutions must use a loop
"""

from operator import index

from to_do import TODO


def task5(items: list[int]) -> list[int]:
    """
    result = []
    for index,item in enumerate(items):
        value = item * index
        result.append(value)
        #result.append(item * index)

    return result

    # solution: list comprehension
    result = list[item * index for index,item in enumerate(items)]
    return  result
    """
    # solution 4: transform a list
    result = map(lambda value: value[0] * value[1], enumerate(items))
    return list(result)

if __name__ == "__main__":
    # items = [1, 5, 11] ---> [0, 5, 22]
    print(task5(items = [1, 5, 11]))