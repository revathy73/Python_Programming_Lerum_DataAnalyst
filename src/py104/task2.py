"""
You are given the variable items. Add all the elements that are located at an even index.

Save your result in a variable called result of type Int.

If items is empty, then set result to -1.
Example Solution
Assume that
items is [1, 2, 3, 4]
Then
result is 4
Hint
The elements 1 and 3 are located at an even index. So, 1 + 3 = 4
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO

def task2(items: list[int]) -> int:

    if not items:
        return  -1

    result = 0
    for index,item in enumerate(items):
        if index % 2 == 0:
            result = result + item

    return result

if __name__ == "__main__":

    # items = [1,2,3,4]
    print(task2(items = [1,2,3,4]))
