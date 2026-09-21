"""
In each question, you are given the variable sells. Each element represents
the number of sales made per day in one week.

Assume that each day of the week is represented by the following
numbers:

Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6
Use this information to solve the questions below.

Which day had the least sales?

Save your result in a variable called result.

Example Solution
Assume that
sells is [20, 100, 800, 768, 765, 90, 10]
Then
result is Sunday
Notes
At least one of your solutions must use a loop
Assume that no two days have the same number of sales
"""

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