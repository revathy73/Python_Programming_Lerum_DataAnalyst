from to_do import TODO


def guide10(sales: str) -> str:
    # Input sales as Scandinavia countries
    # Find out last sale of Input

    result = sales[-1]
    #result = sales[len(sales)-1]
    return result

if __name__ == "__main__":

    # sales = SDNFISD --> D
    print(guide10(sales = "SDNFISD"))

    # sales = DNFSIDS --> S
    print(guide10(sales = "DNFSIDS"))

    # sales = NFSDIFN --> N
    print(guide10(sales = "NFSDIFN"))

    # sales = FSDISIF --> F
    print(guide10(sales ="FSDISIF"))
