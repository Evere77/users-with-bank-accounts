class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0):
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
        # your code here
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        # your code here
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
        # your code here


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_depoist(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()



account1 = BankAccount()
account2 = BankAccount()

account1.deposit(10).deposit(25).deposit(5).withdraw(30).yield_interest().display_account_info()
account2.deposit(100).deposit(75).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()