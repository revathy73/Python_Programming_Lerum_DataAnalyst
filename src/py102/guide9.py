from to_do import TODO


def guide9(sales: str) -> str:

    # Input as Scandinavia countries
    # Find out fourth Indes os the Sales

    result = sales[3]
    return result

if __name__ == "__main__":

    # sales = DNFISI --> I
    print(guide9(sales = "DNFISI"))

    # sales = NFIDSI --> D
    print(guide9(sales = "NFIDSI"))

    # sales = IDFSID --> s
    print(guide9(sales = "IDFSID"))

    # sales = ISINDF --> N
    print(guide9(sales = "ISINDF"))

    # sales = DSNFII --> F
    print(guide9(sales = "DSNFII"))