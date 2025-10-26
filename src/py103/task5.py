from to_do import TODO


def task5(sentence: str) -> int:

    result = 0
    for character in sentence:
        result += 1
    #result = len(sentence)
    return result

if __name__ == "__main__":

    # sentence = "I love India"
    print(task5(sentence = "I love India"))

    # sentence = "PeterPearson"
    print(task5(sentence="Peter"))

    # sentence = "Dev@port_AB"
    print(task5(sentence="Dev@port_AB"))


