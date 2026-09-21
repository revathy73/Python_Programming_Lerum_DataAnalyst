"""
You are given the maps a and b. Create a list which only contains the keys
that are present in both maps.

Save your result in a variable called result.

Example Solution #1
Assume that
a is {1 to "A", 2 to "B", 3 to "C"}
b is {1 to "A", 2 to "B", 4 to "D"}
Then
result is [1, 2]
Notes
Use conditional statement and loops in your solution.
"""

from to_do import TODO


def task3(a: dict[int, str], b: dict[int, str]) -> list[int]:

    result = []
    for number in a.keys():
        if number in b.keys():
            result.append(number)

    return result


if __name__ == "__main__":

    # a = {1:"A", 2:"B", 3:"C"}, b = {1:"A", 2:"B", 4:"D"}
    print(task3(a = {1:"A", 2:"B", 3:"C"}, b = {1:"A", 2:"B", 4:"D"}))
