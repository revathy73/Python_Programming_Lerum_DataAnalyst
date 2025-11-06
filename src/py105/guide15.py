from to_do import TODO


def guide15(birthdays: dict[str, int]) -> dict[str, str]:
    """
    result = {}
    for month in birthdays.values():
        if (month < 1 or month > 12):
            return "error"

        if month in range(3, 6):
            result = "Spring"
        elif month in range(6, 9):
            result = "Summer"
        elif month in range(9, 12):
            result = "Fall"
        else:
            result = "Winter"

    return result
    # solution 2:
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
