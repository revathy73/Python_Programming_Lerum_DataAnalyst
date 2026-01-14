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



