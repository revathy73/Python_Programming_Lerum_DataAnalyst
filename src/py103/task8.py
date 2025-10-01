from to_do import TODO


def task8(number: int) -> int:

    result = 0
    while number > 0:
        add_digit = number % 10
        result += add_digit
        number //= 10

    return result

if __name__ == "__main__":

    # number = 234
    print(task8(number=234))

    # number = 4512
    print(task8(number=4512))



