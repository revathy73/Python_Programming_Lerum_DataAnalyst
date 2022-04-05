if __name__ == "__main__":
    sentence = "I want to visit Hawaii, Hungary, and Honduras"
    positions = []

    for index, letter in enumerate(sentence):
        if letter == "H":
            positions.append(index)

    print(positions)
