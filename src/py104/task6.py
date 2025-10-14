from to_do import TODO


def task6(sentence: str) -> str:

    result = ""
    for index,item in enumerate(sentence):

        if index % 2 == 0:
            result += item.upper()
        else:
            result += item

    return result

if __name__ == "__main__":

    # sentence = "I like Gothenburg"
    print(task6(sentence = "I like Gothenburg"))


