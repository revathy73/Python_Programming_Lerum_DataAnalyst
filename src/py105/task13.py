from to_do import TODO


def task13(sentence: str) -> str:

    words = ""
    for character in sentence:
        if character not in (',', ';', '.', ':'):
            words += character

    result= ""
    highest_used = -1.0
    new_word = words.lower().split(" ")
    new_dt = {}
    for word in new_word:
        new_dt[word] = new_word.count(word)
        for text,times_used in new_dt.items():
            if times_used > highest_used:
                highest_used = times_used
                result = text

    return result

    """
        #result[word] = result.get(name, 0) + 1
        if word in new_dt:
            new_dt[word] = new_dt[word] + 1
        else:
            new_dt[word] = 1
    
    """


if __name__ == "__main__":

    # sentence = "this This THIS is still the very very same"
    print(task13(sentence = "this This THIS is still the very very same"))

