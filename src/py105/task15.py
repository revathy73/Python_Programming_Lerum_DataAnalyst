"""
You are given the variable sentence. Keep count of how many words start
with each letter of the alphabet.

Save your result in a variable called result.

Example Solution
Assume that
sentence is This is the Very small Text
Then
result is {i=1, s=1, t=3, v=1}
Notes
Your implementation should not be case-sensitive.
Only store in result the letters that have a counter larger than 0.
Ignore special characters such as: ,, ;, ., :.
Assume sentence will never be an empty string.
Use conditional statements and loops in your solution.
"""

from pygments.lexer import words

from to_do import TODO


def task15(sentence: str) -> dict[str, int]:

    words = ""
    for character in sentence:
        if character not in (',', ';', '.', ':'):
            words += character

    new_sentence = words.lower().split(" ")
    result = {}
    for word in new_sentence:
        result[word[0]] = result.get(word[0], 0) + 1

    return result

if __name__ == "__main__":

    # sentence = "This is the Very small Text"
    print(task15(sentence = "This is the Very small Text"))

    #print(task15(sentence= "this This THIS is still the very very same"))
