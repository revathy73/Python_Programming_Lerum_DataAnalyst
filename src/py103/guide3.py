"""
You are given the variable age, which represents the age of a person.

Determine whether the person is an adult or not.

Save your result in a variable called result.

Example Solution
Assume that
age is 19
Then
result is true
Hint
Assume that a person is considered an adult once they turn 18 years old.
"""

from to_do import TODO


def guide3(age: int) -> bool:

    if age >= 18:
        result = True
    else:
        result = False

    return result

    # return age >= 18
    # return not (age <= 17)

if __name__ == "__main__":

    # age = 15
    print(guide3(age = 15))

    # age = 18
    print(guide3(age = 18))

    # age = 20
    print(guide3(age = 20))

    # age = 45
    print(guide3(age = 45))

