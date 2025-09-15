from to_do import TODO


def task2(name: str, country: str, month: str) -> str:

    # Input name, country, month
    # Output make the sentence with String function
    result = f"Hello {name}, you are from {country} and you were born in {month}"
    return result


if __name__ == "__main__":

    # name = "Ria", country= "Korea", month = "October"
    print(task2(name = "Ria", country = "Korea", month = "October"))