 # Employee Payroll System
import json

def load_emp():
    try:
        with open('payroll.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_emp(data):
    with open('payroll.json', 'w') as f:
        json.dump(data, f, indent=4)

employees = load_emp()

while True:
    print("\n--- EMPLOYEE PAYROLL SYSTEM ---")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Calculate Salary & Generate Payslip")
    print("4. Save & Exit")
    
    choice = input("Enter option: ")
    
    if choice == '1':
        eid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        des = input("Enter Designation: ")
        sal = float(input("Enter Basic Salary: "))
        employees.append({"id": eid, "name": name, "designation": des, "basic": sal})
        print("Employee added successfully!")
        
    elif choice == '2':
        q = input("Search by ID or Name: ").lower()
        found = False
        for e in employees:
            if q in e['id'].lower() or q in e['name'].lower():
                print(e)
                found = True
        if not found:
            print("No matching employee found.")
            
    elif choice == '3':
        eid = input("Enter Employee ID for payslip: ")
        found = False
        for e in employees:
            if e['id'] == eid:
                basic = e['basic']
                hra = basic * 0.20
                da = basic * 0.10
                pf = basic * 0.05
                net = basic + hra + da - pf
                
                print("\n==============================")
                print("           PAYSLIP            ")
                print("==============================")
                print("Employee ID :", e['id'])
                print("Name        :", e['name'])
                print("Designation :", e['designation'])
                print("Basic Salary:", basic)
                print("HRA (20%)   : +", hra)
                print("DA (10%)    : +", da)
                print("PF (5%)     : -", pf)
                print("------------------------------")
                print("Net Salary  :", net)
                print("==============================\n")
                found = True
                break
        if not found:
            print("Employee ID not found.")
            
    elif choice == '4':
        save_emp(employees)
        print("Payroll data saved. Exiting...")
        break
    else:
        print("Invalid choice, try again.")