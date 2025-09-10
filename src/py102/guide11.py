from to_do import TODO


def guide11(sales: str) -> str:
    # Input sales as scandinavia countries
    # Find out first five sales

    result = sales[0:5]
    return result

if __name__ == "__main__":

    # sales = DFNISFD --> DFNIS
    print(guide11(sales = "DFNISFD"))

    # sales = FNSDFIN --> FNSDF
    print(guide11(sales = "FNSDFIN"))


    # sales = SNDIFIF --> SNDIF
    print(guide11(sales = "SNDIFIF"))