from to_do import TODO


def task14(sells: list[int]) -> str:

    result = ""
    least_value = sells[0]
    value = 0

    for index,sell in enumerate(sells):
        if sell < least_value:
            least_value = sell
            value = index

    if value == 0:
        result = "Monday"
    elif value == 1:
        result = "Tuesday"
    elif value == 2:
        result = "Wednesday"
    elif value == 3:
        result = "Thursday"
    elif value == 4:
        result = "Friday"
    elif value == 5:
        result = "Saturday"
    else:
        result = "Sunday"

    return result

if __name__ == "__main__":

    # sells = [20, 100, 800, 768, 765, 90, 10]
    print(task14(sells = [20, 100, 800, 768, 765, 90, 10]))