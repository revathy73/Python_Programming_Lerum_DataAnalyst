from to_do import TODO


def guide10(companies: list[str]) -> list[str]:
    """
    # solution 1:
    result = []

    for company in companies:
        if company is None:
            continue

        new_name = ""
        for index,letter in enumerate(company):
            if index % 2 == 0:
                new_name += letter.upper()
            else:
                new_name += letter.lower()

        result.append(new_name)

    return result
    """
    #solution 2: (Ternary operator)
    result = []

    for company in companies:
        if company is None:
            continue

        new_name = ""
        for index, letter in enumerate(company):
            new_name += letter.upper() if index % 2 == 0 else letter.lower()

        result.append(new_name)

    return result
