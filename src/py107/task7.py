def censorship(sentence : str) -> str :

    if sentence == "":
        return ""

    result = ""
    text_components = sentence.split(" ")

    for index,text in enumerate(text_components):
        if len(text) > 4:
            for letter in text:
                if letter in (',', ';', '.', ':'):
                    result += letter
                elif letter != "*":
                    result += "*"
            continue
        else:
            result += text + " "

    return result

if __name__ == "__main__":
    print(censorship(sentence = "I live in Sweden"))

