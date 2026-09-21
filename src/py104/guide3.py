"""
You are given a variable called items, which represents a collection of countries.

Multiply the index of the last element by the length of the first country. Save your result in a variable called result

In case the variable items has no countries, set result to be -1

Example Solution
Assume that
items is
["Sweden", "Norway", "Italy", "Panama"]
Then
result is 18
Notes
Do not use any built-in function, like indexOf(), to solve the problem.
"""

from operator import index

from to_do import TODO


def guide3(items: list[str]) -> int:

    if len(items) == 0:
        return -1

    size_of_the_countries = len(items) - 1
    first_element = items[0]
    length_first_element = len(first_element)
    return size_of_the_countries * length_first_element
    # length_first_element = len(items[0])
    # return (len(items) - 1) * len(items[0])

if __name__ == "__main__":

        # countries = ["sweden","norway"]  ---> 6 * 2 = 12
        print(guide3(items=["sweden", "norway", "finland"]))

        # countries = [] ---> -1
        print(guide3(items=[]))
