from to_do import TODO


def task7(a: int, b: int) -> int:

    if a and b == 0:
        return 1

    result = 1
    for integer in range(1, b+1):  #  for integer in range(b):
        result = result * a

    return result


if __name__ == "__main__":

    # a=2 , b= 3
    print(task7(a=2, b=3))

    # a=3 , b= 5
    print(task7(a=3, b=5))

    # a=1 , b= 1
    print(task7(a=1, b=1))




