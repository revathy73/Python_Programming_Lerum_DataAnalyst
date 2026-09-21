"""
You are given the lists a and b. Create a map in which the keys are the
items in a and the values are the items in b.

Save your result in a variable called result.

Example Solution
Assume that
a is [1, 2, 3, 4]
b is ["W", "X", "Y", "Z"]
Then
result is
{
    1 to "W",
    2 to "X",
    3 to "Y",
    4 to "Z"
}
Notes
Assume that a and b will always be of the same size.
Use conditional statements and loops in your solution.
"""

from pygments.unistring import combine

from to_do import TODO


def task12(a: list[int], b: list[str]) -> dict[int, str]:

    result = {}
    for index,number in enumerate(a):
        #for index2, letter in enumerate(b):
            #a[index1] = b[index2]
            result[number] = b[index]

    return result

    """
    result = {}
    for number in range(a , b):
        result[a[number]]  = b[number]

    return result
    
    cost = supermarket.get(item, 0.0)
        result += cost
    """

if __name__ == "__main__":

    # a = [1, 2, 3, 4] ,b = ["W", "X", "Y", "Z"]
    print(task12(a = [1, 2, 3, 4] ,b = ["W", "X", "Y", "Z"]))
