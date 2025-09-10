from to_do import TODO


def guide6(firstname: str, lastname: str) -> str:

    # Input for fistname and lastname
    # Concatenate the string in the desire sentence
    result = "Hello " +firstname+ " " +lastname+ ". Welcome to programming"
    return result

if __name__ == "__main__":

    #firstname=Revathy, lastname =perry, welcome to programming
    print(guide6(firstname = "Revathy", lastname = "perry"))

    #firstname=Maria , lastname = John, Welcome to programming
    print(guide6(firstname = "Maria", lastname = "John"))
