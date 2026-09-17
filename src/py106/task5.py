"""
You are given the variable word. Determine if it is an isogram.

Store your result in a variable called result.

Assign a value of false to result if word is empty.
Assign a value of false to result if word is null
Note
Your code cannot be case sensitive.
Hint
An isogram is a word that has no repeated letters. Some examples include:
Algorithm, space, and copyright.
"""
from to_do import TODO


def task5(word: str) -> bool:

    if word is None or len(word) == 0:
        return False

    counter = dict()
    for letter in word:
        lowered_letter = letter.lower()
        #current_letter_count = counter.get(lowered_letter, 0)
        counter[lowered_letter] = counter.get(lowered_letter, 0) + 1
    highest_value =max(counter.values())
    return highest_value == 1

if __name__ == "__main__":

    # word = "sweden"
    print(task5(word = "sweden"))


