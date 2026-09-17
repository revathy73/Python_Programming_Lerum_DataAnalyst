"""
You are given the variable sentence. Use it to count the number of times each
vowel appears.

Save your result in a variable called result.

Set result to be an empty map if sentence is empty.
Set result to be an empty map if sentence is null.
Example Solution
Assume that
sentence is Hello
Then
result is
{
    'a' to 0,
    'e' to 1,
    'i' to 0,
    'o' to 1,
    'u' to 0
}
Notes
Use a, e, i, o, u as your vowels.
Your solution cannot be case sensitive.
"""
from to_do import TODO


def task4(sentence: str) -> dict[str, int]:

    if sentence is None or len(sentence) == 0:
        return {}

    result = {}
    vowels = "a","e","i","o","u"

    for char in vowels:
        count = 0
        for letter in sentence.lower():
            if letter == char:
                count += 1
        result[char] = count
    return result

if __name__ == "__main__":

    # sentence = "Hello"
    print(task4(sentence = "Hello"))
