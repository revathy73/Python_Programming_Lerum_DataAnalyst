from to_do import TODO


def task10(items: list[str]) -> int:

    if items == []:
        return None

    result = 0
    #search_str = "Nemo"
    for index,item in enumerate(items):
        if item == "Nemo":
            result =  index
            break
        else:
            result = None

    return result


if __name__ == "__main__":

    # items = ["I", "cannot", "Nemo", "find", "him"]
    print(task10(items = ["I", "cannot", "Nemo", "find", "him"]))

    # items = ["Nemo", "NEMO", "nemo", "find", "nEMO"]
    print(task10(items = ["Nemo", "NEMO", "nemo", "find", "nEMO"]))

    print(task10(items = ['Maybe', 'you', None, 'Nemo', 'find', None]))