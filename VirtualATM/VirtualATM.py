# ATM Automation

# Get the user's name
user_name = input("Please enter your name: ")
print("Welcome,", user_name)

# Display the options
print("""
Please select an option:
1 -> Check Balance
2 -> Deposit Money
3 -> Withdraw Money
""")

# Get the user's choice
option = int(input("Enter your choice (1-3): "))
current_balance = 5000

# Validate the user's choice and proceed accordingly
if option in [1, 2, 3]:
    print("Processing your request...")

    if option == 1:
        # Check balance
        print("Your current balance is: ₹", current_balance)
        print("Thank you for banking with us!")

    elif option == 2:
        # Deposit money
        deposit_amount = int(input("Enter the amount you wish to deposit: ₹"))
        if deposit_amount > 500:
            current_balance += deposit_amount
            print(f"₹{deposit_amount} has been successfully deposited.")
            print("Your updated balance is: ₹", current_balance)
            print("Thank you for banking with us!")
        else:
            print("Deposit amount must be more than ₹500.")

    elif option == 3:
        # Withdraw money
        withdraw_amount = int(input("Enter the amount you wish to withdraw: ₹"))
        if withdraw_amount <= current_balance:
            current_balance -= withdraw_amount
            print(f"₹{withdraw_amount} has been successfully withdrawn.")
            print("Your updated balance is: ₹", current_balance)
            print("Thank you for banking with us!")
        else:
            print("Insufficient funds. Your current balance is: ₹", current_balance)
else:
    print("Invalid choice. Please select a valid option (1-3).")
