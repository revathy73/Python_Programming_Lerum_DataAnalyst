import re

from to_do import TODO

def task10(password: str) -> bool:

    lowercase_re = re.findall("[a-z]", password)
    uppercase_re = re.findall("[A-Z]", password)
    digits_re = re.findall("[0-9]", password)
    special_re = re.findall("[@#$]", password)

    return (
        len(password) in range(6, 11)
        and len(lowercase_re) > 0
        and len(uppercase_re) > 0
        and len(digits_re) > 0
        and len(special_re) > 0

    )


if __name__ == "__main__":

    # password = peter#son23
    print(task10(password = "Pete#31"))

    print(task10(password = "sweden"))

    print(task10(password = "pEarson123#"))

    print(task10(password = "Swed1#"))

    # solution: 2
    """
     if len(password) < 6 or len(password) > 10:
        return False

    has_upper = False
    has_lower = False
    has_digits = False
    has_special = False

    for letter in password:
        if letter.isupper():
            has_upper = True
        elif letter.islower():
            has_lower = True
        elif letter.isdigit():
            has_digits = True
        elif letter in "$#@":
            has_special = True


    return has_upper and has_lower and has_digits and has_special

    """

