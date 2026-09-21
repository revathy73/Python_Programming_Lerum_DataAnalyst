"""
You are given the variable day, which is a number representing a day of the
week. Use that number to determine the day of the week.

Save your result in a variable called result

Days of the week
monday is 1
tuesday is 2
wednesday is 3
thursday is 4
friday is 5
saturday is 6
sunday is 7
error is any number that is not between 1 and 7
Example Solution
Assume that
day is 5
Then
result is friday
"""

from to_do import TODO


def guide8(day: int) -> str:
    """
    if day < 1 or day > 7 :
        result = "error"
    elif day == 1:
        result = ("monday")
    elif day == 2:
        result = ("tuesday")
    elif day == 3:
        result = ("wednesday")
    elif day == 4:
        result = ("thursday")
    elif day == 5:
        result = ("friday")
    elif day == 6:
        result = ("saturday")
    elif day == 7:
        result = ("sunday")

    return result
    """

    if (day < 1 or day > 7):
        return "error"

    if day == 1:
        result = "monday"
    elif day == 2:
        result = "tuesday"
    elif day == 3:
        result = "wednesday"
    elif day == 4:
        result = "thursday"
    elif day == 5:
        result = "friday"
    elif day == 6:
        result = "saturday"
    else:
        result = "sunday"

    return result


if __name__ == "__main__":

    # day = 1
    print(guide8( day = 1))

    # day = -1
    print(guide8(day = -1))

    # day = 5
    print(guide8(day = 5))

    # day = 7
    print(guide8(day = 7))


