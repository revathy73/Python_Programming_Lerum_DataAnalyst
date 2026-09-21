"""
You are given the variable pin, which represents the pin code of a credit
card. Determine if the given pin is valid. The pin code is only valid if
it matches the value 5678

Example Solution
Assume that
pin is 1918
Then
result is false
"""

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





