def counter(string) -> bool:

    #result = True
    total = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in string:
        if char.lower() in alphabet:
            position = alphabet.index(char.lower()) + 1
            total += position

    return total % 2 == 0


if __name__ == "__main__":

    print(counter("alexa"))
    print(counter("hello"))