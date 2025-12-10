def harshad(number : int) -> bool:

    if number == 0:
        return False

    total = 0
    for digit in str(number):
        total += int(digit)

    return number % total == 0

if __name__ == "__main__":

    print(harshad(number= 1729))