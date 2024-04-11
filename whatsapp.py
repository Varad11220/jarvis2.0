import tkinter as tk
import json

def save_data():
    global entry_name, entry_phone  # Declare entry_name and entry_phone as global
    
    name = entry_name.get()
    phone = entry_phone.get()
    
    # Load existing data from the JSON file, if it exists
    try:
        with open("data.json", "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []
    
    # If existing_data is not a list (e.g., if the file was empty), make it a list
    if not isinstance(existing_data, list):
        existing_data = []
    
    # Append the new data to the existing data
    existing_data.append({"name": name, "phone": phone})
    
    # Write the updated data back to the JSON file
    with open("data.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=4)
    
    # Clear the entry fields after saving
    from talker import talk
    talk(f"{name} added successfully to the contact list")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    
    # Optionally, provide a confirmation message
    print("Data saved successfully!")
    
    # Close the UI
    root.destroy()


def add_number():
    global entry_name, entry_phone, root  # Declare entry_name, entry_phone, and root as global
    
    root = tk.Tk()
    root.title("Enter Name and Phone Number")

    # Create labels and entry fields for name and phone number
    label_name = tk.Label(root, text="Name:")
    label_name.grid(row=0, column=0, padx=5, pady=5)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    label_phone = tk.Label(root, text="Phone Number:")
    label_phone.grid(row=1, column=0, padx=5, pady=5)
    entry_phone = tk.Entry(root)
    entry_phone.grid(row=1, column=1, padx=5, pady=5)

    # Create a submit button
    submit_button = tk.Button(root, text="Submit", command=save_data)
    submit_button.grid(row=2, columnspan=2, padx=5, pady=5)

    root.mainloop()
    

def search_number(name):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

        # Function to get phone number by name
        for entry in data:
            if entry['name'] == name:
                return entry['phone']
        return None  # Return None if name is not found

        # Example usage:
        
    
    except FileNotFoundError:
        print("Data file not found!")
        
def send_message(number,message):
    import urllib.parse
    encoded_message = urllib.parse.quote(message)
    whatsapp_link = f'https://wa.me/{number}?text={encoded_message}'
    import webbrowser
    webbrowser.open(whatsapp_link)
    
    

# name_to_search = "varad"
# phone_number = search_number(name_to_search)
# if phone_number is not None:
#     print(f"The phone number for {name_to_search} is: {phone_number}")
# else:
#     print(f"No phone number found for {name_to_search}")