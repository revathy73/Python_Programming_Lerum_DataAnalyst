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
       


