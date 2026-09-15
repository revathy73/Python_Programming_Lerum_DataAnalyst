"""
Create a function called indecisive in which the user provides a month number
and the function returns the season name.

The user has the option of not providing any month number and, in that case,
the default output must be Fall.
Seasons of the year:
1.Spring occurs between months 3, 4, 5
2.Summer occurs between months 6, 7, 8
3.Fall occurs between months 9, 10, 11
4.Winter occurs between months 12, 1, 2
5.Error occurs when the value of month is not a number between 1 and 12
"""
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



