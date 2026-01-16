class Account:
    def __init__(self,bal,acc):
        
        self.balance = bal
        self.account_no = acc
    def debit(self,amount):
        if self.balance<amount:
            print("Error! Your balance is low!!")
        else:
            self.balance=-amount
            print(f"RS {amount} was debited")
            print(f"Total balance : {self.get_balance()}")
    def credit(self,amount):
        self.balance=+amount
        print(f"RS {amount} was Credited")
        print(f"Total balance : {self.get_balance()}")
    def get_balance(self):
        return self.balance
    


acc1= Account(10000,1234)
print(acc1.balance)
print(acc1.account_no)
