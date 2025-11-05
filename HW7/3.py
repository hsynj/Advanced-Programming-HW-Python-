class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}$ be hesabe {self.account_holder} variz shod")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Shoma nemitavanid bishtar az mojoodi bardasht konid. Mojoodi -> {self.balance}")
        else:
            self.balance -= amount
            print(f"meghare {amount}$ az hesabe {self.account_holder} bardasht shod.")
    
    def get_balance(self):
        print(f"mojoodi hesab shoma {self.account_holder}, {self.balance}$ ast.")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}$"
    def __repr__(self):
        return f"BankAccount(account_holder={self.account_holder}, balance={self.balance})"


amir = BankAccount('Amir', 20700)
amir.deposit(200)
amir.withdraw(30000)
amir.get_balance()