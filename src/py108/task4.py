"""
Create a class called Hero that satisfies the following requirements:

1. The class has two attributes of type Int:

health with an initial value of 10
level with an initial value of 0
All attributes can be read but not modified from outside the class
2. A method called sick

No parameters
The method does not return any value
The method can be executed from outside the class
Reduces health by 1
3. A method called heal

No parameters
The method does not return any value
The method can be executed from outside the class
Increases health by 1
4. A method called attack

No parameters
The method does not return any value
The method can be executed from outside the class
Increases level by 1
"""
class Hero:

    def __init__(self):
        self.health = 10
        self.level = 0

    def get_health(self):
        return self.health

    def get_level(self):
        return self.level

    def sick(self):
        self.health -= 1
        return self.health

    def heal(self):
        self.health += 1
        return self.health

    def attack(self):
        self.level += 1
        return self.level

if __name__ == "__main__":

    john = Hero()
    john.sick()
    john.heal()
    john.attack()



