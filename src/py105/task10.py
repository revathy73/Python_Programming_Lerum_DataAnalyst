"""
You are given a variable called mapa. Swap the keys and values of the map.

Save your result in a variable called result.

Example Solution
Assume that
mapa is
{
    1 to "A",
    2 to "B",
    3 to "C"
}
Then
result is
{
    "A" to 1,
    "B" to 2,
    "C" to 3
}
Notes
Use conditional statements and loops in your solution.
"""

from to_do import TODO


def task10(mapa: dict[int, str]) -> dict[str, int]:

    result = {}
    for number, letter in mapa.items():
        result[letter] = number

    return result

if __name__ == "__main__":

    # mapa = {1 : "A",2 : "B", 3 : "C"}
    print(task10(mapa = {1 : "A",2 : "B", 3 : "C"}))