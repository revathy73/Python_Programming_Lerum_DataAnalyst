"""
You are given the numbers a and b.

The solution to the task is given, but such a solution has a number of errors.
Debug the code so that the correct behavior is produced.

The expected behavior is to create a map in which the keys go from a to b
inclusive. For each key, the value is an inner map containing two keys, one
called multiplication and another called summation.

The value for the key multiplication is a list with the result of multiplying
the numbers 1 to 5 by the key. The value for the key summation is a list with
the result of adding the numbers 1 to 5 by the key.

In case a is equal to or greater than b, then the result of {0:0} is expected.

Example Solution
Assume that
a is 1
b is 3
Then
result is
{
    1: {
        "multiplication":[1, 2, 3, 4, 5],
        "summation": [2, 3, 4, 5, 6]
    }
    2: {
        "multiplication": [2, 4, 6, 8, 10],
        "summation": [3, 4, 5, 6, 7]
    }
    3: {
        "multiplication": [3, 6, 9, 12, 15],
        "summation": [4, 5, 6, 7, 8]
    }
}
"""
def guide8(a: int, b: int) -> dict[int, dict[str, list[int]]]:

    if a >= b:
        return {0:0}

    result = {}
    for number in range(a, b + 1):
        result[number] = {
            "multiplication" : [number * integer for integer in range(1, 6)],
            "summation" : [number + integer for integer in range(1, 6)]
        }

    return result

if __name__ == "__main__":

    print(guide8(a=1, b=3))
    #print(guide8(a=10, b=3))
