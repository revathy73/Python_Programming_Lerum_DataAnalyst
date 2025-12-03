def indecisive(month = 11):
    if month > 12 or month < 1:
        return "Error"

    if month in range(3, 6):
        return "Spring"
    elif month in range(6, 9):
        return "Summer"
    elif month in range(9, 12):
        return "Fall"
    else:
        return "Winter"


if __name__ == "__main__":

    print(indecisive(month = 1))
    print(indecisive(month = 10))
    print(indecisive(month = 13))
    print(indecisive(month = 3))



