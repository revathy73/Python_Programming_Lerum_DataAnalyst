"""
You are given a map called birthdays in which the keys are the names of people
and the values are the months of their birthdays.

You are also given the variables letter and month.

Determine how many people whose names begin with the letter letter have a
birthday in the month month.

Save your result in a variable called result

Example Solution
Assume that
letter is "a"
month is 1
birthdays is
{
    "Ana" to 1,
    "Anja" to 1,
    "Mary" to 5
}
Then
result is 2
Notes
Your code cannot be case-sensitive.
"""
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


