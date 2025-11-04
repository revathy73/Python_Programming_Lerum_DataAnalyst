from to_do import TODO


def guide5(universities: dict[str, str]) -> dict[str, str]:
    """
    # solution : For loop
    result = {}

    for university,country in universities.items():
        result[country] = university

    return result
    """
    # solution : Dictionary comprehension
    result = {country : university for university, country in universities.items()}
    return  result


if __name__ == "__main__":

    # {"UTP" to "Panama","KTH" to "Sweden","MIT" to "USA"} --> {"Panama" : "UTP","Sweden" : "KTH","USA" :"MIT"}
    print(guide5({"UTP":"Panama","KTH":"Sweden","MIT":"USA"}))

    print(guide5({"a":"A", "b":"B", "c":"C"}))