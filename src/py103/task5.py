"""
You are given the variable sentence.

Count the number of characters in the variable sentence using loops.

Save your result in a variable called result.

Example Solution
Assume that
sentence is I love GBG
Then
result is 10
Notes
Spaces count as characters too
"""

from to_do import TODO


def task5(sentence: str) -> int:

    result = 0
    for character in sentence:
        result += 1
    #result = len(sentence)
    return result

if __name__ == "__main__":

    # sentence = "I love India"
    print(task5(sentence = "I love India"))

    # sentence = "PeterPearson"
    print(task5(sentence="Peter"))

    # sentence = "Dev@port_AB"
    print(task5(sentence="Dev@port_AB"))


