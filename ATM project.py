ac_details = {"name": "Mounika","Atm_pin": "9032","balance": 10000,"transactions": []}

print("----- Welcome to ATM -----")
print("Insert the card")
remaining_attempts =3
user_pin = input("Please enter 4 digit pin: ")

if len(user_pin) == 4:

    if user_pin == ac_details["Atm_pin"]:

        while True:

            print("\n===== ATM MENU =====")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            # Withdraw
            if choice == 1:

                with_draw = int(input("Enter amount to withdraw: "))

                if with_draw <= ac_details["balance"] and with_draw % 100 == 0:

                    ac_details["balance"] -= with_draw

                    ac_details["transactions"].append(
                        f"Withdraw: ₹{with_draw}"
                    )

                    print("Thank you for withdrawing the amount")
                    print("Available Balance:", ac_details["balance"])

                else:
                    print("Insufficient balance or invalid amount")

            # Deposit
            elif choice == 2:

                deposit = int(input("Enter amount to deposit: "))

                if deposit % 100 == 0:

                    ac_details["balance"] += deposit

                    ac_details["transactions"].append(
                        f"Deposit: ₹{deposit}"
                    )

                    print("Thank you for depositing the money")
                    print("Available Balance:", ac_details["balance"])

                else:
                    print("Please deposit amount in multiples of 100")

            # Check Balance
            elif choice == 3:

                print("Current Balance:", ac_details["balance"])

            # Change PIN
            elif choice == 4:

                old_pin = input("Enter old PIN: ")

                if old_pin == ac_details["Atm_pin"]:

                    new_pin = input("Enter new 4 digit PIN: ")

                    if len(new_pin) == 4 and new_pin.isdigit():

                        ac_details["Atm_pin"] = new_pin

                        ac_details["transactions"].append(
                            "PIN Changed"
                        )

                        print("PIN changed successfully")

                    else:
                        print("PIN must contain exactly 4 digits")

                else:
                    print("Incorrect old PIN")

            # Transaction History
            elif choice == 5:

                print("\n----- Transaction History -----")

                if len(ac_details["transactions"]) == 0:
                    print("No transactions available")

                else:
                    for i in ac_details["transactions"]:
                        print(i)

            # Exit
            elif choice == 6:

                print("Thank you for using ATM")
                break

            else:
                print("Choose from the given options")

    else:
        print("Please enter correct PIN")

else:
    print("Please enter 4 digit PIN")   explain me this code
