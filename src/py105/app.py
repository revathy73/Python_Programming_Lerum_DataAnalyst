if __name__ == "__main__":

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

    # add:
    tax_office_3[999] = "LOla"
    print(tax_office_3)





