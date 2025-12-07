def indexer(sentence: str) -> list[int]:

    positions = []

    for index, letter in enumerate(sentence):
        if letter == "H":
            positions.append(index)

    return positions



if __name__ == "__main__":

    print(indexer("Hello world, I am looking for Henry"))
    print(indexer("Hello world, I am very Hungry"))
