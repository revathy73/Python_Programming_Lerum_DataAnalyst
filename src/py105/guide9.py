"""

"""
from to_do import TODO


def guide9(word: str) -> dict[str, int]:
    """
    # solution 1: for loop
    result = {}
    for letter in word:
        # if the letter is in the result
        if letter in result:
            # increase the count by 1
            result[letter] = result[letter] + 1
        # else add the value to the dict and set the value to 1
        else:
            result[letter] = 1

    return result

    # solution 2: Ternary operator
    result = {}

    for letter in word:
        result[letter] = result[letter] + 1 if letter in result else 1

    return result
    """
    # solution 3: no control flow
    result = dict()
    for letter in word:
        result[letter] = result.get(letter, 0) + 1

    return result
    """
    # solution 4: count() method
    result = {}
    for letter in word:
        if letter not in result:
            result[letter] = word.count(letter)

    return result
    """


if __name__ == "__main__":

    # word = "apple"
    print(guide9(word= "apple"))

    # word = "apPle"
    print(guide9(word="apPle"))
