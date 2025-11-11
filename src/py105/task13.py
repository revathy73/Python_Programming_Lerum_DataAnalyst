from to_do import TODO


def task13(sentence: str) -> str:

    result= ""
    words = sentence.split(" ")
    print(words)

    for word in words:
        #if word not in result:
            new_text = word.lower()
            if new_text not in result:
                result = words.count(new_text)

    return result


if __name__ == "__main__":

    # sentence = "this This THIS is still the very very same"
    print(task13(sentence = "this This THIS is still the very very same"))

