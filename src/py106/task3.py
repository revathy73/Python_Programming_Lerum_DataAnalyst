from to_do import TODO


def task3(sentence: str) -> str:

    result = ""
    vowels = "aeiouAEIOU"
    if sentence is None or len(sentence) == 0:
        result = "*"
    else:
        for letter in sentence:
            if letter in vowels:
                result += letter.replace(letter,'*')
            else:
                result += letter

    return result

if __name__ == "__main__":

    # sentence = "I love Sweden"
    print(task3(sentence= "I love Sweden"))
