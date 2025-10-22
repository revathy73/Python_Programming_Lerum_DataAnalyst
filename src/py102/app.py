import math
if __name__ == "__main__":

    """
    new_sentence = "I want to watch the movie \"Avengers\""
    print(new_sentence)

    new_sentence_2 = 'I want to watch the movie \"Avengers\"'
    print(new_sentence_2)

    sentence3 = "I don't know the answer"
    print(sentence3)

    sentence4 = "This is \ngoing in a\n new line"
    print(sentence4)
    
    sentence = "SWEDEN"

    first_letter = sentence[0]
    second_letter = sentence[1]
    last_letter = sentence[-1]
    second_to_last = sentence[-2]
    first3_letters = sentence[0:3]
    length_of_the_string = len(sentence)
    index_of_last_letter = len(sentence)-1
    last_letter_identify = sentence[index_of_last_letter]

    print(f"The first letter is {first_letter}")
    print(f"The second letter is {second_letter}")
    print(f"The last letter is {last_letter}")
    print(f"The second letter from last is {second_to_last}")
    print(f"The first three letter is {first3_letters}")
    print(f"The string length is {length_of_the_string}")
    print(f"The last letter index is {index_of_last_letter}")
    print(f"The last letter is {last_letter_identify}")

    # Syntax Rule #1: Var names can contain letter, numbers and underscores
    name = "Revathy"
    country = "India"
    language = "Tamil"
    age = 35
    course = "Data Analyst"

    # Method 1 : Ugly method string concatenation
    sentence = "Hello " +name+ " you come from " +country+ " and you speak " +language
    print(sentence)

    # Method 2 : f-string (f = format)
    new_sentence = f"Hello {name} you come from {country} and you speak {language}"
    print(new_sentence)

    # Syntax Rule #2: Var names cannot begin with a number
    # 2nd_number = "Olivia"

    # Syntax Rule #3: Var names cannot have spaces
    # course study = "Data Analyst"

    #Synatax Rule #4: Var names cannot have special characters
    #rupee_$ = sek / 8

    # Syntax Rule #5:  Var name cannot have be a reserved keyword
    # Reserved Keyword: if else break continue in for while def is return
    # if = 40 but If = 40 accepted as a variable name
    # break = 60 but Break = 60 accepted as a variable name

    # Formatting Rule #1: Var names are in lower case
    COUNTRY = "Sweden"
    country = "Sweden"

    # Formatting Rule #2: Separate compound words with underscore
    myIDE = "Pycharm"
    my_ide = "Pycharm"

    # Recommendation: create names that are descriptive
    lt = 0.8923
    latitude = 0.8923

    # age = 30 instead of x = 30

    # Variable names are case sensitive
    # Parts of a variable creation
    
    place = "Panama"
    country = "sweden"
    print (country)
    print (country)
    
    #Integer 
    print (50)
    print (50+2)
    print (50-2)
    print (50*2)
    print (50/2)
    print (50**2)
    
    #Float 
    print(40.40)
    print(50*2)
    print(50+2)  
    print(50-2)
    print(50/2)
    print(50**2)
    
    #string
    print("Hello, This is a Data Analyst")
    Print('This is my first course in Python')
    
    name = input("> what is your name?")
    print("Your name is ---> " + name)
       
    sentence = "python"
    print(f"{sentence[-5:-1]}")

    sentence = "python"
    print(f"{sentence[-6:]}")
   
    sentence = "AaaBbbCccDdd"
    #print(f"{sentence[::1]}")
    #print(f"{sentence[::2]}")
    print(f"{sentence[::3]}")

    #print(f"{sentence[-6::2]}")
    #print(f"{sentence[-3:]}")
    
    print(f"{sentence[1::2]}")
    print(f"The Lenghth is : {len(sentence)}")
    
    new_sentence = "I want to watch the movie \"Avengers\""
    print(new_sentence)

    new_sentence_2 = 'I want to watch the movie \"Avengers\"'
    print(new_sentence_2)

    sentence4 = "This is \ngoing in a\n new line"
    print(sentence4)
    
    sentence = "SWEDEN"

    first_letter = sentence[0]
    second_letter = sentence[1]
    last_letter = sentence[-1]
    last_second_letter = sentence[-2]
    print(f"The first letter is {first_letter}")
    print(f"The second letter is {second_letter}")
    print(f"The last_letter is {last_letter}")
    print(f"The last_second_letter is {last_second_letter}")

    first3_letters = sentence[0:3]
    length_of_the_string = len(sentence)
    index_of_last_letter = len(sentence) - 1
    last_letter_identify = sentence[index_of_last_letter]

    print(f"The first3_letters is {first3_letters}")
    print(f"The length_of_the_string is {length_of_the_string}")
    print(f"The index_of_last_letter is {index_of_last_letter}")
    print(f"The index_of_last_letter is {index_of_last_letter}")

    name = input("> what is your name?")
    print("Your name is ---> " + name)
    
    sentence = "AaaBbbCccDdd"
    print(f"{sentence[::1]}")

    print(f"{sentence[-6::2]}")
    print(f"{sentence[-3:]}")

    print(f"{sentence[1::2]}")

    first3_letters = sentence[0:3]
    print(f"The first3_letters is {first3_letters}")
    
     # PRACTICE
    sentence = "Sweden"
    first_letter = sentence[0]
    second_letter = sentence[1]
    print(f"The first letter is: {first_letter}")
    print(f"The second letter is: {second_letter}")

    last_letter = sentence[-1]
    print(f"The last_letter is: {last_letter}")
    print(f"The second_last_letter is: {sentence[-2]}")

    first_3_letters = sentence[0:3]
    print(f"first three letters are: {first_3_letters}")
    last_3_letter = sentence[-3:]
    print(f"last three letters are : {last_3_letter}")

    print(f"last letters from without the last letter: {sentence[-3:-1]}")

    length_of_the_string = len(sentence)
    print(f"length of the string is: {length_of_the_string}")

    print(50**2) #---> square of 50
    
    # variable names can contain letter, numbers and underscores
    name = "Revathy"
    country = "India"
    language = "Tamil"
    age = 35
    course_study = "Data Analyst"

    print(name)
    print(country)
    print(language)
    print(age)
    print(course_study)
   
    # method:#  Ugly method string concatenation
    #     sentence = "Hello " +name+ " you come from " +country+ " and you speak " +language
    #     print(sentence)
    #
    # Method 2 : f-string (f = format)
    #     new_sentence = f"Hello {name} you come from {country} and you speak {language}"
    #     print(new_sentence)

    sentence11 = "Hello " +name+ " you come from " +country+ " and you speak " +language
    print(sentence11)

    sentence12 = f"Hello {name} you come from {country}"
    print(sentence12)

    name = input("> what is your name?")
    print("Your name is ---> " + name)

    country = input("> what is your name?")
    print("your name is ---> " + country)
    
    name = "Revathy"
    country = "India"
    print(name[0:3])   #--->
    print(name[-3:])   #--->
    print(name[-3:-1])  #--->

    print(name[0::2])    #--->
    print(name[0::3])    #--->
    print(name[0::1])    #--->
    
    sentence = "AaaBbbCccDdd"
    print(f"{sentence[::1]}")

    print(f"{sentence[-6::2]}")
    print(f"{sentence[-3:]}")

    print(f"{sentence[1::2]}")
    
    new_sentence = "I want to watch the movie \"Avengers\""
    print(new_sentence)

    new_sentence_2 = 'I want to watch the movie \"Avengers\"'
    print(new_sentence_2)

    sentence3 = "I don't know the answer"
    print(sentence3)

    sentence4 = "This is \ngoing in a\n new line"
    print(sentence4)
    
    sentence = "This is a \"data analyst\" course"
    print(sentence)

    sentence12 = 'This is a \"data analyst\" course'
    print(sentence12)
   
    name = "Revathy"
    print(name[-3::2])

    sentence = "AaaBbbCccDdd"
    print(f"{sentence[-6::2]}")

    text = "Sweden-Stockholm-SEK"
    text_components = text.split("-")
    print(text_components)

    country = text_components[0]
    capital = text_components[1]
    currency = text_components[2]

    print(f"{country}")
    print(f"{capital}")
    print(f"{currency }")

    sentence13 = "I LOve Python"
    print(sentence13)
    print(sentence13.strip())

    print(len(sentence13))
    print(sentence13.upper())
    print(sentence13.lower())

    result1 = 'I' in sentence13
    print(result1)
    result2 = 'l' in sentence13
    print(result2)
    print(sentence13.count('o'))
    print(sentence13.find('o'))
    print(sentence13.find('o'))
    print(sentence13.count('o'))
    
    sentence13 = "Python"
    print(sentence13.count('I'))
    print(sentence13[0:3])
    print(sentence13[-6:])

    print(sentence13[::-1])
    print(sentence13.isalpha())
    print(sentence13.isupper())
    print(sentence13.isdigit())
    print(sentence13.islower())
    print(sentence13.isascii())

    value1 = "12"
    value2 = "12.4"
    value3 = "-5"
    value4 = "abc12"
    print(f"{type(int(value1))}")
    print(f"{type(float(value2))}")
    """
    # str() ---> Convert a value to its text representation
    print(round(19.6))
    print(round(19.5))
    print(round(19.2))
    print(round(3.1429,2))

    number = str(14)
    decimal = str(12.9)
    boolean = str(True)

    print(f"{type(number)}")
    print(f"{type(decimal)}")
    print(f"{type(boolean)}")

    name = input("> what is your name?")
    print("Your name is ---> " , name)


    positive_infinity = math.inf
    print(f"{type(positive_infinity)}")
    print(positive_infinity > 1000)

    negative_infinity = math.inf
    print(f"{type(negative_infinity)}")
    print(negative_infinity < 1000)










