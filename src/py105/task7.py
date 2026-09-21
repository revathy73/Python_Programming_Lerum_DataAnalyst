"""
You are given a list called words. Create a map such that its values are
the words in the list and each key is the index of the word in the list.

Save your result in a variable called result.

Example Solution
Assume that
words is ["I", "love", "Kotlin"]
Then
result is
{
    0 to "I",
    1 to "love",
    2 to "Kotlin"
}
Notes
Your solution must use loops.
"""

from to_do import TODO


def task7(words: list[str]) -> dict[int, str]:

    result = {}
    for index,word in enumerate(words):
       # result = result.get(index,word)
       result[index] = word

    return result

if __name__ == "__main__":

    # words = ["I", "love", "Kotlin"]
    print(task7(words = ["I", "love", "Kotlin"]))
