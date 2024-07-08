from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.messagebox as tmsg

class ContactBook:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def AddContact(self, name, phone_number, email, address):
        contact = ContactBook(name, phone_number, email, address)
        self.contacts.append(contact)
        return True

    def ViewContact(self):
        if not self.contacts:
            return "Contact not found or Contact not added before"
        else:
            contacts_list = "Contact List is here:\n"
            for index, contact in enumerate(self.contacts, start=1):
                contacts_list += f"{index}. Name: {contact.name} - Contact Number: {contact.phone_number}"
            return contacts_list

    def SearchContact(self, search):
        Searched_Contact = [contact for contact in self.contacts if search in contact.name or search in contact.phone_number]
        if not Searched_Contact:
            return "Invalid search. Contact not found."
        else:
            results = ""
            for index, contact in enumerate(Searched_Contact, start=1):
                results += f"{index}. Name: {contact.name} - Phone Number: {contact.phone_number}\n"
            return results
        

    def UpdateContact(self, name, phone_number, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = phone_number
                contact.email = email
                contact.address = address
                return True
        return False

    def DeleteContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

class ContactBookApp:
    def __init__(self, root):
        self.manager = ContactManager()
        self.root = root
        self.root.config(bg="light blue")
        self.root.geometry("500x1000")
        self.root.title("Contact Book Manager")
        self.root.wm_iconbitmap("icon.ico")
        self.create_widgets()

        
    def create_widgets(self):
        
        self.title_label = Label(self.root, text="Contact Book", fg="black", font="italic 18 bold", background="light blue" )
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.name_label = Label(self.root, text="Name:", font="italic 12", background="light blue")
        self.name_label.grid(row=1,column=0, padx=2, pady=2)
        self.name_entry = Entry(self.root)
        self.name_entry.grid(row=1, column=1,padx=2, pady=2)

        self.phone_label = Label(self.root, text="Phone Number:", font="italic 12", background="light blue")
        self.phone_label.grid(row=2, column=0,padx=2, pady=2)
        self.phone_entry = Entry(self.root)
        self.phone_entry.grid(row=2, column=1,padx=2, pady=2)

        self.email_label = Label(self.root, text="Email:", font="italic 12", background="light blue")
        self.email_label.grid(row=3, column=0,padx=2, pady=2)
        self.email_entry = Entry(self.root)
        self.email_entry.grid(row=3, column=1,padx=2, pady=2)

        self.address_label = Label(self.root, text="Address:", font="italic 12", background="light blue")
        self.address_label.grid(row=4, column=0,padx=2, pady=2)
        self.address_entry = Entry(self.root)
        self.address_entry.grid(row=4, column=1,padx=2, pady=4)

        self.contacts_listbox = Listbox(self.root)
        self.contacts_listbox.grid(row=5, column=2, rowspan=20, padx=10, pady=20, ipadx=30, ipady=50)

        self.add_button = Button(self.root, text="Add Contact",font="italic 12", command=self.AddContact, background="light pink")
        self.add_button.grid(row=6, column=0, padx=15, pady=10)

        self.view_button = Button(self.root, text="View Contact",font="italic 12", command=self.ViewContact, background="light pink")
        self.view_button.grid(row=7, column=0, padx=10, pady=10)

        self.search_button = Button(self.root, text="Search Contact",font="italic 12", command=self.SearchContact, background="light pink")
        self.search_button.grid(row=8, column=0, padx=10, pady=10)

        self.update_button = Button(self.root, text="Update Contact",font="italic 12", command=self.UpdateContact, background="light pink")
        self.update_button.grid(row=9, column=0, padx=10, pady=10)

        self.delete_button = Button(self.root, text="Delete Contact",font="italic 12", command=self.DeleteContact, background="light pink")
        self.delete_button.grid(row=10, column=0, padx=10, pady=10) 


    def AddContact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if self.manager.AddContact(name, phone_number, email, address):
            tmsg.showinfo("Success", "Contact added successfully!")
            self.ClearEntries()
        else:
            tmsg.showerror("Error", "Failed to add contact.")

    def ViewContact(self):
        self.contacts_listbox.delete(0, END)
        contacts = self.manager.ViewContact()
        for contact in self.manager.contacts:
            self.contacts_listbox.insert(END, f"{contact.name} - {contact.phone_number}")

    def SearchContact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number to search: ")
        if search_term:
            self.contacts_listbox.delete(0, END)
            for contact in self.manager.contacts:
                if search_term in contact.name or search_term in contact.phone_number:
                    self.contacts_listbox.insert(END, f"{contact.name} - {contact.phone_number}")
            if not self.contacts_listbox.size():
                tmsg.showinfo("No contact found, Enter valid information")
            

    def UpdateContact(self):
        oldname = simpledialog.askstring("Update Contact", "Enter the name or phone number to update: ")
        if oldname:
            newname = self.name_entry.get()
            phone_number= self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if self.manager.UpdateContact(oldname, phone_number, email, address):
                tmsg.showinfo("Contact Updated Successfully")
                self.ClearEntries()
            else:
                tmsg.showerror("Contact Not Found") 
        

    def DeleteContact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if name:
            if self.manager.DeleteContact(name):
                tmsg.showinfo("Success", "Contact deleted successfully!")
                self.view_contacts()
            else:
                tmsg.showerror("Error", "Contact not found.")

    def ClearEntries(self):
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = ContactBookApp(root)
    root.mainloop()
    



    
























            




