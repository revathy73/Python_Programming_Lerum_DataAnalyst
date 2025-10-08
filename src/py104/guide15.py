from to_do import TODO


def guide15(items: tuple[str]) -> bool:
    """
    size_of_items = len(items)

    last_element = items[-1]
    middle_index = int(size_of_items / 2)

    middle_element = items[middle_index]

    return len(middle_element) == len(last_element)
    """

    size_of_items = len(items)
    len_of_last_element = len(items[-1])
    #print(len_of_last_element)

    middle_index = int(len(items) / 2)
    #print(len(items[middle_index]))

    return len(items[middle_index]) == len_of_last_element


if __name__ == "__main__":
    # items = ["John","Jane","Roberto","Mary","Persona"]
    print(guide15(items = ("John","Jane","Roberto","Mary","Persona")))

    print(guide15(items = ("John","Jane","jade","Mary","Persona")))