# Contact Management System

contacts = []

def show_menu():
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\n--- Contact List ---")
        for idx, c in enumerate(contacts, start=1):
            print(f"{idx}. {c['name']} - {c['phone']}")

def search_contact():
    keyword = input("\nEnter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c['name'].lower() or keyword in c['phone']:
            print("\n--- Contact Found ---")
            print(f"Name    : {c['name']}")
            print(f"Phone   : {c['phone']}")
            print(f"Email   : {c['email']}")
            print(f"Address : {c['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    phone = input("\nEnter the phone number of the contact to update: ")
    for c in contacts:
        if c['phone'] == phone:
            print("Enter new details (leave blank to keep current):")
            name = input(f"Name ({c['name']}): ") or c['name']
            email = input(f"Email ({c['email']}): ") or c['email']
            address = input(f"Address ({c['address']}): ") or c['address']
            c.update({'name': name, 'email': email, 'address': address})
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    phone = input("\nEnter the phone number of the contact to delete: ")
    for c in contacts:
        if c['phone'] == phone:
            contacts.remove(c)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main Program Loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
