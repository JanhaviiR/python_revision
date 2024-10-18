balance = 1000.00  
while True:
    print("****ATM Simulator Menu ****")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        print("Your current balance is:",balance)
    elif choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            balance += deposit_amount
            print("Amount has been deposited. New balance is:",balance)
    elif choice == '3':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif withdraw_amount > balance:
            print("Insufficient balance. Transaction denied.")
        else:
            balance -= withdraw_amount
            print("Amount has been withdrawn. New balance is:",balance)
    elif choice == '4':
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice")