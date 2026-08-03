from bank_account import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
    def withdraw(self, amount):
        penalty = amount * 0.1
        total = penalty + amount
        if total > self.balance:
            print("موجودی کافی نیست")
        else:
            self.balance -= total
    def __str__(self):
        base = super().__str__()
        return f"{base} و نرخ سود {self.interest_rate}"

