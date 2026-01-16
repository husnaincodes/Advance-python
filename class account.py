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