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
