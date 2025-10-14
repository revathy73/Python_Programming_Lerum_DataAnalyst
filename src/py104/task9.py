from to_do import TODO


def task9(items: list[int]) -> list[int]:
    if len(items) == []:
        return []

    result = []
    for index,item in enumerate(items):
        if items[index] == items[0]:
            result.append(items[index] * items[index])

        else:
            result.append(items[index] * items[index - 1])

    return result

if __name__ == "__main__":

    # items = [5, 2, 3, 4] --- > [25, 10, 6, 12]
    print(task9(items = [5, 2, 3, 4]))

    # items = [6, 1, 8, 10] --- > [36, 6, 8, 80]
    print(task9(items=[6, 1, 8, 10]))