from to_do import TODO


def guide16(sentence: str) -> str:

    result = ""
    for index,letter in enumerate(sentence):
        if index % 2 == 0:
            result += letter
            # result = result + letter


    return result

if __name__ == "__main__":

    #sentence = "Hello"
    print(guide16("Hello"))

    #sentence = "2345678"
    print(guide16("2345678"))

