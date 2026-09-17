"""
You are given the list called items. Determine the index at which the word
Nemo appears.

Save your result in a variable called result.

Assign a value of null to result in the case that the word Nemo is not present
in items
Example Solution #1
Assume that
items is
["I", "cannot", "Nemo", "find", "him"]
Then
result is 2
Example Solution #2
Assume that
items is
["I", "cannot", "find", "him"]
Then
result is null
Notes
Do not use any built-in function for searching the list.
Your solution must use loops.
If the word Nemo is present in the list, it will always be written as Nemo.
Ignore any other variant like nemo, NEMO, etc.
"""
from to_do import TODO


def task10(items: list[str]) -> int:

    if items == []:
        return None

    result = 0
    #search_str = "Nemo"
    for index,item in enumerate(items):
        if item == "Nemo":
            result =  index
            break
        else:
            result = None

    return result


if __name__ == "__main__":

    # items = ["I", "cannot", "Nemo", "find", "him"]
    print(task10(items = ["I", "cannot", "Nemo", "find", "him"]))

    # items = ["Nemo", "NEMO", "nemo", "find", "nEMO"]
    print(task10(items = ["Nemo", "NEMO", "nemo", "find", "nEMO"]))

    print(task10(items = ['Maybe', 'you', None, 'Nemo', 'find', None]))