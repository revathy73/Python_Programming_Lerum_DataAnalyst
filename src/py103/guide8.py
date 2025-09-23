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



    if day == 1:
        return "monday"
    elif day == 2:
         return "tuesday"
    elif day == 3:
         return "wednesday"
    elif day == 4:
         return "thursday"
    elif day == 5:
         return "friday"
    elif day == 6:
         return "saturday"
    elif day == 7:
         return "sunday"
    else:
         return "error"




if __name__ == "__main__":

    # day = 1
    print(guide8( day = 1))

    # day = -1
    print(guide8(day = -1))

    # day = 5
    print(guide8(day = 5))

    # day = 7
    print(guide8(day = 7))


