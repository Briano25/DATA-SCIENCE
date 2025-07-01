class BankAccount:
    # Constructor to initialize account details
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    # Method to display account details
    def display(self):
        print(f"Account Owner: {self.owner}")
        print(f"Account Balance: {self.balance}")

# Create an account object
account1 = BankAccount("John Doe", 1000)

# Use the object
account1.display()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)  # Trying to withdraw more than balance
