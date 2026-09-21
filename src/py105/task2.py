"""
You are given the variable mapa. Use it to add all the keys.

Store your result in a variable called result

Example Solution
Assume that
mapa is {1 to 10, 2 to 20, 3 to 30}
Then
result is 6
Hint
The keys of the map are [1, 2, 3]
Therefore, 1 + 2 + 3 = 6
Notes
Do not use the built-in function sum().
Use conditional statements and loops in your solution.
"""

from to_do import TODO


def task2(mapa: dict[int, int]) -> int:

    # solution 1: for loop

    if mapa == {}:
        return 0

    result = 0
    for number in mapa.keys():
        result += number

    return result
    """
    # solution 1:
    if not in mapa:
        return 0
    result = 0
    number = 0

    result = {number: number+number for number in mapa.keys()}
    return result
     """

if __name__ == "__main__":

    print(task2(mapa = {1:10, 2:20, 3:30}))
