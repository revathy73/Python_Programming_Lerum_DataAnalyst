from to_do import TODO


def guide14(sales: str) -> int:
    # Input as Scandinavia countries
    # Find out number sales in Sweden

    result = sales.count('S')
    return result


if __name__ == "__main__":

    # Sales = DSFSNII ---> 2
    print(guide14(sales = "DSFSNII"))

    # sales = NDFDIF ---> 0
    print(guide14(sales = "NDFDIF"))

    # sales = FSNID ---> 1
    print(guide14(sales = "FSNID") )