import tkinter as tk
from tkinter import messagebox, simpledialog

contacts={}

#TO ADD CONTACT DETAILS

def add_contacts():
    name=entry_name.get()
    phone=entry_phone.get()
    email=entry_email.get()
    address=entry_address.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning","Name and phone are requires!")
        return

    contacts[name]={"phone":phone,"email":email,"address":address}
    messagebox.showinfo("Success","Contact added successfully!")
    clear_fields()
    view_contacts()

#TO VIEW CONTACT DETAILS

def view_contacts():
    listbox.delete(0,tk.END)
    for name,info in contacts.items():
        listbox.insert(tk.END,f"{name}-{info['phone']}")

#TO SEARCH CONTACT DETAILS

def search_contacts():
    key=simpledialog.askstring("Search","Enter name or phone number : ")

    if key:
        for name,info in contacts.items():
            if key.lower() == name.lower() or key == info["phone"]:
                messagebox.showinfo("Contact Found",f"Name:{name}\nphone: {info['phone']}\nEmail:{info['email']}\nAddress:{info['address']}")
                return
        messagebox.showinfo("Not Found","No matching contact found.")

#TO UPDATE THE CONTACTS

def update_contact():
    name=simpledialog.askstring("Update","Enter name of contact to update:")
    if name in contacts:
        info=contacts[name]
        new_phone=simpledialog.askstring("Phone", f"New phone ({info['phone']}):") or info['phone']
        new_email = simpledialog.askstring("Email", f"New email ({info['email']}):") or info['email']
        new_address = simpledialog.askstring("Address", f"New address ({info['address']}):") or info['address']

        contacts[name]={"phone":new_phone,"email":new_email,"address":new_address}

        messagebox.showinfo("Success","Contact updated successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error","Contact not found!")

#TO DELETE THE CONTACT
        
def delete_contact():
    name=simpledialog.askstring("Delete","Enter name of contact to delete:")
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success","contact deleted!")
        view_contacts()
    else:
        messagebox.showerror("Error","Contact not found!")

#TO CLEAR THE FIELDS

def clear_fields():
    entry_name.delete(0,tk.END)
    entry_phone.delete(0,tk.END)
    entry_email.delete(0,tk.END)
    entry_address.delete(0,tk.END)


app=tk.Tk()
app.title("Contact Book AApplication")
app.geometry("450x500")
app.config(bg="#E8F6F3")

#LABELS AND ENTRY FIELDS

tk.Label(app,text="Name:",bg="#E8F6F3").pack()
entry_name=tk.Entry(app,width=40)
entry_name.pack()

tk.Label(app,text="Phone:",bg="#E8F6F3").pack()
entry_phone=tk.Entry(app,width=40)
entry_phone.pack()

tk.Label(app,text="Email:",bg="#E8F6F3").pack()
entry_email=tk.Entry(app,width=40)
entry_email.pack()

tk.Label(app,text="Address:",bg="#E8F6F3").pack()
entry_address=tk.Entry(app,width=40)
entry_address.pack()

#BUTTINS

tk.Button(app,text="Add Contact",width=20,command=add_contacts).pack(pady=5)
tk.Button(app,text="View Contacts",width=20,command=view_contacts).pack(pady=5)
tk.Button(app,text="Search Contact",width=20,command=search_contacts).pack(pady=5)
tk.Button(app,text="Update Contact",width=20,command=update_contact).pack(pady=5)
tk.Button(app,text="Delete Contact",width=20,command=delete_contact).pack(pady=5)

#CONTACT LIST DISPLAY

listbox=tk.Listbox(app,width=50,height=12)
listbox.pack(pady=10)

app.mainloop()
