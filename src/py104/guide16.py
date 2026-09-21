"""
You are given the variable called items, which represents the names of
students.

Identify all the students whose names start with the letter H.

Example Solution
Assume that
items is
[
    "Elena",
    "Helen",
    "Humberto",
    "John",
    "Henry"
]
Then
result is
["Helen", "Humberto", "Henry"]
Notes
Your solution cannot be case-sensitive
"""

from to_do import TODO


def guide16(items: tuple[str]) -> list[str]:
    """
    # solution 1: for loop no ternary operator
    result = []
    for name in items:
        first_letter = name[0]
        if first_letter.lower() == 'h':
            result.append(name)

    return result

    # solution 2: List comprehension
    result = [name for name in items if name[0].lower() == 'h']
    return result

    # solution 3: List comprehension (Refactoring)
    return [name for name in items if name[0].lower() == 'h']

    # solution 3: filter a list
    result = filter(lambda name: name[0].lower() == 'h', items)
    return list(result)
    """
    # solution 3: Transform a list (Refactoring)
    return list(filter(lambda name: name[0].lower() == 'h', items))


if __name__ == "__main__":

    # items = ("divya", "Revathy" ,"Harini")
    print(guide16(items = ("divya", "Revathy" ,"Harini")))


