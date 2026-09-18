"""
You are given the variables a and b. Create a map called result whose keys
go from a to b, inclusive.

Each value is double its key whenever the key is an even number. Otherwise,
the value is triple the key when the number is odd.

In case a >= b, set result to be an empty map.

Example Solution
Assume that
a is 1
b is 3
Then
result is
{1 to 3, 2 to 4, 3 to 9}
"""
from to_do import TODO


def guide1(a: int, b: int) -> dict[int, int]:
    """
    # solution Method: 1
    if a >= b:
        return {}

    result = {}
    for number in range(a, b + 1):
        if number % 2 == 0:
            result[number] = number * 2
        else:
            result[number] = number * 3

    return result

    # solution method: 2 (ternary operator)
    if a >= b:
        return {}

    result = {}
    for number in range(a, b + 1):
        result[number] = number * 2 if number % 2 == 0 else number * 3

    return result

    # Dictionary comprehension
    if a >= b:
        return {}

    result = {}
    result = {number : number * 2 if number % 2 == 0 else number * 3 for number in range(a, b+1)}
    return  result
    """
    if a >= b:
        return {}

    return {number : number * 2 if number % 2 == 0 else number * 3 for number in range(a, b + 1)}

if __name__ == "__main__":

    # a = 1, b = 3  ---> {1 : 3, 2 : 4, 3 : 9}
    print(guide1(a = 1, b = 3))

    # a = 2, b = 5  --> {2 : 4, 3 : 9, 4 : 8, 5 : 15}
    print(guide1(a = 2, b = 5))

    # a = 20 , b = 10  ---> {}
    print(guide1(a = 20 , b = 10 ))


