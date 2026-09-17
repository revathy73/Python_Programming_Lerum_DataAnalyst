"""
You are given the variable sentence. Replace every vowel with an *.

Save your result in a variable called result.

Assign a value of * to result if sentence is empty.
Assign a value of * to result if sentence is null.
Example Solution
Assume that
sentence is I live in SwEdEn
Then
result is * l*v* *n Sw*d*n
Notes
Use a, e, i, o, u as your vowels.
Your solution cannot be case sensitive
"""
from to_do import TODO


def task3(sentence: str) -> str:

    result = ""
    vowels = "aeiouAEIOU"
    if sentence is None or len(sentence) == 0:
        result = "*"
    else:
        for letter in sentence:
            if letter in vowels:
                result += letter.replace(letter,'*')
            else:
                result += letter

    return result

if __name__ == "__main__":

    # sentence = "I love Sweden"
    print(task3(sentence= "I love Sweden"))
