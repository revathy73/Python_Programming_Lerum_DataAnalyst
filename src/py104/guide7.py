from to_do import TODO


def guide7(items: list[int]) -> list[int]:
    # solution in for loop
    """
    result = []
    for index,item in enumerate(items):
        result.append(item * index)

    return result
    """
    # solution in list comprehension
    result = [item * index for index,item in enumerate(items)]
    return result
    
    """
    # solution in list comprehension (Refactoring)
    return [index * item for index,item in enumerate(items)]
    """

if __name__ == "__main__":

    # items = [1, 3, 5, 7]
    print(guide7(items = [1, 3, 5, 7]))

    # items = []
    print(guide7(items = []))

