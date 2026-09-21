"""
Create a map called result that satisfies the following requirements:

The keys are the even numbers between 10 and 20.

Each value is twice its key.

Notes
Your solution must use loops and conditional statements.
"""

from to_do import TODO


def task1() -> dict[int, int]:
    """
    # Solution 2: (For loop)
    result = {}

    for number in range(10, 20+1):
        if number % 2 == 0:
            result[number] = number * 2

    return result
    """
    # Solution 2: (Dictionary comprehension)
    result = {number: number * 2 for number in range(10, 20+1) if number % 2 == 0}
    return result

if __name__ == "__main__":

    print(task1())
