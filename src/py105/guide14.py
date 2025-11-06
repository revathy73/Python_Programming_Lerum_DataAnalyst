from to_do import TODO


def guide14(scandinavia: dict[str, str]) -> dict[str, str]:

    scand_countries = ["denmark", "norway", "sweden", "finland", "iceland",
                       "faroe Islands", "greenland", "åland"]

    result = {}
    for country,language in scandinavia.items():
        if country.lower() in scand_countries:
            result[country] = language

    return result

if __name__ == "__main__":

    # scandinavia = {"Sweden":"sv","Norway":"no","Panama":"es"}
    print(guide14(scandinavia = {"Sweden":"sv","Norway":"no","Panama":"es"}))
