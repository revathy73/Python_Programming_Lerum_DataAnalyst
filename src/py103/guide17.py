"""
You are given the variable sentence, which represents a text.
Transform the text to make uppercase all the letters located at an even
position and lowercase all the letters at an odd position.

Save the new text in a variable called result

Example Solution
Assume that
sentence is gothenburg
Then
result is GoThEnBeRg
"""

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


