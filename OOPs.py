class Account:
    bank_bal = 0
    acc_no = 0
    def __init__(self,acc_no):
        self.acc_no=acc_no
        
    def debit(self,amt,acc_no):
        if(acc_no==self.acc_no):

            self.acc_no = acc_no
            if amt>self.bank_bal:
                print("Insufficient balance")
            else:
                self.bank_bal=self.bank_bal-amt
                print(f"Success transaction ,{amt} got withdraw and balance is {self.bank_bal}")
        else:
            print("enter the account number properly")

    def credit(self,amt,acc_no):
        if(acc_no==self.acc_no):
            self.bank_bal+=amt
        else:
            print("enter the account number properly")

    def balance(self,acc_no):
        if(acc_no==self.acc_no):
            print(f"Your balance is {self.bank_bal}")
        else:
            print("enter the account number properly")

customer1 = Account(3132)
customer1.credit(10000,3132)
customer1.balance(3132)
customer1.debit(500,3132)
customer1.balance(3132)

customer1.debit(198765432345,3132)
customer1.balance(3132)

