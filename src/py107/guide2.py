def exponential():

    """
    # solution 1: for loop with condition and no step
    result = 0
    for number in range(20, 41):
        if number % 2 == 0:
            result += number ** 3

    print(result)
    """
    # solution 1: for loop with condition and step
    result = 0
    for number in range(20, 41, 2):
        result += number ** 3

    print(result)

