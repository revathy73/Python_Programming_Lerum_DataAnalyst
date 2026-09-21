"""
In each question, you are given the variable sells. Each element represents the number of sales made per day in one week.

Assume that each day of the week is represented by the following numbers:

Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6
Use this information to solve the questions below.

What were the total sales in the week?

Save your result in a variable called result.

Example Solution
Assume that
sells is [20, 100, 800, 768, 765, 90, 10]
Then
result is 2553
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO


def task15(sells: list[int]) -> int:

    result = 0
    for sell in sells:
        result += sell

    return result

if __name__ == "__main__":

    # sells = [20, 100, 800, 768, 765, 90, 10]  --> 2553
    print(task15(sells = [20, 100, 800, 768, 765, 90, 10]))
