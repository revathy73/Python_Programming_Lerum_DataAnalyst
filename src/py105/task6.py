from to_do import TODO


def task6(mapa: dict[int, str], parameter: str) -> dict[int, str]:

    result = {}
    for id, number in mapa.items():
        if parameter == number:
            result[id] = number


    return result


if __name__ == "__main__":

    # mapa = {1:100, 2:100, 3:200} ,parameter = 100
    print(task6(mapa = {20 : "Ana",40 : "John",22 : "Ana"} ,parameter = "Ana"))
