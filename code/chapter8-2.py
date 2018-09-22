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

    def transfer(self, to, amount):
        if not isinstance(to, BankAccount):
            return "invalid to user"

        # 涉及锁, 回滚
        if amount > self.getBalance():
            return "balance not enough"

        self.withdrow(amount)
        to.topup(amount)

        return "success"


sam = BankAccount("Sam", 1000)
sam.topup(500)
sam.withdrow(1200)
balance = sam.getBalance()
print("Balance %s" % (balance))

jem = BankAccount("Jem", 120)
sam.transfer(jem, 80)
print("Balance Sam %s" % (sam.getBalance()))
print("Balance Jem %s" % (jem.getBalance()))
