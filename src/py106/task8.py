from to_do import TODO


def task8(items: list[str]) -> list[str]:

    result = []
    for item in items:
        if item is not None and len(item) > 3:
            result.append(item)


    return result


if __name__ == "__main__":

    # items = ["Hello", "Hej", "Gothenburg", null]
    print(task8(items = ["Hello", "Hej", "Gothenburg", None]))