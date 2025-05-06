
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.owner} tried to withdraw ${amount}, but has insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}.")

    def display_balance(self):
        print(f"{self.owner}'s account balance: ${self.balance}")

# 20 predefined accounts
accounts = [
    BankAccount("Alice", 100, "checking"),
    BankAccount("Bob", 200, "savings"),
    BankAccount("Charlie", 300, "savings"),
    BankAccount("Diana", 400, "checking"),
    BankAccount("Ethan", 500, "savings"),
    BankAccount("Fiona", 600, "checking"),
    BankAccount("George", 700, "savings"),
    BankAccount("Hannah", 800, "checking"),
    BankAccount("Ian", 900, "savings"),
    BankAccount("Jill", 1000, "checking"),
    BankAccount("Kevin", 1100, "savings"),
    BankAccount("Lily", 1200, "checking"),
    BankAccount("Mike", 1300, "savings"),
    BankAccount("Nina", 1400, "checking"),
    BankAccount("Oscar", 1500, "savings"),
    BankAccount("Paula", 1600, "checking"),
    BankAccount("Quinn", 1700, "savings"),
    BankAccount("Rita", 1800, "checking"),
    BankAccount("Sam", 1900, "savings"),
    BankAccount("Tina", 2000, "checking")
]

# Code Starts Here
