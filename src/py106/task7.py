from to_do import TODO


def task7(sentence: str) -> dict[str, int]:


    if sentence is None or sentence == "" :
        return {"letters" : 0, "digits" : 0}

    result = {"letters" : 0, "digits" : 0}
    #result["letters"] = 0
    #result["digits"] = 0
    for char in sentence:
        if char.isalpha():
            result["letters"] = result["letters"] + 1
        elif char.isdigit():
            result["digits"] = result["digits"] + 1

    return result

if __name__ == "__main__":

    # sentence = "H3ll0"
    print(task7(sentence = "H3ll0"))

    # sentence = None
    print(task7(sentence = "None"))
