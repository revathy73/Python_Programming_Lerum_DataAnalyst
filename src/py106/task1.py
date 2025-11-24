from to_do import TODO


def task1(sentence: str) -> int:

    result = 0
    if sentence is None:
       result = 0
    else:
        result = len(sentence)

    return result

if __name__ == "__main__":

    # sentence = "I love GBG"
    print(task1(sentence= "I love GBG"))
