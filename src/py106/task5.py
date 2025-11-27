from to_do import TODO


def task5(word: str) -> bool:

    if word is None or len(word) == 0:
        return False

    counter = dict()
    for letter in word:
        lowered_letter = letter.lower()
        current_letter_count = counter.get(lowered_letter, 0)

        counter[lowered_letter] = current_letter_count + 1

    highest_value =max(counter.values())

    return highest_value == 1

if __name__ == "__main__":

    # word = "sweden"
    print(task5(word = "sweden"))


