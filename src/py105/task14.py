"""
You are given the variable sentence. Identify which character was used the most.

Save your result in a variable called result.

Example Solution
Assume that
sentence is I am it
Then
result is i
Notes
Your implementation cannot be case-sensitive.
Do not consider spaces as part of your solution.
Ignore special characters such as: ,, ;, ., :
Assume there will always be one letter that is used more than the others.
Provide the value of result in lowercase.
Use conditional statements and loops in your solution.
Do not use the built-in function max().
"""

from to_do import TODO
import re


def task14(sentence: str) -> str:
    """
    words = ""
    for character in sentence:
        if character not in (',', ';', '.', ':',' '):
            words += character

    result = ""
    new_dt = {}
    most_used = -1.0
    new_words = words.lower()
    for letter in new_words:
        new_dt[letter] = new_dt.get(letter, 0) + 1
        for character, number in new_dt.items():
            if number > most_used:
                most_used = number
                result = character

    return result
    """

    word = re.sub("[,.:; ]","", sentence.lower())

    result = ""
    most_used = -1.0
    letter_counter = {}
    for letter in word:
        letter_counter[letter] = word.count(letter)
        for char,times_used in letter_counter.items():
            if times_used > most_used:
                most_used = times_used
                result = char

    return result



if __name__ == "__main__":

    # sentence = "I am it"
    print(task14(sentence = "I am it"))