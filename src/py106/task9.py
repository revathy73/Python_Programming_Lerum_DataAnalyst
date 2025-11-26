from to_do import TODO


def task9(identification: str) -> bool:

    if identification is None or len(identification) > 13:
        return False


    year = identification[0:4]
    month = identification[4:6]
    day = identification[6:8]
    id_number = identification[-4:]

    person_number = identification.split("-")
    if len(person_number[0]) != 8 or len(person_number[1]) != 4:
        return False

    if not month.isdigit() or not day.isdigit() or not year.isdigit() or not id_number.isdigit():
        return False
    if int(month) not in range(1, 13):
        return False
    if int(day) not in range(1, 32):
        return False
    if int(year) < 1947:
        return False


    return True


if __name__ == "__main__":

    # identification = "19871208-3478"
    print(task9(identification = "19871208-3478"))

    print(task9(identification="19271208-3478"))

    print(task9(identification="19470110-1739"))

    print(task9(identification="194701101-1739"))







