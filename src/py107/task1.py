def remover(input : str) -> str:

    """
    result = []
    text = list(input)
    vowels = "AEIOU"
    for letter in text:
        if letter.lower() not in vowels.lower():
            result.append(letter)

    return str(result)
    """

    result = ""
    vowels = "AEIOU"
    for letter in input:
        if letter.lower() not in vowels.lower():
            result += letter

    return result


if __name__ == "__main__":

    print(remover(input = "Sweden is nice"))
    print(remover(input = "HELLO"))
