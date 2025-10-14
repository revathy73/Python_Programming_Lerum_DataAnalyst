from to_do import TODO


def task8(items: list[int]) -> list[int]:

    result = []
    value = items[0]

    for index,item in enumerate(items):
        if item > value:
            value = item
            result.append(value)
            items.remove(item)
            while value

    return result

    """                                     
    result = []
    value = items[0]
    for index,item in enumerate(items):
        if value > item:
           result.append(value)
           value = item
           items.remove(value)
        elif items[1] > items[index]:
            result.append(items[1])
        elif items[2] > items[index]:
            result.append(items[2])
        else:
            result.append(items[3])

    return result
    """


if __name__ == "__main__":

    # items = [60, 9, 7, 10]
    print(task8(items = [60, 9, 70, 10]))
