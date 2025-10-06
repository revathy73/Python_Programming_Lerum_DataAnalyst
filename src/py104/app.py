if __name__ == "__main__":

    """
    # create a variable
    country = "Panama"
    print(f"My conutry name is {country}")

    # collection of countries
    countries = ["Panama","Sweden","Spain","Portugal"]
    print(f"My favorite countries are {countries}")

    # Creating a list method1: []--symbol is here imporatnt
    capitals = ["Panama","Stockholm","Madrid", "Lisbon"]
    print(f"The capital of each country is {capitals}")

    Cap1 = ["Panama"] # If suppose am not giving list of capitals
    print(f"The capital of the country is {Cap1}")

    # Method2 : list(( )) --symbol is here imporatnt
    cities =  list(("colon", "Gbg", "Valencia", "Porto"))
    print(f"The cities from each country = {cities}")

    city2 = list(("Panama",)) # If suppose am not giving list of cities see here
    print(f"The city of the country is {city2}") ---> o/p : ('P','a','n','a','m','a')

    # Datatype we can store ---> String
    Language = ["ES", "Sv", "ES", "PT"]
    print(f"The languag eof the country is {Language}")

    # Float is also another datatype
    population = [4.3, 10.4, 45.0,10.7]
    print(f"The population of the countries are {population}")

    # Int
    currencies = [1,1,1,1]
    print(f"The no of the currencies per country = {currencies}")

    # how to add an element
    countries.append("italy")
    print(f"My updated country list is {countries}")

    countries.insert(2,"Norway")
    print(f"My country list after adding: {countries}")

    # Update a list
    countries[5] = "Italy"
    print(f"My updated country list is {countries}")

    # how to delete an item from the list
    countries.append("Venus")
    countries.append("Mars")
    print(f"My updated country list is {countries}")

    del countries[7]
    countries.remove("Venus")
    print(f"My updated country list is after deleting {countries}")
    
    """

    country_2 = ["Panama", "sweden", "norway"]
    # 1: Indices start at 0
    # 2: Access operator is used to access elements
    # 3: Access operator only accepts integers
    print(f"My first element in the list is {country_2[0]}")
    print(f"My first element in the list is {country_2[1]}")
    print(f"My first element in the list is {country_2[2]}")

    # 4: you can get an exception by trying to access  the wrong index
    # print(f"My first element in the list is {countries_2[3]}")

    # 5: access element from behind
    print(f"My first element in the list is {country_2[-1]}")
    print(f"My first element in the list is {country_2[-2]}")
    print(f"My first element in the list is {country_2[-3]}")

    # Relationship between the size of the List and the last index
    # last_index =  size of the list -1
    size_of_list = len(country_2)
    last_index = size_of_list -1
    print(f"The size of the list is {size_of_list}")
    print(f"The last index = {last_index}")
    print(f"The last element = {country_2[last_index]}")









