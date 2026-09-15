"""
Create a function called bonus which accepts a list of numbers and modifies
the original list so that all of its values are incremented by one.
"""
def bonus(numbers):
    for index, number in enumerate(numbers):
        numbers[index] = number + 1


if __name__ == "__main__":

    grades = [1, 1, 1]
    bonus(grades)
    print(grades)



