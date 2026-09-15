"""
Create a function called harshad that satisfies the following requirements:

1) One argument of type Int.
2) The return type is a Boolean.
3) Returns true if the input is a Harshad number and false otherwise.

Hint
1) A number is considered Harshad if it is divisible by the sum of its digits.

2) Harshad numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 1729, and more.

3) Non-Harshad numbers: 11, 13, 15, 17, 19, 22, and more.
"""
def harshad(number : int) -> bool:

    if number == 0:
        return False

    total = 0
    for digit in str(number):
        total += int(digit)

    return number % total == 0

if __name__ == "__main__":

    print(harshad(number= 1729))