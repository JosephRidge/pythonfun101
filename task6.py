"""
Task 6: OOP (Encapsulation Light) (10 min)
Create a BankAccount class:

Private variable __balance
Methods:
deposit(amount)
withdraw(amount) (no negative balance)
get_balance()


Create one object and perform operations.

"""
 
class BankAccount:

    # Private variable __balance

    def __init__(self, amount ):
        self.amount = amount
        self.__balance = amount # encapsulatiion (makes this attribute private)

    # Methods:
    # deposit(amount)
    def deposit(self, amount):
        # self.amount = amount
        self.__balance +=amount
        print(f"Your new balance is {self.__balance}")

    # withdraw(amount) (no negative balance)

    def withdraw(self,amount):
        if self.__balance < amount:
            print(f"Your balance is {self.__balance} not enough money!")
        else:
            self.__balance -= amount
            print(f"Your balance is now {self.__balance}!")


    # get_balance()
    def get_balance(self):
        print(f"Your balance is {self.__balance}/=")

firstAccount = BankAccount(amount = 500.80)
print("*********************************")
firstAccount.get_balance()
firstAccount.deposit(1500.256)
firstAccount.withdraw(1999)

print("*********************************")




