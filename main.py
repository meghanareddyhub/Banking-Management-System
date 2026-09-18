from customer import check_balance, create_customer, verify_password, view_my_details
from transaction import deposit_money, withdraw_money, view_transactions, create_account

print("====== NOVA BANK ======")
account_id = int(input("Enter account ID: "))
password = input("Enter password : ")
if verify_password(account_id, password):
    print("Login successful ✅")
    while True:
        print("1. Check Balance" )
        print("2. Deposit Money" )
        print("3. Withdraw Money" )
        print("4. View Transactions" )
        print("5. View My Details" )
        print("6. Create Customer" )
        print("7. Create Account" )
        print("8. Exit" )

        #BALANCE
        choice = int(input("Enter your choice :"))
        if choice == 1 :
            balance = check_balance(account_id)
            if balance is None:
                print("Account not found")
            else : 
                print("Your current balance is Rs",balance,"/-") 
        #DEPOSIT
        elif choice == 2:
            #account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to deposit:"))
            result = deposit_money(account_id,amount)
            if result : 
                print("Amount deposited successfully !!")
            else:
                print("Invalid amount")
        #WITHDRAW
        elif choice == 3:
            #account_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to withdraw:"))
            result = withdraw_money(account_id,amount)
            if result : 
                print("Amount withdrawn successfully !!")
            else:
                print("Inavlid account, amount or Insufficient balance :( ")
        #TRANSACTION
        elif choice == 4:
           # account_id = int(input("Enter account ID:"))
            transactions = view_transactions(account_id)
            print("===== Transactions =====")
            for transaction in transactions:
                print("Type:",transaction[0])
                print("Amount: Rs",transaction[1])
                print("Date:",transaction[2])
                print("-----------------")
        #MY DETAILS
        elif choice == 5:
            details = view_my_details(account_id)
            if details is None : 
                print("Account details not found")
            else:
                print("\n === MY ACCOUNT DETAILS === ")
                print("Name :",details[0])
                print("Phone :",details[1])
                print("Email :",details[2])
                print("Address :",details[3])
                print("Account ID :",details[4])
        #CREATE CUSTOMER
        elif choice == 6 : 
            full_name = input("Enter full name : ")
            phone = input("Enter phone number : ")
            email = input("Enter email : ")
            address = input("Enter address : ")
            customer_id = create_customer(
                full_name,
                phone,
                email,
                address
            )
            print("Customer created Successfully 😊!!!")
            print("Customer ID:",customer_id)
        #CREATE ACCOUNT ID
        elif choice == 7 :
            customer_id = int(input("Enter customer ID:"))
            account_type = input("Enter account type (Savings/Current):")
            account_id = create_account(customer_id,account_type)
            print("Account created successfullyy!!")
            print("Account ID:",account_id)
        #EXIT
        elif choice == 8 :
            print("Thank you for using Nova Bank !!")
            break
        else : 
            print("Invalid")

        #CONINUE OR EXIT 
        again = input("\n Would you like to continue ? (Yes/No):")
        if again.lower() == "no":
            print("Thank you for using Nova Bank !! ")
            break
        elif again.lower() == "yes":
            continue    
else:
    print("Invalid account ID or password ")
