import time #importing librari 
print("Please Insert your card") 
time.sleep 
password = 1234 # creting password to authentication 
pin=int(input("Enter your atm pin"))
Balance = 10000  
if pin == password: #condition for authentication verification 
    while True: 
        print(""""
            1 == Balance 
            2 == Withdraw balance 
            3 == Deposit balance
            4 == Exit  
            """) 
        try: #verification of options 
            option = int(input("Please Enter your Choice"))
        except: 
            print("Please Enter Valid option")
            

        if option == 1: 
            print("**************************")
            print("**************************")
            print(f"Your current balance is {Balance}")
            print("**************************")
            print("**************************")
        elif option == 2:
            withdrawal_amount=int(input(" Please Enter the with draw amount"))
            Balance = Balance - withdrawal_amount
            print("**************************")
            print("**************************") 
            print(f"{withdrawal_amount} is debited from your account")
            print("**************************")
            print("**************************")


            print("**************************")
            print("**************************")
            print(f" Your Updated balance is {Balance}")
            print("**************************")
            print("**************************") 
        elif option == 3: 
            Deposit_amount = int(input("Please Enter your deposite ampunt"))
            Balance = Balance + Deposit_amount 

            print("**************************")
            print("**************************")
            print(f"{Deposit_amount} is credited to your account")
            print("**************************")
            print("**************************")

            print("**************************")
            print("**************************")
            print(f"Your Updated Balance is {Balance}")
            print("**************************")
            print("**************************")
        else:
            break
else: 
    print("**************************")
    print("**************************")
    print("Worng Pin Please Try Again")
    print("**************************")
    print("**************************")