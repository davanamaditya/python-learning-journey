 # Student Management System
import json

def load_data():
    try:
        with open('students.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)

students = load_data()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student Records")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Save & Exit")
    
    ch = input("Enter your choice: ")
    
    if ch == '1':
        sid = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        students.append({"id": sid, "name": name, "age": age, "marks": marks})
        print("Student added successfully!")
        
    elif ch == '2':
        if len(students) == 0:
            print("No student records found.")
        else:
            for s in students:
                print(s)
                
    elif ch == '3':
        s_id = input("Enter ID to search: ")
        found = False
        for s in students:
            if s['id'] == s_id:
                print("Found:", s)
                found = True
                break
        if not found:
            print("Student not found.")
            
    elif ch == '4':
        s_id = input("Enter ID to update: ")
        for s in students:
            if s['id'] == s_id:
                s['name'] = input("Enter new name: ")
                s['marks'] = float(input("Enter new marks: "))
                print("Record updated successfully!")
                break
        else:
            print("Student ID not found.")
            
    elif ch == '5':
        s_id = input("Enter ID to delete: ")
        for s in students:
            if s['id'] == s_id:
                students.remove(s)
                print("Student record deleted.")
                break
        else:
            print("Student ID not found.")
            
    elif ch == '6':
        if len(students) == 0:
            print("No students available to calculate average.")
        else:
            total = sum(s['marks'] for s in students)
            avg = total / len(students)
            print(f"Class Average Marks: {avg:.2f}")
            
    elif ch == '7':
        save_data(students)
        print("Data saved. Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")