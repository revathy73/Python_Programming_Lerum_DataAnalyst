import re

from to_do import TODO


def task13(sentence: str) -> str:
    """
    words = ""
    for character in sentence:
        if character not in (',', ';', '.', ':'):
            words += character

    result= ""
    highest_used = -1.0
    new_word = words.lower().split(" ")
    new_dt = {}
    for word in new_word:
        new_dt[word] = new_word.count(word)
        for text,times_used in new_dt.items():
            if times_used > highest_used:
                highest_used = times_used
                result = text

    return result
    """
    result = ""
    words = re.sub("[,:;. ]","",sentence)
    new_word= words.lower().split(" ")
    word_counter = {}
    most_used = -1.0
    for word in new_word:
        if word in word_counter:
            word_counter[word] = word_counter[word] + 1
            for text, text_used in word_counter.items():
                if text_used > most_used:
                    most_used = text_used
                    result = text
    return result # it has error ,need to check again


if __name__ == "__main__":

    # sentence = "this This THIS is still the very very same"
    print(task13(sentence = "this This THIS is still the very very same"))

