from to_do import TODO


def guide6(age: int) -> str:
    """
    if(age < 2):
        result = "infant"
    elif(age < 5):
        result = "toddler"
    elif(age < 12):
        result = "child"
    elif(age < 19):
        result = "teen"
    elif(age < 39):
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


