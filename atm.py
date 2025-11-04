class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def create_pin(self):
        if self.pin == "":
            self.pin = input("Create a four-digit PIN: ")
            print("PIN created successfully.")
        else:
            print("PIN already exists. Please change your PIN if needed.")

    def login(self):
        entered_pin = input("Enter your four-digit PIN: ")
        if entered_pin == self.pin:
            print("Login successful.")
            return True
        else:
            print("Invalid PIN or please create your PIN first.")
            return False

    def deposit(self):
        amount = int(input("Enter your amount: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self):
        withdraw_amount = int(input("Enter your withdrawal amount: "))
        if withdraw_amount > self.balance:
            print("Insufficient balance.")
        elif withdraw_amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= withdraw_amount
            print(f"{withdraw_amount} withdrawn successfully.")

    def balance_enquiry(self):
        print(f"Your current balance is: {self.balance}")

    def change_pin(self):
        old_pin = input("Enter your old PIN: ")
        if old_pin == self.pin:
            self.pin = input("Enter your new four-digit PIN: ")
            print("PIN changed successfully.")
        else:
            print("Old PIN did not match.")


def main():
    atm = ATM()

    while True:
        print("\n--- ATM MAIN MENU ---")
        print("1. Create PIN")
        print("2. Login to ATM")
        print("3. Exit")

        main_choice = input("Enter your choice (1/2/3): ")

        if main_choice == "1":
            atm.create_pin()

        elif main_choice == "2":
            if atm.pin == "":
                print("Please create a PIN first.")
                continue

            if atm.login():
                while True:
                    print("\n--- ATM SERVICES ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Balance Enquiry")
                    print("4. Change PIN")
                    print("5. Logout")

                    choice = input("Select your ATM service: ")

                    if choice == "1":
                        atm.deposit()
                    elif choice == "2":
                        atm.withdraw()
                    elif choice == "3":
                        atm.balance_enquiry()
                    elif choice == "4":
                        atm.change_pin()
                    elif choice == "5":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice.")

        elif main_choice == "3":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
