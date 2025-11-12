from pygments.lexer import words

from to_do import TODO


def task15(sentence: str) -> dict[str, int]:

    words = ""
    for character in sentence:
        if character not in (',', ';', '.', ':'):
            words += character

    new_sentence = words.lower().split()
    result = {}
    for word in new_sentence:
        result[word[0]] = result.get(word[0], 0) + 1

    return result

if __name__ == "__main__":

    # sentence = "This is the Very small Text"
    print(task15(sentence = "This is the Very small Text"))

    #print(task15(sentence= "this This THIS is still the very very same"))
