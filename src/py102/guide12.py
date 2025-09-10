from to_do import TODO


def guide12(sales: str) -> int:
    # Input sales as scandinavia countries
    # Find out total number of sales per day

     result = len(sales)
     return result

if __name__ == "__main__":

    # sales = SDIFNDSI --> 8
    print(guide12( sales = "SDIFNDSI"))

    # sales = NFIDS --> 5
    print(guide12( sales = "NFIDS"))

    # sales = FSDINSF --> 7
    print(guide12(sales = "FSDINSF"))