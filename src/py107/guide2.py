"""
Create a function called exponential which raises all even numbers
between 20 and 40 to the third power,
adds the results together, and prints the result.
"""
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

