import json
import os

class Contact:
    def __init__(self, name: str, mobile_number: int | None = None, home_number: int | None = None, email: str | None = None, address: str | None = None) -> None:
        self.name = name
        self.mobile = mobile_number
        self.home = home_number
        self.email = email
        self.address = address
        
    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'mobile_number': self.mobile,
            'home_number': self.home,
            'email': self.email,
            'address': self.address
        }

class ContactManager:
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)
        
    def remove_contact(self, name: str) -> None:
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        
    def update_contact(self, name: str, new_contact: Contact) -> None:
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[i] = new_contact
                break
                
    def get_contact(self, name: str) -> Contact | None:
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
        
    def list_contacts(self) -> list[Contact]:
        return self.contacts

class Data:
    @staticmethod
    def save_data(file_path: str, data: dict) -> None:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_data(file_path: str) -> dict:
        if os.path.exists(file_path):
            with open(file_path) as file:
                return json.load(file)
        return {}
    
    @staticmethod
    def delete_file(file_path: str) -> None:
        if os.path.exists(file_path):
            os.remove(file_path)

def main():
    contact_manager = ContactManager()
    data_file = "contacts.json"
    
    # Load existing contacts
    contacts_data = Data.load_data(data_file)
    for contact_info in contacts_data.get("contacts", []):
        contact = Contact(**contact_info)
        contact_manager.add_contact(contact)
    
    while True:
        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. Update Contact")
        print("4. List Contacts")
        print("5. Save and Exit")
        choice = input("Enter choice: ")
        
        if choice.strip() == "1":
            name = input("Enter name: ")
            mobile = input("Enter mobile number: ")
            home = input("Enter home number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, mobile or None, home or None, email or None, address or None)
            contact_manager.add_contact(contact)
            print("Contact added.")
        
        elif choice.strip() == "2":
            name = input("Enter name of contact to remove: ")
            contact_manager.remove_contact(name)
            print("Contact removed.")
        
        elif choice.strip() == "3":
            name = input("Enter name of contact to update: ")
            contact = contact_manager.get_contact(name)
            if contact:
                new_mobile = input(f"Enter new mobile number (current: {contact.mobile}): ")
                new_home = input(f"Enter new home number (current: {contact.home}): ")
                new_email = input(f"Enter new email (current: {contact.email}): ")
                new_address = input(f"Enter new address (current: {contact.address}): ")
                updated_contact = Contact(name, new_mobile or contact.mobile, new_home or contact.home, new_email or contact.email, new_address or contact.address)
                contact_manager.update_contact(name, updated_contact)
                print("Contact updated.")
            else:
                print("Contact not found.")
        
        elif choice.strip() == "4":
            for contact in contact_manager.list_contacts():
                print(f"Name: {contact.name}, Mobile: {contact.mobile}, Home: {contact.home}, Email: {contact.email}, Address: {contact.address}")
        
        elif choice.strip() == "5":
            # Save contacts to file
            contacts_data = {"contacts": [contact.to_dict() for contact in contact_manager.list_contacts()]}
            Data.save_data(data_file, contacts_data)
            print("Data saved. Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()