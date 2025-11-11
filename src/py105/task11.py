from to_do import TODO


def task11(mapa: dict[int, str], prospect: int) -> bool:

    result = False
    for number in mapa.keys():
        if prospect == number:
            result = True

    return result


if __name__ == "__main__":

    # mapa = {1 : "A", 2 : "B", 3 : "C"}, prospect = 1  ----> True
    print(task11(mapa = {1 : "A", 2 : "B", 3 : "C"}, prospect = 1))

    # mapa = {1 : "A", 2 : "B", 3 : "C"}, prospect = 4  ----> False
    print(task11(mapa={1: "A", 2: "B", 3: "C"}, prospect = 4))

