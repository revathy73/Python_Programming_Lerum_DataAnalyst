"""
Create a class called Account that satisfies the following requirements:

1. The class has one attribute called balance:

balance is of type Double
It represents the initial balance of the account
The attribute can be read but not modified from outside the class
The initial value is provided through the constructor
2. A method called deposit

Contains one parameter of type Double
The parameter represents the amount to be deposited
The method can be executed from outside the class
The method increases the bank account’s balance
The method does not return any value
3. A method called withdrawal

Contains one parameter of type Double
The parameter represents the amount to be withdrawn
The method decreases the bank account’s balance only if there is enough money available
The method does not return any value
The method can be executed from outside the class
4. A method called fee

No parameters
The method decreases the bank’s balance by 5%
The method does not return any value
The method can be executed from outside the class
"""
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

    """
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
        """

