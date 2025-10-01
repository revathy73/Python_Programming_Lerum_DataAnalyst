from to_do import TODO


def task6(number: int) -> int:

    """
    rev_num = int(str(number)[::-1])
    return rev_num
    """
    result = 0
    while number > 0:
        digit = number % 10
        result = result * 10 + digit
        number //= 10
    
    return result

if __name__ == "__main__":

    # number = 678
    print(task6(number=678))

    # number = 100026
    #print(task6(number=100026))

