class BankAcount:
    def __init__(self , owner , balance=100):
        self.owner = owner
        self.owner = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to {self.owner}")

    def withdraw(self , amount) :
        if amount < self.balance:
            self.balance -= amount
            print (f"withdrawn {amount} to {self.owner}")
        else:
            print("Insufficient balance")


    def show_balance(self):
        if __name__ = "__main__" :
            my_acount = BankAcount("Behrad Shahabi" , 2500)
            my_acount.deposit(250)
            my_acount.withdraw(1000)
        print (f"your balance = {my_acount.balance}")



