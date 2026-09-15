"""
Code has been given that identifies the indices at which the letter H appears
in a sentence.

Generalize the given code into a function called indexer so that the function
can be used for any given sentence.
"""
def indexer(sentence: str) -> list[int]:

    positions = []

    for index, letter in enumerate(sentence):
        if letter == "H":
            positions.append(index)

    return positions



if __name__ == "__main__":

    print(indexer("Hello world, I am looking for Henry"))
    print(indexer("Hello world, I am very Hungry"))
