"""
You are given a variable called items, which represents a collection of three grades. Find the highest grade of the three and save it in a variable called result.

In case items does not have exactly three elements, set the result to be -1

Example Solution
Assume that
items is [70, 80, 69]
Then
result is 80
Notes
Do not use any built-in function, like max(), to solve the problem.
Assume that no item appears more than once in the given list.
"""

from calendar import firstweekday

from to_do import TODO


def guide2(items: list[int]) -> int:

    if len(items) < 3 or len(items) > 3:
        return -1

    first_element = items[0]
    second_element = items[1]
    third_element = items[2]

    if first_element > second_element:
        if first_element > third_element:
            return first_element
        else:
            return third_element
    else:
        if second_element > third_element:
            return second_element
        else:
            return third_element

    # solution method :2
    #if first_element > second_element and first_element > third_element:
    #     return first_element
    #elif second_element > first_element and second_element >third_element:
    #    return second_element
    #else:
    #   return third_element

if  __name__ == "__main__":

    # items = [40, 45, 60]
    print((guide2(items=[40, 45, 60])))

    # items = [30, 10, 20]
    print((guide2(items=[30, 10, 20])))

    # items = [70, 80]
    print((guide2(items=[70, 80])))

    # items = [20, 10, 30]
    print((guide2(items=[30, 10, 20])))




