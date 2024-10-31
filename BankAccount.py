class BankAccount():
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

    def add_interest(self):
        pass

    def print_receipt(self):
        pass