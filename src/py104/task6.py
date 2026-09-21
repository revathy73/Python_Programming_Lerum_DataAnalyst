"""
You are given the variable sentence. Change to uppercase every character
located in an even position.

Save your result in a variable called result.

Example Solution
Assume that
sentence is I like Gothenburg
Then
result is I LiKe GOtHeNbUrG
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO


def task6(sentence: str) -> str:
    """
    # solution 1:
    result = ""
    for index,letter in enumerate(sentence):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter
    return result
    """

    # solution 2: for loop with Ternary operator)
    result = ""
    for index,letter in enumerate(sentence):
        letter_add = letter.upper() if index % 2 == 0 else letter
        result += letter_add
    return result



if __name__ == "__main__":

    # sentence = "I like Gothenburg"
    print(task6(sentence = "I like Gothenburg"))


