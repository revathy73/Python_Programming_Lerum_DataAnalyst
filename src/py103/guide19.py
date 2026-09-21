"""
You are given the variable sentence, which represents a text.
Use a while loop to create a new text which is the reverse of sentence

Save your result in a variable called result

Example Solution
Assume that
sentence is ABCD
Then
result is DCBA
Notes
Use a while loop to solve the problem
"""

from to_do import TODO


def guide19(sentence: str) -> str:

    result = ""
    size_of_sentence = len(sentence)
    index = size_of_sentence - 1


    while index >= 0:
        letter = sentence[index]
        result += letter
        index -= 1

    return result


if __name__ == "__main__":

    # senetence = ABCD
    print(guide19(sentence="ABCD"))

    # senetence = 1234
    print(guide19(sentence="1234"))

    # senetence = zyx
    print(guide19(sentence="zyx"))
