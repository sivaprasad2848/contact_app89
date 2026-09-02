import tkinter as tk
from tkinter import ttk

# Function to display data in the command prompt
def submit():
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()

    print("----- User Details -----")
    print("Name   :", name)
    print("Email  :", email)
    print("Mobile :", mobile)
    print("------------------------")


# Create main window
root = tk.Tk()
root.title("AI Studio")
root.geometry("400x250")
root.minsize(320, 240)

# Name
ttk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = ttk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Email
ttk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10, sticky="w")
email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Mobile
ttk.Label(root, text="Mobile").grid(row=2, column=0, padx=10, pady=10, sticky="w")
mobile_entry = ttk.Entry(root, width=30)
mobile_entry.grid(row=2, column=1, padx=10, pady=10)

# Submit Button
submit_btn = ttk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=3, column=1, padx=10, pady=20)

root.mainloop()