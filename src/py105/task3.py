from to_do import TODO


def task3(a: dict[int, str], b: dict[int, str]) -> list[int]:

    result = []
    for number in a.keys():
        if number in b.keys():
            result.append(number)

    return result


if __name__ == "__main__":

    # a = {1:"A", 2:"B", 3:"C"}, b = {1:"A", 2:"B", 4:"D"}
    print(task3(a = {1:"A", 2:"B", 3:"C"}, b = {1:"A", 2:"B", 4:"D"}))
