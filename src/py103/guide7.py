"""
You are given the variable month, which is a number representing a month
of the year. Use that number to determine the season of the year.

Save your result in a variable called result

Seasons of the year
spring occurs between months 3, 4, 5
summer occurs between months 6, 7, 8
fall occurs between months 9, 10, 11
winter occurs between months 12, 1, 2
error occurs when the value of month is not a number between 1 and 12
Example Solution
Assume that
month is 11
Then
result is fall
"""

from to_do import TODO


def guide7(month: int) -> str:

    if (month < 1 or month > 12):
        return "error"

    if month in range(3, 6):
        return "spring"
    elif month in range(6, 9):
        return "summer"
    elif month in range(9, 12):
        return "fall"
    else:
        return "winter"

    """
    if (month < 1 or month > 12):
        return "error"

    if month in range(3, 6):
        return "spring"
    elif month in range(6, 9):
        return "summer"
    elif month in range(9, 12):
        return "fall"
    else:
        return "winter"
    """


if __name__ == "__main__":

       # month = 4
       print(guide7(month = 4))

       # month = 8
       print(guide7(month = 9))

       # month = 11
       print(guide7(month = 11))

       # month = 12
       print(guide7(month = 12))

       # month = 15
       print(guide7(month = 15))
       


