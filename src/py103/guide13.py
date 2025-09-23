from to_do import TODO


def guide13(number: int) -> bool:
    return number % 2 != 0

if __name__ == "__main__":

    # number = 13
    print(guide13(number=13))

    # number = 9
    print(guide13(number=9))

    # number = 17
    print(guide13(number=17))

    # number = 12
    print(guide13(number=12))

    # number = 16
    print(guide13(number=16))

    """
        # Another Method :: 1
        if number % 2 != 0:
            return True
        else:
            return False

        # Another Method :: 2

        if number % 2 != 0:
            result =  True
        else:
            result = False
            
        return result    

        """