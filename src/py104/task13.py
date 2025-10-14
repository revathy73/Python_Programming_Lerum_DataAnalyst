from to_do import TODO


def task13(sells: list[int]) -> str:

    for index,sell in enumerate(sells):
        if sells[0] > sells[index]:
           result = "Monday"
        elif sells[1] > sells[index]:
            result = "Tuesday"
        elif sells[2] > sells[index]:
            result = "Wednesday"
        elif sells[3] > sells[index]:
            result = "Thursday"
        elif sells[4] > sells[index]:
            result = "Friday"
        elif sells[5] > sells[index]:
            result = "Saturday"
        else:
            result = "Sunday"

    return result

if __name__ == "__main__":

    # sells = [20, 100, 800, 768, 765, 90, 10]
    print(task13(sells = [20, 100, 800, 768, 765, 90, 10]))
