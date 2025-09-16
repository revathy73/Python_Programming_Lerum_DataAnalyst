from to_do import TODO


def task8(sentence: str, character: str) -> int:

    # INPUT the text
    # Count number times the character occurs in the text
    # Output the result

    result = sentence.count('I')
    return result

if __name__ == "__main__":

    # sentence = INDIA
    print(task8(sentence= "INDIA", character= "I"))
