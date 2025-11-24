from to_do import TODO


def task4(sentence: str) -> dict[str, int]:

    if sentence is None or len(sentence) == 0:
        return {}

    result = {}
    vowels = "a","e","i","o","u"

    for char in vowels:
        count = 0
        for letter in sentence.lower():
            if letter == char:
                count += 1
        result[char] = count


    return result

if __name__ == "__main__":

    # sentence = "Hello"
    print(task4(sentence = "Hello"))
