from to_do import TODO


def task13(sells: list[int]) -> str:

    result = ""
    highest_value = sells[0]
    value = 0
    for index,sell in enumerate(sells):
        if sell > highest_value:
            highest_value = sell
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
    print(task13(sells = [1000, 100, 800, 768, 765, 90, 10]))


"""
days = ["Monday","Tuesday","wednesday","Thursday","Friday","Saturday","Sunday"]

    highest_value = sells[0]
    index = 0
    result = ""
"""