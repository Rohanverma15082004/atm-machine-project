print("----------Functions----------")

def checkBalance(balance):
    print(f"Your balance is: {balance}")


def depositAmount(balance):
    amt = float(input("Enter deposit amount: "))
    balance += amt
    print(f"Deposit successful! Total balance: {balance}")
    return balance


def withdrawAmount(balance):
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: {balance}")
    else:
        print(f"Insufficient balance: {balance}")
    return balance


def verifyPin():
    real_pin = "1234"
    pin = input("Enter your PIN: ")
    if pin == real_pin:
        print("Valid PIN")
        return True
    else:
        print("Invalid PIN")
        return False


# Main Program
mini_Project = "STRING PROJECT"
print(mini_Project.center(60, "-"))

print()
program = "Program Number [1]:"
print(program)
print()

a = "___________ATM_MACHINE_PROJECT__________"
print(a.center(60))

balance = float(input("Enter amount: "))
print()

print("***FEATURES***")
print("""
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
""")


while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if verifyPin():
            checkBalance(balance)

    elif choice == 2:
        balance = depositAmount(balance)

    elif choice == 3:
        if verifyPin():
            balance = withdrawAmount(balance)

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice")


