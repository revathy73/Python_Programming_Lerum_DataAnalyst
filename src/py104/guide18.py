import string

from to_do import TODO


def guide18() -> tuple[str]:
    """
    # solution 1: for loop
    result = []
    vowels = ["a","e","i","o","u"]
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter in vowels:
            result.append(letter.upper())
        else:
            result.append(letter)

    return tuple(result)

    # solution 1: for loop (ternary operator)
    result = []
    vowels = ["a","e","i","o","u"]
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        value_to_add = letter.upper() if letter in vowels else letter
        result.append(value_to_add)

    return  tuple(result)
    """
    # solution 1: tuple comprehension

    vowels = ["a", "e", "i", "o", "u"]
    alphabet =  string.ascii_lowercase
    result = tuple((letter.upper() if letter in vowels else letter for letter in alphabet))
    return result

if __name__ == "__main__":

    print(guide18())
