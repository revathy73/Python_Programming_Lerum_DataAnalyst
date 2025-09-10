from to_do import TODO


def guide13(sales: str) -> bool:

    # Input sales as Scandinavia countries
    # Find out Denmark sell on the day

    result = 'D' in sales
    return result


if __name__ == "__main__":

    # sales = IFNDS ---> True
    print(guide13(sales = "IFNDS"))

    # sales = FSNIS --->  False
    print(guide13(sales = "FSNIS"))

    # sales = DFSDNI ---> True
    print(guide13(sales = "DFSDNI"))