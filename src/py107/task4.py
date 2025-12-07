def washing(number_of_times : int, number_of_months : int) -> float:

    result = 0.0

    result = number_of_times * number_of_months * 30  * (21 / 60)
    return result


if __name__ == "__main__":

    print(washing( number_of_times = 8,number_of_months = 7))

