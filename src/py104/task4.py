from to_do import TODO


def task4(items: list[int], factor: int) -> list[int]:
    result = []
    for item in items:
        if item % factor == 0 and item not in result:
            result.append(item)


    return result
if __name__ == "__main__":

    # items = [1, 2, 4, 5, 6], factor = 2
    print(task4(items = [1, 2, 4, 5, 6], factor = 2))

    # items = [25, 15, 25, 15, 30], factor = 5
    print(task4(items=[25, 15, 25, 15, 30], factor=5))