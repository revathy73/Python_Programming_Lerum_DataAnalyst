from to_do import TODO


def guide17(sentence: str) -> str:

    result = ""
    for index,letter in enumerate(sentence):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
    return result

if __name__ == "__main__":

    # sentence = australia
    print(guide17(sentence="australia"))

    #sentence = smyckegatan
    print(guide17(sentence= "smyckegatan"))

    # sentence = ABCD
    print(guide17(sentence="ABCD"))

    # sentence = aBcD
    print(guide17(sentence="aBcD"))

    # sentence = aB cD
    print(guide17(sentence="aB cD"))

    # sentence =
    print(guide17(sentence=""))


