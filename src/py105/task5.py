"""
You are given the variables mapa and constant. Identify all the keys in mapa
that are not paired with the value constant

Save your result in a variable called result.

Example Solution
Assume that
mapa is {1 to 100, 3 to 200, 4 to 500}
constant is 100
Then
result is [3, 4]
Hint
The keys [3, 4] are the only ones not paired with the value of constant, or
100.
Notes
Use conditional statements and loops in your solution.
"""

from to_do import TODO


def task5(mapa: dict[int, int], constant: int) -> list[int]:

    result = []
    for id, number in mapa.items():
        if constant != number:
            result.append(id)

    return result

if __name__ == "__main__":
    # mapa = {1:100, 2:100, 3:200} ,parameter = 100
    print(task5(mapa = {1:100, 2:100, 3:200} ,constant = 100))
