import datetime
#import pytz


class Account:
    """ A sipmle account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return utc_time

    def __init__(self, name, balance):
        self._name = name
        self.__balance = 0
        self._transaction_list = []
        print("account created for " + self._name)
        self.deposit(balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Ammount must be greater then zero and no more then your account balance")
        self.show_balance()


    def show_balance(self):
        print("Balance ks {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
            print("{:6} on {} (local time was)".format(amount, trans_type, date))

if __name__ == '__main__':
    tim = Account('Tim', 0)
    tim.deposit(1000)
    tim.withdraw(500)

    tim.show_transactions()

    steph = Account('Steph', 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()

    print(steph.__dict__)