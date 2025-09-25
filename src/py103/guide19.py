from to_do import TODO


def guide19(sentence: str) -> str:

    result = ""
    size_of_sentence = len(sentence)
    index = size_of_sentence - 1


    while index >= 0:
        letter = sentence[index]
        result += letter
        index -= 1

    return result


if __name__ == "__main__":

    # senetence = ABCD
    print(guide19(sentence="ABCD"))

    # senetence = 1234
    print(guide19(sentence="1234"))

    # senetence = zyx
    print(guide19(sentence="zyx"))
