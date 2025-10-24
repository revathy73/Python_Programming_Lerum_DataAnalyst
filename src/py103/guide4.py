from to_do import TODO


def guide4(pin: int) -> bool:

    # Input the PIN
    # If_else statement for check valid PIN
    # If pin correct set the result to be True
    # Else set the result to be false
    # Output the result

    # return pin == 5678
    if pin == 5678:
       result = True
    else:
       result = False

    return result


if __name__ == "__main__":

    # pin = 5678 ---> True
    print(guide4(pin = 5678))

    #pin = 4523 ---> False
    print(guide4(pin = 4523))

    #pin = 2316 ---> False
    print(guide4(pin = 8910))





