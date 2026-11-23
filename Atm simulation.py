
print("===================================")
print("       WELCOME TO PYTHON ATM       ")
print("===================================")

# Account Details
correct_pin = "1234"
balance = 5000
transactions = []

# PIN Verification
pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:

    print("\nLogin Successful!")

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print("\nYour Current Balance is:", balance)

        # Deposit Money
        elif choice == "2":

            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: Rs. {amount:.2f}")
                print("Money Deposited Successfully!")
                print("Updated Balance:", balance)

            else:
                print("Please enter a valid amount!")

        # Withdraw Money
        elif choice == "3":

            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Please enter a valid amount!")

            elif amount > balance:
                print("Insufficient Balance!")

            else:
                balance -= amount
                transactions.append(f"Withdrawn: Rs. {amount:.2f}")
                print("Please collect your cash!")
                print("Remaining Balance:", balance)

        # Change PIN
        elif choice == "4":

            old_pin = input("Enter your old PIN: ")

            if old_pin == correct_pin:

                new_pin = input("Enter your new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    correct_pin = new_pin
                    print("PIN Changed Successfully!")

                else:
                    print("PIN must contain exactly 4 digits!")

            else:
                print("Incorrect Old PIN!")

        # Transaction History
        elif choice == "5":

            print("\n====== TRANSACTION HISTORY ======")

            if len(transactions) == 0:
                print("No transactions yet!")

            else:
                for transaction in transactions:
                    print(transaction)

        # Exit
        elif choice == "6":
            print("\nThank you for using Python ATM!")
            break

        else:
            print("Invalid Choice! Please try again.")

else:
    print("\nIncorrect PIN! Access Denied.")

print("\n===================================")
print("          THANK YOU!")
print("===================================")