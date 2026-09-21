"""
You are given the variable age, which represents the age of a person.
Determine the stage of life the person is in.

Save your result in a variable called result.

Stages of life
infant a person between 0 to 1 year old
toddler a person between 2 to 4 years old
child a person between 5 to 12 years old
teen a person between 13 to 19 years old
adult a person between 20 to 39 years old
middle adult a person between 40 to 59 years old
senior adult a person 60 years old and above.
Example Solution
Assume that
age is 30
Then
result is adult
"""

from to_do import TODO


def guide6(age: int) -> str:

    """
    if(age < 2):
        result = "infant"
    elif(age < 5):
        result = "toddler"
    elif(age < 13):
        result = "child"
    elif(age < 20):
        result = "teen"
    elif(age < 40):
        result = "adult"
    elif(age < 60):
        result = "middle adult"
    else:
        result = "senior adult"
    return result
    """
    if age in range(0, 2):
        return "infant"
    elif age in range(2, 5):
        return "toddler"
    elif age in range(5, 13):
        return "child"
    elif age in range(13, 20):
        return "teen"
    elif age in range(20, 40):
        return "adult"
    elif age in range(40, 60):
        return "middle adult"
    else:
        return "senior adult"


if __name__ == "__main__":

        # age = 1   ---> infant
        print(guide6(age = 1))

        # age = 3   ---> toddler
        print(guide6(age = 3))

        # age = 4   ---> toddler
        print(guide6(age = 4))

        # age = 7   ---> child
        print(guide6(age = 7))

        # age = 5   ---> child
        print(guide6(age = 5))

        # age = 12  ---> child
        print(guide6(age = 12))

        # age = 17  ---> teen
        print(guide6(age = 17))

        # age = 19  ---> teen
        print(guide6(age = 9))

        # age = 25  ---> adult
        print(guide6(age = 25))

        # age = 45  ---> middle adult
        print(guide6(age = 45))

        # age = 59  ---> middle adult
        print(guide6(age = 59))

        # age = 40  ---> middle adult
        print(guide6(age = 40))

        # age = 60  ---> senior adult
        print(guide6(age = 60))

        # age = 65  ---> senior adult
        print(guide6(age = 65))

        # age = 70  ---> senior adult
        print(guide6(age = 70))


