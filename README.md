# 💳 ATM Machine Project (With File Handling)

Welcome! 👋  
This is a simple yet powerful ATM Machine project built using Python.  
Now upgraded with **File Handling**, which allows data to be saved permanently even after closing the program.

---

# 🚀 Features

🔐 Secure PIN verification (3 attempts)  
💰 Check current balance anytime  
💵 Deposit money (only positive amount allowed)  
🏧 Withdraw money (with balance validation)  
📂 Persistent balance using file handling  
🧾 Transaction history stored in file  
⚡ Error handling using try-except  
📋 Clean and user-friendly menu  
🗣 Messages in English + Hindi  

---

# 📁 Files Used

### 1️⃣ balance.txt
- Stores current balance  
- Updated every time deposit/withdraw happens  

Example:
5500

---

### 2️⃣ history.txt
- Stores all transaction records  
- New data is appended (not overwritten)  

Example:
Deposited: 1000 | Balance: 6000 Withdrawn: 500 | Balance: 5500

---

# 🛠 Tech Used

- Python (Core Concepts)
- Functions
- Loops
- Exception Handling (try-except)
- File Handling (`r`, `w`, `a` modes)
- f-strings for formatting

---

# ▶️ How to Run

1. Make sure Python is installed  
2. Clone this repository:
git clone https://github.com/Rohanverma15082004/ATM-Machine-Project.git

3. Open project folder:
cd ATM-Machine-Project

4. Run the program:
python atm.py

---

# 🔥 How It Works

1. Program starts and loads balance from `balance.txt`  
2. User enters PIN  
3. User selects options:
   - Check Balance  
   - Deposit  
   - Withdraw  
4. Every transaction:
   - Updates balance file  
   - Saves history in `history.txt`  
5. Data remains saved even after program exits  

---

# 💡 Concepts Covered

✔ File Handling (Read, Write, Append)  
✔ Persistent Data Storage  
✔ Functions & Modular Code  
✔ Input Validation  
✔ Real-world ATM logic  

---

# 🔄 Future Improvements

- Add multiple users support  
- Add mini statement feature  
- Store PIN securely in file  
- Add GUI (Tkinter)  

---

# 👨‍💻 Author

**Rohan Verma**  
Python Learner 🚀  
Building projects to improve real-world coding skills  

---

# ⭐ Final Note

This project started as a basic ATM system and evolved into a **file-based persistent system**, making it closer to real-world applications.

If you like this project, feel free to ⭐ star the repo!
