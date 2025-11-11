from to_do import TODO


def task10(mapa: dict[int, str]) -> dict[str, int]:

    result = {}
    for number, letter in mapa.items():
        result[letter] = number

    return result

if __name__ == "__main__":

    # mapa = {1 : "A",2 : "B", 3 : "C"}
    print(task10(mapa = {1 : "A",2 : "B", 3 : "C"}))