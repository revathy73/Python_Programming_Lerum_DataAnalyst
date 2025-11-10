from to_do import TODO


def task4(mapa: dict[int, int], parameter: int) -> list[int]:

    result = []
    for id,number in mapa.items():
        if parameter == number:
            result.append(id)

    return result

    """

    result = 0.0
    for item in ingredients:
        cost = supermarket.get(item, 0.0)
        result += cost

    return result
    """

if __name__ == "__main__":
    # mapa = {1:100, 2:100, 3:200} ,parameter = 100
    print(task4(mapa = {1:100, 2:100, 3:200} ,parameter = 100))

