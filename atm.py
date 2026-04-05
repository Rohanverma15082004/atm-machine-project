# 📁 File names
BAL_FILE = "balance.txt"
HIS_FILE = "history.txt"


# 🔹 1. Load balance (read file)
def load_balance():
    try:
        with open(BAL_FILE, "r") as f:
            return float(f.read())
    except:
        return 0.0   # agar file nahi hai to


# 🔹 2. Save balance (write file)
def save_balance(balance):
    with open(BAL_FILE, "w") as f:
        f.write(str(balance))


# 🔹 3. Save history (append)
def save_history(text):
    with open(HIS_FILE, "a") as f:
        f.write(text + "\n")


# 🔹 4. Deposit
def deposit(balance):
    try:
        amt = float(input("Deposit amount dalo: "))

        if amt <= 0:
            print("Amount positive hona chahiye")
            return balance

        balance += amt
        print(f"Deposit successful! Balance: {balance}")

        save_balance(balance)
        save_history(f"Deposited: {amt} | Balance: {balance}")

    except:
        print("Galat input")

    return balance


# 🔹 5. Withdraw
def withdraw(balance):
    try:
        amt = float(input("Withdraw amount dalo: "))

        if amt > balance:
            print("Paise kam hai")

        elif amt <= 0:
            print("Sahi amount dalo")

        else:
            balance -= amt
            print(f"Withdraw successful! Balance: {balance}")

            save_balance(balance)
            save_history(f"Withdrawn: {amt} | Balance: {balance}")

    except:
        print("Galat input")

    return balance


# 🔹 6. PIN check
def Pin():
    real_pin = "1234"

    for i in range(3):
        pin = input("PIN dalo: ")

        if pin == real_pin:
            print("PIN correct ✅")
            return True
        else:
            print(f"Wrong PIN ❌ | Attempt left: {2-i}")

    print("Card blocked 🚫")
    return False


# 🔥 MAIN PROGRAM
if Pin():

    balance = load_balance()
    print(f"💰 Current Balance: {balance}")

    while True:
        print("""
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
""")

        choice = input("Choose option: ")

        if choice == "1":
            print(f"Balance: {balance}")

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("Thank you 👋")
            break

        else:
            print("Invalid option")

else:
    print("Access Denied ❌")


