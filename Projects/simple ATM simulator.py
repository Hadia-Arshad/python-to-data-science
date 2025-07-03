balance = 1000
while True:
    print("\nwellcome to ATM") 
    print("1. check balance")  
    print("2. deposit money") 
    print("3. withdraw money")
    print("4. Eixt")
    user_choice=int(input("enter your choice (1-4):"))
    if user_choice== 1:
        print("your current balance is:", balance)
    elif user_choice == 2:
        deposit= int(input("enter deposit amount:"))
        balance+=deposit
        print("deposited successfully. New balance:", balance)
    elif user_choice == 3:
        withdrawal= int(input("enter withdraw amount:"))
        if withdrawal<=balance:
            balance-=withdrawal
            print("successfully withdrawal. remaining balance is:", balance)
        else:
            print("insufficient balance. Transaction failed.")
    elif user_choice== 4:
        print("Thank you for using ATM")
        break