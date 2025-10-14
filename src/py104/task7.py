from to_do import TODO


def task7(items: list[int]) -> int:

    if not items:
        return 0

    result = items[0]
    for item in items:
        if item < result:
            result = item

    return result

if __name__ == "__main__":

    # items=[10, 2, 5]
    print(task7(items=[10, 2, 5]))