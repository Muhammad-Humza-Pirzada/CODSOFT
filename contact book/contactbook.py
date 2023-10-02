class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"""
            _______________________________
            | Contact added successfully. |
            ```````````````````````````````
            """)

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, updated_contact):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.name = updated_contact.name
                contact.phone = updated_contact.phone
                contact.email = updated_contact.email
                contact.address = updated_contact.address
                print(f"""
            _______________________________
            | Contact updated successfully. |
            ```````````````````````````````
            """)
                return
        print(f"""
            ______________________
            | Contact not found. |
            ``````````````````````
            """)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"""
            _______________________________
            | Contact deleted successfully. |
            ```````````````````````````````
            """)
                return
        print(f"""
            ______________________
            | Contact not found. |
            ``````````````````````
            """)
        
    def show_contacts(self):
        if self.contacts:
            print("""
            _____________________
            |   All Contacts:   |
            `````````````````````""")
            for index, contact in enumerate(self.contacts):
                print(f"""
            __________________________________________________________________________________________
            {index+1}. Name: {contact.name} | Phone: {contact.phone} | Email: {contact.email} | Address: {contact.address}""")
        else:
            print("No contacts available.")

def main():
    contact_book = ContactBook()

    while True:
        print(f"""
                ________________________
                | Contact Book Menu:   |
                | 1. Add Contact.      |
                | 2. Search Contact.   |
                | 3. Update Contact.   |
                | 4. Delete Contact.   |
                | 5. Show All Contacts |
                | 6. Exit.             |
                ````````````````````````
            
            """)
        

        choice = input(
            f"""
            ~~~~~~~Enter Your Choice~~~~~~~
            ```````````````````````````````
            """
        )

        if choice == "1":
            name = input(f"""
            ~~~~~~~Enter Name:~~~~~
            ```````````````````````
                    """)
            phone = input(f"""
            ~~~~~~~Enter Phone:~~~~ 
            ```````````````````````
                    """)
            email = input(f"""
            ~~~~~~~Enter Email:~~~~
            ```````````````````````
                    """)
            address = input(f"""
            ~~~~~~~Enter Address:~~~
            ````````````````````````
                    """)
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            keyword = input(f"""
            ~~~~~~~Enter search keyword: ~~~~
            `````````````````````````````````
                    
                    """)
            found_contacts = contact_book.search_contact(keyword)
            if found_contacts:
                print(f"""      
            ~~~~~~Search Results:~~~~~~
            ```````````````````````````""")
                for contact in found_contacts:
                    print(f"""
            _______________________________________________
            | Name: {contact.name}, 
            | Phone: {contact.phone},
            | Email: {contact.email},
            | Address: {contact.address}
            ```````````````````````````````````````````````
            """)
            else:
                print(f"""
            _______________________________ 
            | No matching contacts found. |
            ```````````````````````````````
            """)

        elif choice == "3":
            name = input(f"""
            ~~~~~Enter the name of the contact to update:~~~~~
            ``````````````````````````````````````````````````
                        """)
            updated_name = input(f"""
            ~~~~~Enter updated Name: ~~~~~~
            ```````````````````````````````
                        """)
            updated_phone = input(f"""
            ~~~~~Enter updated Phone: ~~~~~
            ```````````````````````````````
                        """)
            updated_email = input(f"""
            ~~~~~Enter updated Email: ~~~~~
            ```````````````````````````````
                        """)
            updated_address = input(f"""
            ~~~~~Enter updated Address: ~~~~
            ````````````````````````````````
                        """)
            updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
            contact_book.update_contact(name, updated_contact)

        elif choice == "4":
            name = input(f"""
            ~~~~~Enter the name of the contact to delete: ~~~~~
            ```````````````````````````````````````````````````
                        """)
            contact_book.delete_contact(name)
        
        elif choice == "5":
            contact_book.show_contacts()

        elif choice == "6":
            print(f"""
                 ___________________________
                | Exiting the Contact Book. |
                `````````````````````````````
                """)
            break

        else:
            print(f"""
                _____________________________________
                | Invalid choice. Please try again. |
                `````````````````````````````````````
                """)

if __name__ == "__main__":
    main()
