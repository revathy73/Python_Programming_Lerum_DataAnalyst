"""
You are given the variables mapa and prospect. Determine if mapa has a key with the value prospect

Save your result in a variable called result.

Example Solution
Assume that
mapa is {1 to "A", 2 to "B", 3 to "C"}
prospect is 1
Then
result is true
Notes
Use conditional statements and loops in your solution.
"""

from to_do import TODO


def task11(mapa: dict[int, str], prospect: int) -> bool:

    result = False
    for number in mapa.keys():
        if prospect == number:
            result = True

    return result


if __name__ == "__main__":

    # mapa = {1 : "A", 2 : "B", 3 : "C"}, prospect = 1  ----> True
    print(task11(mapa = {1 : "A", 2 : "B", 3 : "C"}, prospect = 1))

    # mapa = {1 : "A", 2 : "B", 3 : "C"}, prospect = 4  ----> False
    print(task11(mapa={1: "A", 2: "B", 3: "C"}, prospect = 4))

