from to_do import TODO


def guide19(a: int, b: int) -> tuple[int]:
    """
    # solution 1: for loop
    result = []
    for integer in range(a, b + 1):
        if integer % 2 != 0 and integer % 3 == 0:
            result.append(integer)

    return tuple(result)

    # solution 1: tuple comprehension
    result = tuple((integer for integer in range(a, b + 1) if integer % 2 != 0 and integer % 3 == 0))
    return  result
    """
    return tuple((integer for integer in range(a, b + 1) if integer % 2 != 0 and integer % 3 == 0))

if __name__ == "__main__":

    # a = 6, b = 18
    print(guide19(a = 6, b = 18))