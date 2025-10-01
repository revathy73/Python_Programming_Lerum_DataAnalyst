from to_do import TODO


def task2(number: int) -> bool:

    if number <= 1:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True


    """
    result = False
    if number > 1:
        for integer in range(2, number+1):
            if number % integer == 0:
                if number == integer:
                    result = True
                else:
                    result = False

    return result
    """

if __name__ =="__main__":

    # number = 5
    print(task2(number = 5))

    # number = 6
    print(task2(number = 6))