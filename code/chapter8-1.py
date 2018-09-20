# -*- coding: UTF-8 -*-


class BankAccount():
    def __init__(self, username, balance):
        self.__username = username
        self.__balance = balance

    def getUsername(self):
        return self.__username

    def getBalance(self):
        return self.__balance

    def topup(self, amount):
        if type(amount) is not int:
            return False

        if amount <= 0:
            return False

        self.__balance += amount
        return True

    def withdrow(self, amount):
        if type(amount) is not int:
            return False

        if amount > self.__balance:
            return False

        self.__balance -= amount
        return True


sam = BankAccount("Sam", 1000)
sam.topup(500)
sam.withdrow(1200)
balance = sam.getBalance()
print("Balance %s" % (balance))
