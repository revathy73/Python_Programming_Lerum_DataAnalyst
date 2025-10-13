from to_do import TODO


def task3(items: list[int]) -> list[int]:
    result = []
    for item in items:
        lowercase_letter_counter = items.count(item)
        if lowercase_letter_counter > 1 and item not in result:
            result.append(item)

    return result

if __name__ == "__main__":

    # items = [1, 1, 1, 2, 2, 3]
    print(task3(items = [1, 1, 1, 2, 2, 3]))
