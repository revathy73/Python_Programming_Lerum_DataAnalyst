from to_do import TODO


def guide15(sales: str) -> int:
    # Input as scandinavia countries
    # Find out total number of sales in Sweden and Norway


    sweden_sales = sales.count("S")
    norway_sales = sales.count("N")
    result = sweden_sales + norway_sales
    return result

if __name__ == "__main__":

    # sales = DSFNISN ---> 4
    print(guide15(sales ="DSFNISN"))

    # sales = SDNFNI ---> 3
    print(guide15(sales ="SDNFNI"))

    # sales = DFIIFD ---> 0
    print(guide15(sales = "DFIIFD"))
