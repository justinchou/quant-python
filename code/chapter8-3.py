# -*- coding: UTF-8 -*-


class BankAccount(object):

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


class CreditCardAccount(BankAccount):
    def __init__(self, username, balance, totalCredit):
        # BankAccount.__init__(self, username, balance)
        super(CreditCardAccount, self).__init__(username, balance)
        self.__totalCredit = totalCredit
        self.__usedCredit = 0
        self.__bill = []

    def getTotalCredit(self):
        return self.__totalCredit

    def getUseableCredit(self):
        return self.__totalCredit - self.__usedCredit

    def withdrow(self, amount):
        if amount <= self.getBalance():
            # BankAccount.withdrow(self, amount)
            super(CreditCardAccount, self).withdrow(amount)
            return True
        elif amount - self.getBalance() <= self.getUseableCredit():
            withdrowCredit = amount - self.getBalance()
            self.__usedCredit += withdrowCredit
            # BankAccount.withdrow(self, self.getBalance())
            super(CreditCardAccount, self).withdrow(self.getBalance())
            self.__bill.append(withdrowCredit)
            return True

        return False

    def getMyBill(self):
        bill = {"totalCredit": self.__totalCredit, "usedCredit": self.__usedCredit,
                "balance": self.getBalance(), "bill": self.__bill}
        return bill


sam = CreditCardAccount("Sam", 1000, 1800)

sam.withdrow(200)
print(sam.getMyBill())

sam.withdrow(1000)
print(sam.getMyBill())

sam.withdrow(800)
print(sam.getMyBill())

sam.withdrow(1000)
print(sam.getMyBill())
