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

    # solution 2: for loop (ternary operator)
    if not items:
        return []

    result = []
    for index,item in enumerate(items):
        value_to_transform =items[index] * items[index] if items[index] == items[0] else items[index] * items[index - 1]
        result.append(value_to_transform)

    return result
    """
    # solution 3: list comprehension
    result = [items[index] * items[index] if items[index] == items[0] else items[index] * items[index - 1] for index,item in enumerate(items)]
    return result
     """

if __name__ == "__main__":

    # items = [5, 2, 3, 4] --- > [25, 10, 6, 12]
    print(task9(items = [5, 2, 3, 4]))

    # items = [6, 1, 8, 10] --- > [36, 6, 8, 80]
    print(task9(items=[6, 1, 8, 10]))