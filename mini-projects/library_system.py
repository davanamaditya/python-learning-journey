 # Library Management System
import json

def load_books():
    try:
        with open('library.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_books(books):
    with open('library.json', 'w') as f:
        json.dump(books, f, indent=4)

books = load_books()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Save & Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        bid = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        books.append({"id": bid, "title": title, "author": author, "status": "Available"})
        print("Book added successfully!")
        
    elif choice == '2':
        q = input("Search by ID or Title: ").lower()
        matched = [b for b in books if q in b['id'].lower() or q in b['title'].lower()]
        if matched:
            for b in matched:
                print(b)
        else:
            print("No books found.")
            
    elif choice == '3':
        bid = input("Enter Book ID to issue: ")
        for b in books:
            if b['id'] == bid:
                if b['status'] == "Available":
                    b['status'] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
                break
        else:
            print("Book ID not found.")
            
    elif choice == '4':
        bid = input("Enter Book ID to return: ")
        for b in books:
            if b['id'] == bid:
                b['status'] = "Available"
                print("Book returned successfully!")
                break
        else:
            print("Book ID not found.")
            
    elif choice == '5':
        print("\nAvailable Books:")
        avail_found = False
        for b in books:
            if b['status'] == "Available":
                print(b)
                avail_found = True
        if not avail_found:
            print("No books currently available.")
                
    elif choice == '6':
        save_books(books)
        print("Library data saved. Exiting...")
        break
    else:
        print("Invalid choice, try again.")