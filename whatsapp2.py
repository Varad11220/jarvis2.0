import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import webbrowser
import sys
from main import talk
def open_whatsapp(number, message):
    encoded_message = message.replace(" ", "%20")
    whatsapp_link = f"https://wa.me/{number}?text={encoded_message}"
    webbrowser.open(whatsapp_link)
    sys.exit()

def load_contacts(filename):
    with open(filename, 'r') as file:
        contacts = json.load(file)
    return contacts

def on_contact_selected():
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_contact = contact_listbox.get(selected_index)
        number = selected_contact.split(": ")[1]
        message = None
        message = simpledialog.askstring("Input", "Enter your message:")
        open_whatsapp(number, message)
        talk(f"Opening whatsapp to send message to {selected_contact}")
            
def create_contact_list_gui(contacts):
    root = tk.Tk()
    root.title("WhatsApp Contact List")

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    contact_label = tk.Label(frame, text="Select a contact:")
    contact_label.pack()

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    global contact_listbox
    contact_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, width=40, font=('Arial', 14))
    contact_listbox.pack(fill=tk.BOTH, expand=True)
    contact_listbox.bind('<Double-Button-1>', lambda event: on_contact_selected())

    scrollbar.config(command=contact_listbox.yview)

    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']}: {contact['phone']}")

    root.mainloop()


