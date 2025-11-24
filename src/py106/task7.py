from to_do import TODO


def task7(sentence: str) -> dict[str, int]:

    result = []
    #alphabet = string.ascii_lowercase
    #numbers = math.inf

    for char in sentence:
        count = 0
        if char.isalpha():
            result["letters"] = count(char)
        elif char.isdigit():
            result["digits"] = count(char)

    return result

if __name__ == "__main__":

    # sentence = "H3ll0"
    print(task7(sentence = "H3ll0"))
