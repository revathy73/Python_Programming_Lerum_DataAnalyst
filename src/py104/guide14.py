"""
You are given a variable called items, which represents a collection of
numbers.

Access the number located in the middle of the collection. Save the result
in a variable called result.

Example Solution
Assume that
items is [1, 5, 7, 9, 10]
Then
result is 7
Notes
Assume that items will always have a clear middle number.
"""

from to_do import TODO


def guide14(items: tuple[int]) -> int:

   length_of_items = len(items)
   middle_index = int(length_of_items / 2)
   middle_element = items[middle_index]

   return middle_element

if __name__  == "__main__":

    # items = [3,7,5,1,9]
    print(guide14(items = (3,7,5,1,9)))

    print(guide14(items = (3, 8, 4)))


