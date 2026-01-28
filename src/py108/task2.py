class Account:

    def __init__(self,balance: float):
        self.__balance = balance

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float):

        if amount > 0:
            self.__balance += amount
        else:
            self.__balance += 0

    def withdrawal(self, amount: float):

        if amount in range (0, self.__balance + 1):
            self.__balance -= amount
        else:
            self.__balance -= 0

    def fee(self):

        fee = self.balance * 0.05
        self.__balance = self.balance - fee

if __name__ == "__main__":

    revathy = Account(1000)
    revathy.deposit(-300)
    revathy.withdrawal(5000)
    revathy.withdrawal(200)


    class Account:
        def __init__(self, balance: float):
            self.__balance = balance

        @property
        def balance(self) -> float:
            return self.__balance

        def deposit(self, amount: float):
            if amount > 0:
                self.__balance += amount
            else:
                print("Cannot deposit negative amount")

        def withdrawal(self, amount: float):
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient balance")

        def fee(self):
            self.__balance -= self.__balance * 0.05

