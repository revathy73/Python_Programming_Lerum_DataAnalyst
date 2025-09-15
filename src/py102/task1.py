from to_do import TODO


def task1(country: str, capital: str, currency: str) -> str:
    # Input country,Capital and currency
    # Get the result using String function

    result = f"The capital of {country} is {capital}. They use the {currency}"
    return result

if __name__ == "__main__":

    # country = INDIA, capital = DELHI, currency = RUPEES
    print(task1(country = "INDIA", capital = "DELHI", currency ="RUPEES"))