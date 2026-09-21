"""
You are given the variables mapa and parameter. Identify all the keys in
mapa whose value is equivalent to parameter

Save your result in a variable called result.

Example Solution
Assume that
mapa is {1 to 100, 2 to 100, 3 to 200}
parameter is 100
Then
result is [1, 2]
Hint
The keys [1, 2] are the only ones paired with parameter, or 100.
Notes
Use conditional statements and loops in your solution.
"""
from to_do import TODO


def task4(mapa: dict[int, int], parameter: int) -> list[int]:

    result = []
    for key,number in mapa.items():
        if parameter == number:
            result.append(key)

    return result


if __name__ == "__main__":
    # mapa = {1:100, 2:100, 3:200} ,parameter = 100
    print(task4(mapa = {1:100, 2:100, 3:200} ,parameter = 100))

