class Account:
    def __init__(self,acc_num,name,balance):
        self.account_number=acc_num
        self.name=name
        self.balance=balance
        self.transaction=[]
    def view_Account_Details(self):
        return f"Account Number:{self.account_number}\n NAme:{self.name} \nBalance:{self.balance}"
    def deposit(self,amount):
        self.balance+=amount
        self.transaction.append(f"Deposited: {amount}")
        return f"{amount} deposited successfully.Current balance:{self.balance}"
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.transaction.append(f"withdrawn:{amount}")
            return f"{amount} withdrawn successfully.Current balance:{self.balance}"
        else:return "Insufficient Balance"
    def transfer(self,amount,target_account):
        if self.balance>=amount:
            self.balance-=amount
            target_account.balance+=amount
            self.transaction.append(f"transferred {amount} to account {target_account.account_number}")
            target_account.transaction.append(f"recieved {amount} from account {self.account_number}")
            return f"transferred {amount} to {target_account.name} (Account {target_account.account_number})"
        else:
            return "Insufficient balance for transfer"
    def print_transaction(self):
        return "\n".join(self.transaction) if self.transaction else "No transactions"
accounts={}
def createAccount():
    account_number=input("Enter Account Number:")
    name=input("Enter Name:")
    init_deposit=float(input("Enter initial deposit amount:"))
    accounts[account_number]=Account(account_number,name,init_deposit)
    print(f"Account created successfully with account number {account_number}")

def viewAccountDetails():
    account_number=input("Enter account number:")
    if account_number in accounts:
        print(accounts[account_number].view_account_details())
    else:
        print("Account not found")
def deposit():
    account_number=input("Enter account number:")
    if account_number in accounts:
        amount=float(input("Enter deposit amount:"))
        print(accounts[account_number].deposit(amount))
    else:print("account not found")

def withdraw():
    account_number=input("Enter account number:")
    if account_number in accounts:
        amount=float(input("Enter withdraw amount:"))
        print(accounts[account_number].withdraw(amount))
    else:print("account not found")
def transfer():
    from_account=input("Enter your account number")
    to_account=input("Enter reciever account number")
    if from_account in accounts and to_account in accounts:
        amount=float(input("Enter transfer amount:"))
        print(accounts[from_account].transfer(amount,accounts[to_account]))
    else:print("Invalid account details")
def print_details():
    account_number=input("Enter account number:")
    if account_number in accounts:
        print(accounts[account_number].print_transactions())
    else:
        print("Account not found")

while(True):
    print()
    print("1.Create Account")
    print("2.View Account Details")
    print("3.Deposit Ammount")
    print("4.Withdraw Amount")
    print("5.Transfer Amount")
    print("6.Print Transaction Details")
    print("7.Exit")
    choice=int(input("Enter choice"))
    if choice==1:
        createAccount()
    elif choice==2:
        viewAccountDetails()
    elif choice==3:
        deposit()
    elif choice==4:
        withdraw()
    elif choice==5:
        transfer()
    elif choice==6:
        print_details()
    elif choice==7:
        break
    else:
        print("enter a valid choice")
print(accounts)
print("THANKS FOR USING OUR BANK SERVICE")