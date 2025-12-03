def bonus(numbers):
    for index, number in enumerate(numbers):
        numbers[index] = number + 1


if __name__ == "__main__":

    grades = [1, 1, 1]
    bonus(grades)
    print(grades)



