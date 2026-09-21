"""
You are given a map called birthdays in which the keys are the names of
people and the values are the months they were born.

Return a map in which the keys are the names of people and the values are
the seasons of the year they were born.

Example Solution::
Spring occurs between months 3, 4, 5
Summer occurs between months 6, 7, 8
Fall occurs between months 9, 10, 11
Winter occurs between months 12, 1, 2
Assume that
birthdays is
{
    "Rita" to 1,
    "Jay" to 5
}
Then
result is
{
    "Rita" to "Winter",
    "Jay" to "Spring"
}
"""

from to_do import TODO


def guide15(birthdays: dict[str, int]) -> dict[str, str]:
    """
    # solution 1:
    result = {}
    for name,month in birthdays.items():
        if (month < 1 or month > 12):
            return "error"

        if month in range(3, 6):
            month = "Spring"
        elif month in range(6, 9):
            month = "Summer"
        elif month in range(9, 12):
            month = "Fall"
        else:
            month = "Winter"

        result[name] = month

    return result
    """

    # solution 3:
    for name, month in birthdays.items():
        if (month < 1 or month > 12):
            return "error"

        if month in range(3, 6):
            birthdays.update({name:"Spring"})
        elif month in range(6, 9):
            birthdays.update({name:"Summer"})
        elif month in range(9, 12):
            birthdays.update({name:"Fall"})
        else:
            birthdays.update({name:"Winter"})

    return birthdays


if __name__ == "__main__":

    # birthdays = {"Rita": 1,"Jay": 5}
    print(guide15(birthdays = {"Rita": 1,"Jay":5}))

    # birthdays = {"Devi": 6,"Jay": 12}
    print(guide15(birthdays={"Devi": 6,"Jay": 12}))
