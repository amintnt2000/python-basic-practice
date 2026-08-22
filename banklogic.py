from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

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
class BankLogic:
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
class CreateAccountRequest(BaseModel):
    owner_name : str = Field(min_length=3)
bank = BankLogic()

@app.post("/account")
def create_account(request: CreateAccountRequest):
    new_account = bank.create_account(request.owner_name)
    return {
        "message": f"Account created for {new_account.owner_name}",
        "account number": new_account.account_number,
        "balance": new_account.balance
    }
@app.get("/account/{account_number}")
def find_account_detail(account_number:int):
    account_detail = bank.find_account(account_number)
    if account_detail is None:
        raise HTTPException(status_code=404, detail="account was not found")
    return {
        "Balance": account_detail.balance,
        "Account number": account_detail.account_number,
        "Owner Name": account_detail.owner_name
    }
class AmountRequest(BaseModel):
    amount : float = Field(gt=0)
@app.post("/account/{account_number}/deposit")
def deposit_to_account(account_number:int, request:AmountRequest):
    account = bank.find_account(account_number)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        account.deposit(request.amount)
    except InvalidAmountError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Deposit successful", "new_balance": account.balance}
@app.post("/account/{account_number}/withdraw")
def withdraw_from_account(account_number:int, request:AmountRequest):
    account = bank.find_account(account_number)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        account.withdraw(request.amount)
    except InsufficientFundsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InvalidAmountError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Withdraw successful", "new_balance":account.balance}
class TransferRequest(BaseModel):
    from_account : int
    to_account : int
    amount : float = Field(gt=0)
@app.post("/transfer")
def transfer(request: TransferRequest):
    from_account = bank.find_account(request.from_account)
    to_account = bank.find_account(request.to_account)
    if from_account is None or to_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        from_account.withdraw(request.amount)
        to_account.deposit(request.amount)
    except InvalidAmountError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InsufficientFundsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Transfer successful",
            "Transfer": f"From account {request.from_account} To account {request.to_account}",
            "new_balance": from_account.balance}