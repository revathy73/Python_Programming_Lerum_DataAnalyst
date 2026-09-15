"""
Create a function called baldor that returns the sum of all the odd numbers
between 1 and 1111, inclusive.
"""
def baldor():

    result = 0
    for number in range(1, 1112, 2):
        result += number

    return result
