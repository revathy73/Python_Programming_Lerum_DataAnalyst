def single_error():
    raise KeyError


def create_password(password: str):
    if len(password) < 3:
        raise AssertionError("Password is too short")
    elif password == "qwerty":
        raise NameError("Invalid password name. Too Easy")
    elif password[0] == "q":
        raise SystemError("Unable to create password")
    else:
        print("Password created successfully")


def get_file_details(filename: str):
    if filename.lower() == "python":
        print(f"File Content --> Python is amazing")
    elif filename.lower() == "kotlin":
        print(f"File Content --> Kotlin is amazing")
    else:
        raise FileNotFoundError(f"'{filename}' was not found")


if __name__ == "__main__":
    pass
