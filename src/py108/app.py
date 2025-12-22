from logging import exception

if __name__ == "__main__":
    """
    class Dog:  # This is basic definition of a class
        pass  # these tw0 lines are class definition

    # creating instances of a class
    firulais = "Dog()"   # these two lines are class instances
    fibi = Dog()

    print(type(firulais))  #output < class 'str'>

    firulais = 10.0  #output < class 'float'>
    fibi = Dog()
    
    # syntax rule : classname
    # 1. does not begin with number like class 1Dog() --> this is wrong
    # correct Method -- > ** only use letters for ex--> class Dog
    # we can also use underscores nad numbers ex: --> class Dog_ or class Dog_1
    # numbers not be in the beginning

    # Formatting Rule : classname
      # FR.1: classname must be begin with capital letter ex: class Dog:
      # FR.2: compound words are capitilaized PASCAL CASE ex: class AlienDog

    # How do we define attributes of a class? --> using variables
    class Dog: #It is just a template
        # Constructor
        def __init__(self, name, breed, age):
            self.name = name
            self.breed = breed
            self.age = age

    # We use the template to create instance of the class

    firulais = Dog(name = "firulais", breed = "Bulldog", age = 1)
    fibi = Dog(name = "fibi", breed = "Labrador", age = 2)
    fabi = Dog(name = "fabi", breed = "Mini Bulldog", age = 3)
    # firulais, fibi, fabi are object.because they represent the instances of the class

    print("--------")

    print(firulais.name)
    print(firulais.breed)
    print(firulais.age)
    print(fibi.name)
    print(fibi.breed)
    print(fibi.age)
    print(fabi.name)
    print(fabi.breed)
    print(fabi.age)

    # Methods of a class
    class Dog:
        def __init__(self,name,breed,age):
            self.name = name
            self.breed = breed
            self.age = age

        def bark(self):
            print(f"{self.name} is barking: whoof whoof")

        def sleep(self):
            self.bark()
            self.bark()
            self.bark()
            print(f"{self.name} is sleeping: ZZZZZzzzZZZ")
   
    # Inheritance>
    # parent class or super class
    class Animal:
        planet = "Earth"
        def __init__(self,name,breed,age):
            self.name = name
            self.breed = breed
            self.age = age
            self.owner = ""

        def sleep(self):
            print(f"{self.name} is sleeping: ZZZZZzzzZZZ")

        def move(self):
            print(f"{self.name} is moving")

    # child class or sub class
    class Dog(Animal): #Dog extended or inherited from the animal
        def __init__(self, name, breed, age, barking_level):
            super().__init__(name, breed, age)
            self.barking_level = barking_level

        def bark(self):
            print(f"{self.name} is barking: whoof whoof")

        def sleep(self):
            self.bark()
            super().sleep()

    # child class or sub class
    class Cat(Animal): #Cat extended or inherited from the animal
        def meow(self):
            print(f"{self.name} is meowing: meow meow")

        def move(self):
            self.meow()
            super().move()

    fibi = Dog(name="Fibi",breed="labrador",age=2, barking_level=5)
    print(fibi.name)
    print(fibi.breed)
    print(fibi.age)
    fibi.bark()
    fibi.sleep()
    fibi.move()

    mimi = Cat("Mimi","Bengal", 2)
    mimi.meow()
    mimi.move()
    mimi.sleep()
    """
    #own exceptions (Inheritance playing role in exception)
    class UnderageError(Exception):
        pass

    class Unkownageerror(exception):
        pass

    age = 17
    if age < 18:
        raise UnderageError("You are underage, you cannot drive")
    elif age == None:
        raise Unkownageerror("we cannot determine age, you cannot drive")












