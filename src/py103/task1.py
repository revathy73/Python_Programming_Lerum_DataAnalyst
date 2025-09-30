from to_do import TODO


def task1(a: int, b: int) -> int:

    if a >= b:
       return 0

    result = 0
    for number in range(a, b+1):
        result += number

    return result

if __name__ == "__main__":

    # a = 1,  b = 1
    print(task1(a=1, b=1))

    # a = 1,  b = 5
    print(task1(a=1, b=5))

    # a= 2, b = 20
    print(task1(a=2, b=20))

