from to_do import TODO


def task5(sentence: str) -> int:

    for character in sentence:
        result = sentence.count(character)
    #no_of_characters = len(sentence)
    return result

if __name__ == "__main__":

    # sentence = "I love India"
    print(task5(sentence = "I love India"))

    # sentence = "PeterPearson"
    print(task5(sentence="Peter"))

    # sentence = "Dev@port_AB"
    print(task5(sentence="Dev@port_AB"))


