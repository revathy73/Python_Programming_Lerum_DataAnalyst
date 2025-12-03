def multiplication():
    """
    # solution 1: using for loop and no step
    result = 1
    for number in range(1, 10):
        if number % 2 != 0:
            result *= number

    print(result)
    """
    # solution 1: using for loop and step
    result = 1
    for number in range(1, 10, 2):
        result *= number

    print(result)
