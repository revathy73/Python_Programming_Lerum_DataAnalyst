"""
You are given the variables sentence and character. Use a while loop to
determine the position at which character first appears in sentence

Save your result in a variable called result

Example Solution
Assume that
sentence is ABCDA
character is a
Then
result is 0
Notes
Use a while loop to solve the problem
Your program must not be case-sensitive
Assume that character is always present in sentence
"""

from to_do import TODO


def guide20(sentence: str, character: str) -> int:

    index = 0
    size_of_sentence = len(sentence)
    result = 0

    while index < size_of_sentence:
        current_character = sentence[index]
        if current_character.lower() == character.lower():
            result = index
            break
        index += 1
    return result

if __name__ == "__main__":

    # sentence = "hello", character = "e"
    print(guide20(sentence="hello", character="e"))

    # sentence = "world", character = "r"
    print(guide20(sentence="world", character="r"))

    # sentence = "PythoN", character = "N"
    print(guide20(sentence="PythoN", character="N"))


