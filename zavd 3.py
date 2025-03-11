class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостатньо коштів!")

    def __str__(self):
        return f"Рахунок {self.account_number} ({self.owner}): {self.balance} грн"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            self.accounts[from_acc].withdraw(amount)
            self.accounts[to_acc].deposit(amount)


# Приклад використання
bank = Bank()
acc1 = BankAccount("Олег", "12345", 1000)
acc2 = BankAccount("Анна", "67890", 500)
bank.add_account(acc1)
bank.add_account(acc2)
bank.transfer("12345", "67890", 200)
print(acc1)
print(acc2)