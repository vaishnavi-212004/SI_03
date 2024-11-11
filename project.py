import json
import os

# Define the Contact class
class Contact:
    def __init__(self, contact_id, name, phone, email):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Contact(ID: {self.contact_id}, Name: {self.name}, Phone: {self.phone}, Email: {self.email})"

    def to_dict(self):
        """Convert the Contact object to a dictionary."""
        return {
            "contact_id": self.contact_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        """Create a Contact object from a dictionary."""
        return Contact(data["contact_id"], data["name"], data["phone"], data["email"])

# Define the Contact Management System class
class ContactManager:
    def __init__(self, data_file="contacts.json"):
        self.data_file = data_file
        self.contacts = self.load_data()

    def load_data(self):
        """Load contact data from the JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return [Contact.from_dict(data) for data in json.load(file)]
        return []

    def save_data(self):
        """Save all contacts to the JSON file."""
        with open(self.data_file, "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def add_contact(self, name, phone, email):
        """Add a new contact."""
        contact_id = len(self.contacts) + 1  # Generate a new contact ID
        new_contact = Contact(contact_id, name, phone, email)
        self.contacts.append(new_contact)
        self.save_data()
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("No contacts in the system.")
        else:
            for contact in self.contacts:
                print(contact)

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        """Update an existing contact."""
        contact = self.get_contact_by_id(contact_id)
        if contact:
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            self.save_data()
            print(f"Contact ID {contact_id} updated successfully.")
        else:
            print(f"Contact with ID {contact_id} not found.")

    def delete_contact(self, contact_id):
        """Delete a contact by ID."""
        contact = self.get_contact_by_id(contact_id)
        if contact:
            self.contacts.remove(contact)
            self.save_data()
            print(f"Contact ID {contact_id} deleted successfully.")
        else:
            print(f"Contact with ID {contact_id} not found.")

    def search_contact(self, search_term):
        """Search for a contact by name."""
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found for '{search_term}'.")

    def get_contact_by_id(self, contact_id):
        """Get a contact by ID."""
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                return contact
        return None

# Main program for testing the contact management system
def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            contact_manager.add_contact(name, phone, email)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            contact_id = int(input("Enter contact ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            contact_manager.update_contact(contact_id, name or None, phone or None, email or None)

        elif choice == '4':
            contact_id = int(input("Enter contact ID to delete: "))
            contact_manager.delete_contact(contact_id)

        elif choice == '5':
            search_term = input("Enter name or part of the name to search: ")
            contact_manager.search_contact(search_term)

        elif choice == '6':
            print("Exiting the contact management system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
