"""
Create a function called summation in which the user can provide an arbitrary
amount of numbers.

The function shall then output the sum of all the given numbers.
"""
def summation(*numbers):
    # solution 1
    """
    result = 0
    for number in numbers:
        result += number

    return result
    """
    # solution 2:
    return sum(numbers)

if __name__ == "__main__":

    print(summation(0))
    print(summation(0, 1))
    print(summation(0, 1, 2))


