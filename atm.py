# 🔹 Functions

def checkBalance(balance):
    return balance


def deposit(balance):
    try:
        amt = float(input("Enter deposit amount: "))
        
        if amt <= 0:
            print("Amount positive hona chahiye")
            return balance
        
        balance += amt
        print(f"Deposit successful! Total balance: {balance}")
    
    except:
        print("Galat input diya hai")
    
    return balance


def withdraw(balance):
    try:
        amt = float(input("Enter withdraw amount: "))
        
        if amt > balance:
            print("Paise kam hai")
        
        elif amt <= 0:
            print("Amount sahi dalo")
        
        else:
            balance -= amt
            print(f"Withdrawal successful! Remaining balance: {balance}")
    
    except:
        print("Galat input diya hai")
    
    return balance


def Pin():
    real_pin = "1234"
    
    for i in range(3):
        pin = input("Pin dalo: ")
        
        if pin == real_pin:
            print(f"Pin verified successfully ✅")
            return True
        else:
            print(f"Galat pin ❌ | Attempt left: {2-i}")
    
    print(f"Card block ho gaya 🚫")
    return False


# 🔥 MAIN PROGRAM

if Pin():

    # balance input
    while True:
        try:
            balance = float(input("Starting balance dalo: "))
            break
        except:
            print("Number dalo bhai")

    # menu
    while True:
        print(f'''
========== ATM MENU ==========
1. Balance Check
2. Deposit
3. Withdraw
4. Exit
==============================
''')

        choice = input("Kya karna hai: ")

        if choice == "1":
            print(f"💰 Tumhara balance hai: {checkBalance(balance)}")

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print(f"Thank you! Visit again 👋")
            break

        else:
            print(f"Galat option select kiya hai")

else:
    print(f"Access Denied ❌")


