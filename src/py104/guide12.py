from to_do import TODO


def guide12(a: int, b: int) -> list[int]:

    if a > b:
        result = []

    result = []
    for integer in range(a, b):
        if integer == a:  # we can give instead of this statement (a+1)
            continue
        elif integer % 2 != 0 and integer % 5 == 0:
            result.append(integer * 3)
        elif integer % 2 == 0 and integer % 5 == 0:
            result.append(integer * 5)
        else:
            result.append(integer)

    return result

if __name__ == "__main__":

    # a= 3, b= 10 ---> [4, 15, 6, 7, 8, 9]
    print(guide12(a= 3, b= 10))

    # a= 12, b= 2 ---> []
    print(guide12(a=12, b=2))

    # a= 12, b= 12 ---> []
    print(guide12(a=12, b=12))




