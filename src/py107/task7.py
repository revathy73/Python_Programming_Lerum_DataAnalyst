def censorship(sentence : str) -> str :

    result = []

    for text in sentence.split():
        word = ""
        special_char = ""
        for letter in text:
            if letter.isalnum():
                word += letter
            else:
                special_char += letter
        if len(word) > 4:
            word = "*" * len(word)

        result.append(word + special_char)

    return " ".join(result)

if __name__ == "__main__":

    #print(censorship(sentence="wrds."))  # word.
    print(censorship(sentence="wor.ds"))  # *****.
    print(censorship(sentence = "Avoid saying bad words"))
    print(censorship(sentence="I live in Sweden"))




