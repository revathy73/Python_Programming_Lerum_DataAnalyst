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


