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

        # countries = ["sweden","norway"]
        print(guide3(items=["sweden", "norway", "finland"]))

        # countries = [] ---> -1
        print(guide3(items=[]))
