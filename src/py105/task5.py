from to_do import TODO


def task5(mapa: dict[int, int], constant: int) -> list[int]:

    result = []
    for id, number in mapa.items():
        if constant != number:
            result.append(id)

    return result


if __name__ == "__main__":
    # mapa = {1:100, 2:100, 3:200} ,parameter = 100
    print(task5(mapa = {1:100, 2:100, 3:200} ,constant = 100))
