 from to_do import TODO


def guide14(a: int, b: int) -> int:

    if a >= b:
        return -1

    result = 0
    for number in range(a, b + 1):
        if number % 2 == 0:
        #    result = result + number
             result += number

    return result

if __name__ == "__main__":

    # a=1, b=6
    print(guide14(a=1,b=6))

    # a=1, b=5
    print(guide14(a=1, b=5))

    # a=7, b=3
    print(guide14(a=7, b=5))

    # a=5, b=5
    print(guide14(a=5, b=5))



