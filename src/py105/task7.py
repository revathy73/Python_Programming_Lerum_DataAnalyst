from to_do import TODO


def task7(words: list[str]) -> dict[int, str]:

    result = {}
    for index,word in enumerate(words):
       # result = result.get(index,word)
       result[index] = word

    return result

if __name__ == "__main__":

    # words = ["I", "love", "Kotlin"]
    print(task7(words = ["I", "love", "Kotlin"]))
