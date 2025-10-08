from to_do import TODO


def guide11(items: list[int]) -> list[int]:
    """
    # solution 1: for loop
    result = []
    for number in items:
        if number % 11 == 0:
            result.append(number * 3)
        else:
            result.append(number)

    return result

    # solution 1: for loop (Ternary operator)
    result = []
    for number in items:
        value =number * 3 if number % 11 == 0 else number
        result.append(value)

    return  result

    # solution 2: list comprehension
    result = [number * 3 if number % 11 == 0 else number for number in items]
    return result
    # solution 2: list comprehension(refactoring)
    return [number * 3 if number % 11 == 0 else number for number in items]

    # solution 3: Transform a list

    transformed_list = map(lambda number: number * 3 if number % 11 == 0 else number ,items )
    return  list(transformed_list)
    """

    # solution 3: Transform a list (Refactoring)
    return list(map(lambda  number: number * 3 if number % 11 == 0 else number, items))

if __name__ == "__main__":

    # items = [99, 78, 66, 55, 9, 10]
    print(guide11(items = [99, 78, 66, 55, 9, 10, 6, 11, 55]))
