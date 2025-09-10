from to_do import TODO


def guide7(country: str, capital: str) -> str:

    # Create sentence using string
    # Output the sentence
    result = f"The capital of {country} is {capital}"
    return result

if __name__ == "__main__":

     # country = India, capital = Delhi
     print(guide7(country = "India", capital = "Delhi"))

     #country = Australia,capital = Sydney
     print(guide7(country= "Australia", capital = "Sydney"))