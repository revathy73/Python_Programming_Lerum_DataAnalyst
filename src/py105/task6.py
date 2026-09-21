"""
You are given the variables mapa and parameter. Filter mapa to only contain
the key-value pairs that have a value of parameter

Save your result in a variable called result.

Example Solution
Assume that
parameter is Ana
mapa is
{
    20 to "Ana",
    40 to "John",
    22 to "Ana"
}
Then
result is
{
    20 to "Ana",
    22 to "Ana"
}
Notes
Use conditional statements and loops in your solution.
"""

from to_do import TODO


def task6(mapa: dict[int, str], parameter: str) -> dict[int, str]:

    result = {}
    for id,name in mapa.items():
        if parameter == name:
            result[id] = name

    return result

if __name__ == "__main__":

    # mapa = {1:100, 2:100, 3:200} ,parameter = 100
    print(task6(mapa = {20 : "Ana",40 : "John",22 : "Ana"} ,parameter = "Ana"))
