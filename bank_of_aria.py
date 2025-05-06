
class BankAccount:
    def __init__(self, owner, balance, account_type):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type

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
    BankAccount("Tina", 2000, "checking"),
   

# Code Starts Here
    BankAccount("Alice", 100, "checking"),
    BankAccount("Bob", 200, "savings"),
    BankAccount("Charlie", 300, "savings"),
    BankAccount("Charlie", 100, "checking")
]
bob_saving = BankAccount("Bob", 200, "savings")
charlie_saving = BankAccount("Charlie", 300, "savings")
alice_checking = BankAccount("Alice", 100, "checking")
charlie_checking = BankAccount("Charlie", 100, "checking")
bob_saving.deposit(200)
charlie_saving.deposit(300)
alice_checking.withdraw(50)
charlie_checking.withdraw(80)

# for acc in accounts:
if bob_saving.account_type == "savings":
    bob_balance =(105/100) * bob_saving.balance 
    bob_saving.balance =  bob_balance
    print (bob_balance)

