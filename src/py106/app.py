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
    # Syntax error
    """
    name = "Sweden"
    print(name)
    # ----- Syntax error ------
    # --> do not follow the syntax rules of the python language
    name "Sweden"  ---> here syntax error without equal sign
    print(name     ---> here syntax error without equal closing bracket
   ------------------- 
    # Index error
    letters = ["a","b","c"]
    print(letters[0])
   
    print(letters[10]) --> trying to access an element at a position that does not exist
    -----------------------------
    # Key error : Tyring to access a value for a key that does not exist
    data = {"one" : 1, "two": 2, "three":3}
    print(data["four"])
    # ZeroDivision Error: trying to divide a number by 0
    print(10/0)
    
    # Logical error:
    # the program finishes executing successfully but does not provide the expected behavior/desired output
    print("---START-----")
    countries =["Panama","Sweden","Norway"]
    print(countries[1])
    print("-----END-----")
   
    # Runtime error:
    # The program begins executing but stops abruptly before successfully completing the execution
    print("---START-----")
    single_error()
    print("-----END-----")
    
    # 1.ZeroDivision error
    print(1/0)
    
    # 2. Key error
    print("-----START-----")
    data = {"1":1}
    print(data["2"])
    print("----END-----")
   
    # 3. Index error --> list index out of range
    data = [2, 5, 6, 7]
    print(data[5])
    
    # Compile time error: The program does not even start executing
    # syntax error
    print("--- START-----")
    name "Humberto"
    print(name)
    print("---END----")
    
    # Runtime error with example: -- Single error
    print("----START------")
    try:
        provided_filename = input("Enter a filename:")
        get_file_details(filename = provided_filename)
        print("Finished with the try")
    except FileNotFoundError:
        print("Unable to get file details")

    print("----END----")

    # Runtime error with example: -- Multiple error
    print("----START------")
    try:
        user_password = input("Provide a password:")
        create_password(password=user_password)
        print("Finished with the try")
    except AssertionError:
        print("Please is too short, provide a longer password")
    except NameError:
        print("Password is too common, please use a more creative password")
    except SystemError:
        print("We have a problem on the server. Please try again while we fix it")
        
    except:
          print("try again") --- when we are creating a software this 
          will not be a user friendly method. Try before code
  
    print("----END----")
   
    # else and Finally Block
    print("----START----")
    try:
        provided_file_name = input("Please provide a filename:")
        print("*** Open Database ***")
        get_file_details(filename = provided_file_name)
    except FileNotFoundError:
        print("Failure: Unable to get details")
    else:
        print("Logging: Operation completed without any problems")
    finally:
        print("*** close database ***")

    print("--- END ---")
    
    # assert keyword:To make sure that conditions are true otherwise stop the app
    user_age = int(input("What is your age?"))

    assert(user_age > 17)

    print("You are an adult")
   
    # 'raise' keyword: Manually trigger an exception
    Syntax: raise [ExceptionType]([optional_message])
    filenames = ["app.py","run.py","main.py"]
    user_filename = input("Provide me with a filename:")
    if user_filename not in filenames:
        raise FileNotFoundError(f"The file {user_filename} was not found")
    else:
        print("The file was found")
    
    # another method: assert
    # SYNTAX :: assert condition, optional_message
    filenames = ["app.py","run.py","main.py"]
    user_filename = input("Provide me with a filename:")

    assert(user_filename in filenames)
    print("The file was found")

    # NULL POINTER EXCEPTION:
    countries = []
    print(countries)
    print(len(countries))
    print(type(countries))
    print("-------------")
    """
    names = []
    print(names)
    print(type(names))
    #print(names[0])
    #print(len(names))
    #print( 3 * none)

    countries1 = ["sweden","Norway", None, "Norway",None]

    if names is None:
        print("names in None")
    else:
        print(f"names is not None and has a length of {len(names)}")



        












