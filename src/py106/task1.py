"""
You are given the variable sentence. Use it to calculate its length.

Save your result in a variable called result.

Assign a value of 0 to result if sentence is null.
Example Solution
Assume that
sentence is "I love GBG"
Then
result is 10
"""
from to_do import TODO


def task1(sentence: str) -> int:

    result = 0
    if sentence is None:
       result = 0
    else:
        result = len(sentence)

    return result

if __name__ == "__main__":

    # sentence = "I love GBG"
    print(task1(sentence= "I love GBG"))
