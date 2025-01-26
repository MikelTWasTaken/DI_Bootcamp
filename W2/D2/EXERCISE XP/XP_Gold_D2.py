# Exercise 1: Bank Account
# Instructions
# Part I:

# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive

# Part II : Minimum balance account

# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.


# Part III: Expand the bank account class

# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (False by default)

# Create a method called authenticate. This method should accept 2 strings : a username and a password. If the username and password match the attributes username and password the method should set the authenticated boolean to True.

# Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception


# Part IV: BONUS Create an ATM class

# __init__:
# Accepts the following parameters: account_list and try_limit.

# Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
# Hint: isinstance()

# Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2.
# Hint: Check out this tutorial

# Sets attribute current_tries = 0

# Call the method show_main_menu (see below)

# Methods:
# show_main_menu:
# This method will start a while loop to display a menu letting a user select:
# Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
# Exit.

# log_in:
# Accepts a username and a password.

# Checks the username and the password against all accounts in account_list.
# If there is a match (ie. use the authenticate method), call the method show_account_menu.
# If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.

# show_account_menu:
# Accepts an instance of BankAccount or MinimumBalanceAccount.
# The method will start a loop giving the user the option to deposit, withdraw or exit.


class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

class BankAccount(User):
    total_deposit = 0
    total_withdraw = 0

    def __init__(self, name, age, gender, balance):
        # Initialize the parent class (User)
        super().__init__(name, age, gender)
        self.balance = balance

    def show_info(self):
        return f"{self.name} has a remaining balance of: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("The deposit amount should be positive")
        else:
            self.balance += amount
            BankAccount.total_deposit += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        elif amount < 0:
            raise Exception("The withdraw amount should be greater than zero")
        else:
            self.balance -= amount
            BankAccount.total_withdraw += amount

# Creating a BankAccount instance
user_account = BankAccount("John Doe", 30, "Male", 0)
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(user_account.show_info())
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        user_account.deposit(amount)
        print(f"Deposited ${amount:.2f}. Current balance: ${user_account.balance:.2f}")
    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        user_account.withdraw(amount)
        print(f"Withdrew ${amount:.2f}. Current balance: ${user_account.balance:.2f}")
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the banking program!")

class MinimumBalanceAccount(BankAccount):
    def __init__(self, name, age, gender, balance, minimum_balance=0):
        super().__init__(name, age, gender, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Balance must remain above the minimum balance of ${self.minimum_balance}")
        super().withdraw(amount)


class BankAccount(User):
    total_deposit = 0
    total_withdraw = 0

    def __init__(self, name, age, gender, balance, username, password):
        super().__init__(name, age, gender)
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print("Authentication successful!")
        else:
            raise Exception("Authentication failed")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must authenticate first")
        super().deposit(amount)

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must authenticate first")
        super().withdraw(amount)

class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list):
            raise Exception("account_list must be a list of BankAccount or MinimumBalanceAccount instances.")
        if any(not isinstance(account, (BankAccount, MinimumBalanceAccount)) for account in account_list):
            raise Exception("All items in account_list must be instances of BankAccount or MinimumBalanceAccount.")
        if try_limit <= 0:
            print("Invalid try_limit input. Setting try_limit to 2.")
            try_limit = 2
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

    def show_main_menu(self):
        while True:
            print("Main Menu:")
            print("1. Log in")
            print("2. Exit")
            choice = input("Enter your choice (1-2): ")

            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.log_in(username, password)
            elif choice == "2":
                break
            else:
                print("Invalid choice, please try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                self.show_account_menu(account)
                return
            except Exception as e:
                print(e)
        
        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Max tries reached. Shutting down the ATM.")
            exit()
        else:
            print(f"Invalid credentials. Try {self.current_tries}/{self.try_limit}.")

    def show_account_menu(self, account):
        while True:
            print(f"Welcome, {account.name}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                try:
                    account.deposit(amount)
                    print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")
                except Exception as e:
                    print(e)
            elif choice == "2":
                amount = float(input("Enter withdraw amount: "))
                try:
                    account.withdraw(amount)
                    print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")
                except Exception as e:
                    print(e)
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again.")