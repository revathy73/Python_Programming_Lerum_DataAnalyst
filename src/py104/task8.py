"""
You are given the variable items. Identify the three elements with the highest value.

Save your result in a variable called result.

Example Solution
Assume that
items is [60, 9, 7, 10]
Then
result is [9, 10, 60]
Notes
Assume that items will always have at least 3 elements.
Do not use the built-in function max().
Do not use the built-in function takeLast().
Do not use the built-in function take().
Do not use the built-in function subList().
result cannot have repeated items.
result must have the elements organized in ascending order.
"""

from to_do import TODO


def task8(items: list[int]) -> list[int]:

    unique_values = list(set(items))
    sorted_list = sorted(unique_values)

    if len(sorted_list) >= 3:
        last_index = len(sorted_list) - 1

        third_item = sorted_list[last_index]
        second_item = sorted_list[last_index - 1]
        first_item = sorted_list[last_index - 2]
        result = [first_item, second_item, third_item]
    else:
        result = sorted_list

    return result

    """
    result = []
    highest_value = items[0]
    while len(result) < 3:
        for index,item in enumerate(items):
            if item > highest_value:
                value = item
                if index[0] 
                result.append(highest_value)
                items.remove(item)
            item += 1

    return result
    """


if __name__ == "__main__":

    # items = [60, 9, 70, 10] ---> [10, 60, 70]
    print(task8(items = [60, 9, 70, 10]))
