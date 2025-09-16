from to_do import TODO


def task9(sentence: str, character: str) -> bool:

    result = 'U' in sentence
    return result


if __name__ == "__main__":

    # sentence = EUROPE
    print(task9(sentence = "EUROPE", character = "U"))
