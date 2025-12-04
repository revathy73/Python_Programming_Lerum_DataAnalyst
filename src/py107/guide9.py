def transformer(sentence: str) -> str:

    letters_of_interest = ["a", "e", "i", "o", "u"]
    new_string = ""

    for letter in sentence:
        new_string += "$" if letter.lower() in letters_of_interest else letter

    return new_string


if __name__ == "__main__":

    print(transformer(sentence = "The country am living is sweden"))
    print(transformer(sentence="Thr r n vwls n hr"))