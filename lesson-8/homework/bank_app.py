class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = self.generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def generate_account_number(self):
        return str(len(self.accounts) + 1).zfill(4)

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for acc_num, acc in self.accounts.items():
                file.write(f"{acc_num},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    acc_num, name, balance = line.strip().split(',')
                    self.accounts[acc_num] = Account(acc_num, name, float(balance))
        except FileNotFoundError:
            print("File not found. New file is created.")

bank = Bank()
print("Welcome to the Bank Application!")
while True:
    print("1. Create an account")
    print("2. View account details")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        bank.create_account(name, initial_deposit)
    elif choice == "2":
        account_number = input("Enter account number: ")
        bank.view_account(account_number)
    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(account_number, amount)
    elif choice == "4":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw(account_number, amount)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    print('-'*50)