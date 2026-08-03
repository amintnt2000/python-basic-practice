class BankAccount:
    def __init__(self, owner,   balance=0):
        self.owner = owner
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("موجودی نمی‌تونه منفی باشه")
        else:
            self._balance = value
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if amount > self._balance:
            print("موجودی کافی نیست")
        else:
            self._balance -= amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return f" حساب {self.owner} با موجودی {self._balance}"


