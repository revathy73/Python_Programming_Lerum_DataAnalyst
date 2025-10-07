from to_do import TODO


def guide4(a: int, b: int) -> list[int]:

    if a >= b:
        return []

    result = []
    for number in range(a, b + 1):
        if number % 2 != 0 and number % 5 == 0:
            value = number ** 2
            result.append(value)
        elif number % 2 != 0:
            result.append(number)

    return result

if __name__ == "__main__":

    # a = 5, b = 10
    print(guide4(a = 5, b = 10))

    # a = 10, b = 5
    print(guide4(a=10, b=5))




