if __name__ == "__main__":
    pass

    """
    # ------------- Syntax Rules of naming a function ----------- #
    # Syntax Rule 1: Function names can only contain letters, numbers and underscores
    def greetings():
        pass

    def greetings_spanish():
        pass

    def greetings_spanish_v2():
        pass

    # Syntax Rule 2: function names cannot begin with a number
    # def 1st_greetings():
    #     pass

    # Syntax Rule #3: function names cannot have spaces
    # def spanish greetings():
    #     pass

    # Syntax Rule 4: Function name cannot have special characters
    #def $panish_greetings():
        #pass

    # Function cannot contain a reserved keyword
    # def break():
    # pass

    # Syntax Rule #6: names are case sensitive
    def greet():
        pass

    def Greet():
        pass

    #----------------------- Formatting Rule ---------------------- #
    # Rule 1:
    def print_compount_name():
        pass

    # -- This is not use in Python. In other programming language people are using
    def printcompleteName(): # not following standard
        pass

    # Rule 2:
    def PRINT_DATA(): # not following standard
        pass # It will run but we should not

    def print_data():
        pass

    # Recommendation
    # Function names should express an action, an intention --- example
    def generate():
        pass

    def download_data(): # -- function for download data
        pass

    def show_data(): # -- function for showing data
        pass

    def calculate_area(): # -- calculate area for different shapes
        pass
        
    # passing parameters
    def area_of_circle(radius):
        area = 3.1416 * (radius ** 2)
        return area

    output_of_function1 = area_of_circle(1)
    output_of_function2 = area_of_circle(15)

    print(output_of_function1)
    print(output_of_function2)
   
    # passing parameters by position
    def counter_calculator(sentence, letter):
        print(f"> Sentence = {sentence}")
        print(f"> letter = {letter}")

    # 1)pass by position
    counter_calculator("Hello to python", "H")

    # 2)pass by name
    #counter_calculator(sentence="Hello to python", letter = "H")
    counter_calculator(letter="H",sentence="welcome to python")
    """
    # Parameters by default value
    def counter(sentence, letter = "H"):
        print(f"> sentence = {sentence}")
        print(f"> letter = {letter}")

    counter(sentence = "Hello to python", letter= "Z")
    counter(sentence= "Hello to python") # it assume the value







