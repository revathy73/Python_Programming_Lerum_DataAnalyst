from to_do import TODO


def guide15(a: int, b: int) -> int:

    if a >= b:
        return -1

    result = 1
    for number in range(a, b + 1):
        if number % 2 != 0:
            result *= number

    return result

if __name__ == "__main__":

    # a=1, b=6
    print(guide15(a=1,b=6))

    # a=7, b=2
    print(guide15(a=7, b=2))

    #a= 7, b=7
    print(guide15(a=7, b=7))

    # a= 2, b= 9
    print(guide15(a=2, b=9))