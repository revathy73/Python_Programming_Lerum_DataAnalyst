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