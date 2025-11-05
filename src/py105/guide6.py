from to_do import TODO


def guide6(birthdays: dict[str, int], letter: str, month: int) -> int:

    result = 0

    for person_name,birth_month in birthdays.items():
        first_letter_name = person_name[0]
        if first_letter_name.lower() == letter.lower() and birth_month == month:
            result += 1

    return result

if __name__ == "__main__":

    # birthdays = {"Ana":1,"Anja":1,"Mary":5}
    print(guide6(birthdays = {"Ana":1,"Anja":1,"Mary":5} , letter = "A", month = 1))

    # birthdays = {"Ana":1,"Anja":1,"Mary":5}
    print(guide6(birthdays={"Ana": 1, "Anja": 1, "Mary": 5}, letter="a", month=5))

    # birthdays = {"Ana":1,"Anja":1,"Mary":5}
    print(guide6(birthdays={"Ana": 1, "Anja": 1, "Mary": 5}, letter="M", month=1))


