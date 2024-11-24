import datetime

def ATM():
    Balance = 10000
    Pin = 1234
    Transaction_history = []

    def Log_transaction(Task, Amount=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if Amount is not None:
            Transaction_history.append(f"{timestamp} - {Task}:₹{Amount}")
        else:
            Transaction_history.append(f"{timestamp} - {Task}")
    #Authenticate PIN
    for Attempt in range(3): # Allows 3 attempts
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == Pin :
            print("PIN is Accepted")
            break 
        else:
            print(f"Incorrect PIN. Attempts remaining: {2 - Attempt}")
    else:
        print("Too Many incorrect attempts. Exiting.")
        return # Exit Program after 3 faild attempts 
    
    #Main ATM Menu 
    while True:
        print("\nWelcome to the ATM!")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        Choice = input("Enter your choice: ")

        if Choice == "1":
            # Balance Inquiry 
            print(f"Your current balance is: ₹{Balance}")
            Log_transaction("Balance Inquiry")
        elif Choice == "2":
            # Cash withdrawl 
            try:
                Amount = float(input("Enter the amount to withdraw: "))
                if Amount > Balance:
                    print("Insufficient Balance.")
                elif Amount <=0:
                    print("Enter a valid amount.")
                else:
                    Balance -= Amount 
                    print(f"₹{Amount} Withdrawn Successfully. Remaining balance: ₹{Balance}")
                    Log_transaction("Withdrawal", Amount)
            except ValueError:
                print("Invalid amount. please enter a numeric value.")
        elif Choice == "3":
            #cash Deposit 
            try:
                Amount =  float(input("Enter the amount to deposit: "))
                if Amount <= 0:
                    print("Enter a Valid amount.")
                else:
                    Balance += Amount 
                    print(f"₹{Amount} depostied successfully. Current balance: ₹{Balance}")
                    Log_transaction("Deposite", Amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif Choice == "4":
            # Change PIN 
            current_pin = int(input("Enter Current PIN: "))
            if current_pin == Pin:
                new_pin = int(input("Enter new PIN: "))
                confirm_pin = int(input("Confirm new PIN:"))
                if new_pin == confirm_pin:
                    Pin = new_pin 
                    print("PIN changed successfully.")
                    Log_transaction("PIN Changed")
                else:
                    print("PIN confirm doesn't match. Try again.")
            else:
                print("Incorrect PIN.")
        elif Choice == "5":
            # Transaction History 
            if not Transaction_history:
                print("No transactions yet.")
            else:
                print('\nTransaction History:')
                for transaction in Transaction_history:
                    print(transaction)
        elif Choice == "6":
            #Exit 
            print("Thank you for using ATM. Goodbye!")
            break 
        else:
            print("Invalid Option. Please try again.")
if __name__ == "__main__":
    ATM()