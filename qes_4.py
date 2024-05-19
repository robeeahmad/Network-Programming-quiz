class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${}. New balance: ${}".format(amount, self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrew ${}. New balance: ${}".format(amount, self.balance))

    def get_balance(self):
        return self.balance

    def __str__(self):
        return "Account Number: {}, Account Holder: {}, Balance: ${}".format(
            self.account_number, self.account_holder, self.balance
        )


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def __str__(self):
        return "{}, Interest Rate: {}".format(
            super().__str__(), self.interest_rate
        )


bank_account = BankAccount("1000000", "Ruba Ahmad_1")

bank_account.deposit(1000)

bank_account.withdraw(500)

print(bank_account)

savings_account = SavingsAccount("78000", "Ruba Ahmad_2", interest_rate=0.05)

savings_account.apply_interest()
print(savings_account)
