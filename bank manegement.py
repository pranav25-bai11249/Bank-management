import random
bank_accounts=[]
account_numbers=[]
cif_numbers=[]
bank_loan=[]

def create_account():
    account=[]
    n1=random.randint(1000,9999)
    n2=random.randint(100,999)
    name=input("Enter your name: ")
    n3=int(input("Enter your contact number: "))
    balance=int(input("Enter your initial balance: "))

    account.append(n1) #0
    account.append(n2) #1
    account.append(name) #2
    account.append(n3) #3
    account.append(balance) #4

    print("Thank you for creating an account with us")
    print("Your account number is: ",n1)
    print("Your CIF number is: ",n2)
    print(account)

    account_numbers.append(n1)
    cif_numbers.append(n2)

    bank_accounts.append(account)

def view_account():
    n1=int(input("Enter your account number: "))
    n2=int(input("Enter your CIF number: "))
    for i in bank_accounts:
        if i[0]==n1 and i[1]==n2:
            print(i)
        else:
            print("Wrong details entered please check your account number and CIF number")

def deposit_money():
    n1=int(input("Enter your account number: "))
    n2=int(input("Enter your cif number: "))
    for i in bank_accounts:
        if i[0]==n1 and i[1]==n2:
            balance=int(input("Enter the amount you want to deposit: "))
            i[4]+=balance
        else:
            print("Wrong details entered please check your account number and CIF number")

def withdraw_money():
    n1=int(input("Enter your account number: "))
    n2=int(input("Enter your CIF number: "))
    for i in bank_accounts:
        if i[0]==n1 and i[1]==n2:
            balance=int(input("Enter the amount you want to withdraw: "))
            if balance>i[4]:
                print("Balance cannot be negative")
            else:
                i[4]-=balance
        else:
            print("Wrong details entered please check your account number and CIF number")

def apply_loan():
    loan=[]
    n1=int(input("Enter your account number: "))
    n2=int(input("Enter your CIF number: "))
    for i in bank_accounts:
        if i[0]==n1 and i[1]==n2:
            amount=int(input("Enter the loan amount: "))
            if amount>i[4]//2:
                print("You are not eligible for loan")
            else:
                emi=int(input("Enter how many installment you want to pay: "))
                interest=amount*110/100
                emi_amount=interest/emi
                loan.append(i[0]) #0 
                loan.append(i[1]) #1
                loan.append(i[2]) #2
                loan.append(i[3]) #3
                loan.append(interest) #4
                loan.append(emi_amount) #5
                loan.append(emi) #6
                bank_loan.append(loan)
        else:
            print("Wrong details entered please check your account number and CIF number")

def repay_loan():
    n1= int(input("Enter your account number: "))
    n2=int(input("Enter your CIF number: "))
    for i in bank_loan:
        if i[0]==n1 and i[1]==n2:
            i[4]-=i[5]
            i[6]-=1
        else:
            print("Wrong details entered please check your account number and CIF number")
        if i[6]==0:
            bank_loan.remove(i)
                

while True:
    print("1: Create a new account")
    print("2: View your account")
    print("3: Deposit money")
    print("4: Withdraw money")
    print("5: Apply for loan")
    print("6: Repay loan")
    print("7: Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        create_account()
    elif choice==2:
        view_account()
    elif choice==3:
        deposit_money()
    elif choice==4:
        withdraw_money()
    elif choice==5:
        apply_loan()
    elif choice==6:
        repay_loan()
    elif choice==7:
        break