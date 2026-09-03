# OOP concepts using classes , inheritance,encapsulation and theoratical concept of abstraction
# Banking example
class bankaccount:
    def __init__(self,name,accountno,balance):
        self.name=name
        self.__accountno=accountno
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdrawl(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")
    def get_bal(self):
        return self.__balance
    def set_bal(self,amount):
         self.__balance=amount
    def get_accountno(self):
           return self.__accountno
        
   
        
    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.__accountno)
        print("Remaining Balance:", self.__balance)

       

class savingacc(bankaccount):
    def __init__(self,name,accountno,balance,interestrate):
        super().__init__(name,accountno,balance)
        self.interestrate=interestrate
    def add_interest(self):
        interest=self.get_bal()*self.interestrate/100
        self.set_bal(self.get_bal() + interest)
    def display(self):
        super().display()
        print("Interest rate is ",self.interestrate)
        
class currentacc(bankaccount):
        def __init__(self,name,accountno,balance,extralimit):
            super().__init__(name,accountno,balance)
            self.extralimit=extralimit
        def withdrawl(self, amount):
            if amount<=self.get_bal()+self.extralimit:
                self.set_bal(self.get_bal()-amount)
            else:
                print("Limit exceeds")
        def display(self):
            super().display()
            print("Extra limit is ",self.extralimit)
accounts = []
while True:           
    print("         Banking System             ")
    print("1. Open Saving Account")
    print("2. Open Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Display Account")
    print("6. Exit")         

    ch=int(input("Select any number"))
    if ch==1:
        print("Saving account selected")
        name=input("Enter your name")
        accountno=input("Enter your account no")
        if len(accountno)<8:
            print("Account now must have alteast 8 digits")
            continue

        balance=float(input("Enter the balance"))
        interestrate=float(input("Enter interest rate"))

        ac=savingacc(name,accountno,balance,interestrate)
        accounts.append(ac)
        print("Account created successfully")
        ac.display()

    elif ch==2:
        print("Current account Selected")
        name=input("Enter your name")
        accountno=input("Enter your account no")
        if len(accountno)<8:
            print("Account now must have alteast 8 digits")
            continue
        
        balance=float(input("Enter the balance"))
        extralimit=float(input("Enter the extra limit"))
        ac = currentacc(name, accountno, balance, extralimit)
        accounts.append(ac)
        print("Account created successfully")
    elif ch==3:
        accountno=input("Enter account number")
        found=False
        for account in accounts:
            if account.get_accountno()==accountno:
                amount=float(input("Enter the amount you want to deposit"))
                ac.deposit(amount)
                print("Amount deposit successfully" )
                print("Remainig balance is ",ac.get_bal())
                found=True
                break
        if found==False:
            print("Account no not found")
    elif ch==4:
        accountno=input("Enter account no")
        found=False
        for account in accounts:
            if account.get_accountno()==accountno:
                amount=float(input("Enter the amount you want to withdraw"))
                ac.withdrawl(amount)
                print("New balance is ",ac.get_bal())
                found=True
        if found==False:
            print("Account not found")

    elif ch==5:
        accountno = input("Enter account number: ")
        found=False
        for account in accounts:
            if account.get_accountno()==accountno:
                account.display()
                found=True
                break
        if found==False:
                 print("Account not found")
       
               
        


    elif ch==6:
        print("Thank you for using bank")
        break
    else:
        print("Invalid choice")
        


