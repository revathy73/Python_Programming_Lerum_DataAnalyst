"""
You are given a variable called items, which represents a collection of numbers.

Multiply the first, third, fifth, and last elements of the collection. Save your result in a variable called result

In case the variable items has less than five elements, set result to be -1

Example Solution
Assume that
items is [1,2,3,4,5,6]
Then
result is 90
"""

from pkgutil import iter_modules

from to_do import TODO


def guide1(items: list[int]) -> int:

    if len(items) <= 5:
        return  -1

    first_element = items[0]
    third_element = items[2]
    fifth_element = items[4]
    last_element = items[-1]

    result = first_element * third_element * fifth_element * last_element
    return result

if __name__ == "__main__":

    # items = [1,2,3,4,5]
    print((guide1(items=[1,2,3,4,5])))

    # items = [1,2,3,4,5,6]
    print((guide1(items=[1,2,3,4,5,6])))

    # items = [1,2,3]
    print((guide1(items=[1,2,3])))




