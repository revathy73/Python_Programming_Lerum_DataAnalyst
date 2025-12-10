def tweet(sentence : str) -> str:

    #result = ""
    size = len(sentence)
    result = sentence + ("@" * (280- size))

    return result


if __name__ == "__main__":

    print(tweet(sentence= "I feel good today!"))
