class Account:
    """
     The class account is the basic class that savingAccount and CheckingAccount inherit from it all methods and attributes 
    """
    def __init__(self,account_number,holder_name,balance,type,counter=0) :
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance 
        self.type=type
        self.counter=counter

    def deposit(account,amount):
        """
         We use Function 'depsoit' to add money to an account
        """
        account.balance+=amount 

    def withdraw(account,amount):
        """
         we use Function 'withdraw' to withdraw money from an account
        """
        if account.type =="SavingAccount" and account.counter < 10 :
            if account.balance > 0:
                    account.balance-=amount 
                    account.counter+=1
            else :
                    print("you don't enough money")
        elif account.type =="CheckingAccount" :
                if account.balance > 0:
                    account.balance-=amount 
                else :
                    print("you don't enough money")
        else :
             print("you execced the limit of withdraw to this account,please try later")
        
    
    def transfer(Sender_Acc,receiver_Acc,Amount):
         """
         We use Function 'Transfer' to transfer money from an account to another account
         """
         if (Sender_Acc.balance >0)  and  (Amount <= Sender_Acc.balance):  
            Sender_Acc.balance-=Amount
            receiver_Acc.balance+=Amount
         else :
              print("The Account doesn't have enough balance to transfer")

         
    def check_balance(account):
        """
        We use Function 'check_balance' to return data about an account like (account_number,holder_name of account and so on)
        """
        details={"holder_name":account.holder_name,"account.number":account.account_number,"account_type":account.type,"account.balance":account.balance}
        return details 
    

class savingAccount(Account):
    """
    This is the savingAccount class iherits all methods and attributes from its parent class Account.
    """
    def __init__(self,account_number,holder_name,balance,type) :
        super().__init__(account_number,holder_name,balance,type)
        


class CheckingAccount(Account):
    """
    This is the CheckingAccount class iherits all methods and attributes from its parent class Account.
    """
    def __init__(self,account_number,holder_name,balance,type) :
        super().__init__(account_number,holder_name,balance,type)
        


Account1=savingAccount(100,"ahmed",200,"SavingAccount")

Account2=savingAccount(200,'ali',4000,'SavingAccount')
     
Account1.transfer(Account2,200)


print(Account1.balance)
print(Account2.balance)

