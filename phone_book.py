import json
import os

file_name = "contacts.json"

def load_contacts():
    if not os.path.exists(file_name):
        return {}
    with open(file_name, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_contact(contacts):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False)

def add_contacts(contacts):
    name = input("Contact name: ")
    phone = int(input("Phone number: "))
    if name in contacts:
        change = input("contact already exist do you want to chane the number (y/n): ").lower()
        if change == "n" :
            print("Cancelled")
            return
    contacts[name] = phone
    save_contact(contacts)
    print(f"{name} Added")

def search_contact(contacts):
    name = input("The name of the contact you are looking for").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found")

def delete_contact(contacts):
    name = input("The name of the contact you are looking for").strip()
    if name in contacts:
        contacts.pop(name)
        save_contact(contacts)
        print(f"{name} contact deleted")
    else:
        print("Contact not found")

def show_all(contacts):
    if not contacts:
        print("contact is empty")
        return
    else:
        for name , phone in contacts.items:
            print(f"{name}: {phone}")
def phone_book():
    contacts = load_contacts()
    while True:
        choice = input("\nWhat do you want to do?\n"
        "a) Add contact\n"
        "s) Search contact\n"
        "d) Delete contact\n"
        "c) Show all\n"
        "x) Exit\n").lower()

        if choice == "a":
            add_contacts(contacts)
        elif choice == "s":
            search_contact(contacts)
        elif choice == "d":
            delete_contact(contacts)
        elif choice == "c":
            show_all(contacts)
        elif choice == "x":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    phone_book()
