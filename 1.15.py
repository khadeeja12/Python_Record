class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance is ₹{self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. New balance is ₹{self.balance:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Balance: ₹{self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest: ₹{interest:.2f}.")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=1000.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. New balance is ₹{self.balance:.2f}.")
            else:
                print("Exceeds overdraft limit.")
        else:
            print("Withdrawal amount must be positive.")


if __name__ == "__main__":
    savings = SavingsAccount("SA123456", "Alice", 1000.0)
    savings.deposit(500)
    savings.withdraw(200)
    savings.apply_interest()
    savings.display_balance()

    checking = CheckingAccount("CA123456", "Bob", 500.0)
    checking.deposit(300)
    checking.withdraw(700)
    checking.withdraw(2000)  
    checking.display_balance()
