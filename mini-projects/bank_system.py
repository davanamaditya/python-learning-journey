 # Bank Account Management System
import json

def load_bank():
    try:
        with open('bank.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def save_bank(data):
    with open('bank.json', 'w') as f:
        json.dump(data, f, indent=4)

accounts = load_bank()

while True:
    print("\n--- BANK ACCOUNT MANAGEMENT SYSTEM ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance & History")
    print("5. Save & Exit")
    
    ch = input("Enter your choice: ")
    
    if ch == '1':
        acc = input("Enter new account number: ")
        if acc in accounts:
            print("Account already exists!")
        else:
            name = input("Enter account holder name: ")
            bal = float(input("Enter initial deposit amount: "))
            accounts[acc] = {"name": name, "balance": bal, "history": [f"Account created with opening balance: {bal}"]}
            print("Account created successfully!")
            
    elif ch == '2':
        acc = input("Enter account number: ")
        if acc in accounts:
            amt = float(input("Enter amount to deposit: "))
            accounts[acc]['balance'] += amt
            accounts[acc]['history'].append(f"Deposited: +{amt}")
            print("Deposit successful! New Balance:", accounts[acc]['balance'])
        else:
            print("Account not found.")
            
    elif ch == '3':
        acc = input("Enter account number: ")
        if acc in accounts:
            amt = float(input("Enter amount to withdraw: "))
            if accounts[acc]['balance'] >= amt:
                accounts[acc]['balance'] -= amt
                accounts[acc]['history'].append(f"Withdrew: -{amt}")
                print("Withdrawal successful! New Balance:", accounts[acc]['balance'])
            else:
                print("Insufficient balance!")
        else:
            print("Account not found.")
            
    elif ch == '4':
        acc = input("Enter account number: ")
        if acc in accounts:
            print("\nAccount Holder:", accounts[acc]['name'])
            print("Current Balance:", accounts[acc]['balance'])
            print("Transaction History:")
            for h in accounts[acc]['history']:
                print(" -", h)
        else:
            print("Account not found.")
            
    elif ch == '5':
        save_bank(accounts)
        print("Bank records saved. Exiting...")
        break
    else:
        print("Invalid choice, try again.")
        