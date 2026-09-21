"""
You are given a list called names.

Determine how many times each name appears in the list.

Save your result in a variable called result

Example Solution
Assume that
names is
["Anna", "Anja", "Mary", "Anna"]
Then
result is
{
    "Anna" to 2,
    "Anja" to 1,
    "Mary" to 1
}
Notes
Your result must be case sensitive
"""

from to_do import TODO


def guide10(names: list[str]) -> dict[str, int]:

    """
    # solution 1: for loop
    result = {}
    for name in names:
        if name in result:
            result[name] = result[name] + 1
        else:
            result[name] = 1

    return result

    # solution 2: Ternary operator
    result = {}
    for name in names:
        result[name] = result[name] + 1 if name in result else 1

    return  result

    # solution 3: no control flow
    result = dict()
    for name in names:
        result[name] = result.get(name, 0) + 1

    return result
    """
    # solution 4: count() method
    result = {}
    for name in names:
        if name not in result:
            result[name] = names.count(name)

    return result


if __name__ == "__main__":

    # names = ["Anna", "Anja", "Mary", "Anna"]
    print(guide10(names =["Anna", "Anja", "Mary", "Anna"]))

    # names = ["Elpida","Alva","Devi","Saran"]
    print(guide10(names = ["Elpida","Alva","Devi","Saran"]))
