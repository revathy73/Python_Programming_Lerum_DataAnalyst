from to_do import TODO


def guide12(number: int) -> bool:

    if number % 2 == 0:
        result = True
    else:
        result = False

    return result



if __name__ == "__main__":

    # number = 15
    print(guide12( number = 15))

    # number = 7
    print(guide12(number = 7))

    # number = 19
    print(guide12(number = 19))

    # number = 21
    print(guide12(number = 21))

    # number = 16
    print(guide12(number = 16))

    # number = 10
    print(guide12(number = 10))

    # number = 4
    print(guide12(number = 4))

    """
    # Another Method :: 1
    if number % 2 == 0:
        return True
    else:
        return False

    # Another Method :: 2
    
    return number % 2 == 0 
       
    """
