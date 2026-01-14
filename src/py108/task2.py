class Account:

    def __init__(self,balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount) -> float:

        if amount > 0:
            self.balance += amount
        else:
            self.balance += 0

    def withdrawal(self, amount) -> float:

        if amount in range (0, self.balance +1):
            self.balance -= amount
        else:
            self.balance -= 0

    def fee(self):

        fee = self.balance * 0.05
        self.balance = self.balance - fee

if __name__ == "__main__":

    revathy = Account(1000)
    revathy.deposit(-300)
    revathy.withdrawal(5000)
    revathy.withdrawal(200)
