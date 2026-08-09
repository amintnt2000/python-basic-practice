class InsufficientFundsError(Exception):
    pass
class InvalidAmountError(Exception):
    pass

class Account:
    def __init__(self, owner_name, account_number):
        self.owner_name = owner_name
        self.account_number = account_number
        self._balance = 0
        self.transaction_history = []
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        else:
            self._balance = value
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        else:
            self._balance += amount
            self.transaction_history.append(f"Deposit:{amount}")
    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            raise InvalidAmountError("The withdrawal cannot be negative.")

        else:
            self._balance -= amount
            self.transaction_history.append(f"Withdraw:{amount}")
    def __str__(self):
        return f"Owner name:{self.owner_name}, Account id:{self.account_number} , Account balance:{self._balance}"
class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_number = 1
    def create_account(self, owner_name):
        new_account = Account(owner_name, self.account_number)
        self.accounts[self.account_number] = new_account
        self.account_number += 1
        return new_account
    def find_account(self, account_number):
        if account_number not in self.accounts:
            return None
        else:
            return self.accounts[account_number]
    def transfer(self, from_account_number, to_account_number, amount):
        if not self.find_account(from_account_number):
            raise ValueError("Account not exist.")
        elif not self.find_account(to_account_number):
            raise  ValueError("The destination account does not exist.")
        else:
            self.find_account(from_account_number).withdraw(amount)
            self.find_account(to_account_number).deposit(amount)


bank = Bank()

# ساخت دو حساب
acc1 = bank.create_account("Ali")
acc2 = bank.create_account("Sara")

# واریز اولیه
acc1.deposit(1000)
print(acc1)  # Owner: Ali, balance: 1000

# انتقال موفق
bank.transfer(acc1.account_number, acc2.account_number, 300)
print(acc1)  # balance: 700
print(acc2)  # balance: 300

# انتقال با موجودی ناکافی -> باید خطا بده
try:
    bank.transfer(acc1.account_number, acc2.account_number, 10000)
except InsufficientFundsError as e:
    print(f"خطا: {e}")

# انتقال به حساب ناموجود -> باید خطا بده
try:
    bank.transfer(acc1.account_number, 999, 50)
except ValueError as e:
    print(f"خطا: {e}")

# واریز مقدار نامعتبر -> باید خطا بده
try:
    acc1.deposit(-50)
except InvalidAmountError as e:
    print(f"خطا: {e}")

# تاریخچه تراکنش‌ها
print(acc1.transaction_history)