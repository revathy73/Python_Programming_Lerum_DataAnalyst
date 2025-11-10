from to_do import TODO


def task2(mapa: dict[int, int]) -> int:
    # solution 1: for loop
    """
    result = 0

    for number in mapa.keys():
        result += number

    return result
    """
    # solution 1:
    result = 0
    number = 0
    result = {number: number+number for number in mapa.keys()}
    return result

if __name__ == "__main__":

    print(task2(mapa = {1:10, 2:20, 3:30}))
