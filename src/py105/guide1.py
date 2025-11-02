from to_do import TODO


def guide1(a: int, b: int) -> dict[int, int]:

    if a >= b:
        return {}

    result = {}
    for number in range(a, b + 1):
        if number % 2 == 0:
            result[number] = number * 2
        else:
            result[number] = number * 3

    return result

if __name__ == "__main__":

    # a = 1, b = 3  ---> {1 : 3, 2 : 4, 3 : 9}
    print(guide1(a = 1, b = 3))

    # a = 2, b = 5  --> {2 : 4, 3 : 9, 4 : 8, 5 : 15}
    print(guide1(a = 2, b = 5))

    # a = 20 , b = 10  ---> {}
    print(guide1(a = 20 , b = 10 ))
