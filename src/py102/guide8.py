from to_do import TODO


def guide8(sales: str) -> str:

    # Input sales as Scandinavia countries
    # Find out first index from sales input

    result = sales[0]
    return result

if __name__ == "__main__":

    # sales = SDIINFF --> S
    print(guide8(sales = "SDIINFF"))

    #sales = DFSNI --> D
    print(guide8(sales = "DFSNI"))

    #sales = NFSDIS --> N
    print(guide8(sales="NFSDIS"))

    #sales = FSDNII --> F
    print(guide8(sales="FSDNII"))

