from to_do import TODO


def guide10(items: list[str]) -> list[str]:
    """
    # solution 1: for loop
    result = []
    for index,item in enumerate(items):
        if index % 2 == 0:
            result.append(item.upper())
        else:
            result.append(item.lower())

    return result

    # solution 1: for loop (Ternary operator)
    result = []

    for index,item in enumerate(items):
        value = item.upper() if index % 2 == 0 else item.lower()
        result.append(value)

    return result

    # solution 2: list comprehension
    result = [item.upper() if index % 2 == 0 else item.lower() for index,item in enumerate(items)]
    return result

    # solution 2: list comprehension(refactoring)
    return [item.upper() if index % 2 == 0 else item.lower() for index,item in enumerate(items)]

    # solution 3: Transform a list

    transformed_list = map(
        lambda index_element: index_element[1].upper() if index_element[0] % 2 == 0 else index_element[1].lower(),
        enumerate(items)
    )
    return list(transformed_list)
    """

    # solution 3: Transform a list (Refactoring)

    return list(map(
        lambda index_element: index_element[1].upper() if index_element[0] % 2 == 0 else index_element[1].lower(),
        enumerate(items)
        ))

if __name__ == "__main__":

    # items = ["KOTLIN", "python", "Linero Tech", "jetbrains"]
    print(guide10(items = ["KOTLIN", "python", "Linero Tech", "jetbrains"]))

    # items = []
    print(guide10(items = []))
