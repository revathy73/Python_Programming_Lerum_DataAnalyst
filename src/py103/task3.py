from to_do import TODO


def task3(number: int) -> int:

    result = 1
    for integer in range(1, number+1):
        result *= integer

    return result

if __name__ == "__main__":

    # number = 3
    print(task3(number=3))

    # number = 6
    print(task3(number=6))


