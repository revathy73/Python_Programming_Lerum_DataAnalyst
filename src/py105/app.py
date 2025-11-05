if __name__ == "__main__":
    """
    # create a dictionary
    # Method 1:
    swedish_tax_agency = {1234: "Bob", 5678: "Jane", 91011: "John"}
    print(f"There are {len(swedish_tax_agency)} people in sweden : {swedish_tax_agency}")
    print(type(swedish_tax_agency))

    # Method 2:
    panama_tax_agency = dict({321:"Ana", 987:"Maria", 675:"Jose", 777:"Juan"})
    print(f"There are {len(panama_tax_agency)} people in Panama : {panama_tax_agency}")
    print(type(panama_tax_agency))

    # what are the parts of a KV pair
    # KVP -> Entity, Entry, Item

    # what data types can be as keys and values?
    # str, int, float, boolean
    # dict{str, float}

    ######   Properties   #####
    # Properties of a dictionary
    # 1. Keys are unique
    tax_office_1 = {123: "Bob", 456: "Jane", 789: "Mary"}
    print(tax_office_1)

    # Values can be duplicated
    tax_office_2 = {123:"Bob", 456: "Bob", 789: "Mary"}
    print(tax_office_2)

    # prop: 3 --> A key can point to a single value
    tax_office_3 = {123: "Bob", 456: "Mary", 789: "Jane"}
    print(tax_office_3[456])

    # prop: 4 ---> KVP are changeable (add, remove, update KVP)
    # change
    tax_office_3[123] = "Robert"
    print(tax_office_3)

    # Remove
    del tax_office_3[456]
    print(tax_office_3)

    # add: using the accessor operator []
    tax_office_3[999] = "LOla"
    print(tax_office_3)

    # Update the function :
    tax_office = dict()
    print(tax_office)
    tax_office_3.update({999:"Pat"})
    print(tax_office_3)
    
    # How to access values in the dictionary:
    names = ["Jane", "Bob", "John"]
    print(names[2])
    
    tax_office_111 = {111: "Jane", 124: "Diva", 145: "Ury"}
    print(tax_office_111[124])

    print(tax_office_111.get(125,"N/A"))
   
    tax_office_123 = {"Sweden": "Europe","Panama":"America","Russia":"Asia"}
    print(tax_office_123["Sweden"])

    print(tax_office_123.get("Panama"))
    
    # Looping over the entries in List
    capitals = ["Panama", "Stockholm", "Madrid"]
    for capital in capitals:
        print(capital)
    
    # Looping over the entries in Dict?
    coding = {"kotlin":"kt","python":"py","Java":"java"}
    for entry in coding:
        print(entry)

    # Method 1: No unpacking
    # The element at position 0 is always the key
    # The element at position 1 is always the value
    for entry in coding.items():
        print(entry)
        print(f"languages are '{entry[0]}',the extension is '{entry[1]}'")
    # Method 2: Yes unpacking
    # The first variable is always the key
    # The first variable is always the value
    # You can call the variable whatever you want
    for language,extension in coding.items():
        print(f"For the language '{language}' the extension is '{extension}'")

    entries = coding.items()
    print(entries)
    print(type(entries))

    entries = list(coding.items())
    print(entries)

    coding["javascript"] = "js"
    print(entries)

    for language,extension in entries:
        print(f"{language} ---> {extension}")

    entries = list(coding.items())
    # ---> want to prevent from updating in dictionary change to list
    print(entries)

    coding["wcs"] = "c#" # It is not updated here bcoz, changed to list
    print(entries)
    
    initials = {"A":"Adam","B":"Bob","C":"Carol"}
    # Access the collection of keys
    keys_of_dict = initials.keys()
    print(keys_of_dict)

    initials["H"] = "Humberto"
    print(keys_of_dict)
    print(type(keys_of_dict))
    """
    coding = {"kotlin":"kt","python":"py","Java":"java"}
    keys_of_code = list(coding.keys())
    coding["c#"] = "wcp" # ---> we cant update here directly bcoz,it is changed list
    print(keys_of_code)

    # Looping over the keys: using a variable
    keys = coding.keys()
    for key in keys:
        print(key)

    # looping 2 # Inline
    for key in coding.keys():
        print(key)

























