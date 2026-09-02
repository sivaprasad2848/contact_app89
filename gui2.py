import tkinter as tk
from tkinter import ttk

# Function to submit data
def submit():
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()

    # Check for empty fields
    if name == "" or email == "" or mobile == "":
        return

    # Print in Command Prompt
    print("----- User Details -----")
    print("Name   :", name)
    print("Email  :", email)
    print("Mobile :", mobile)
    print("------------------------")

    # Insert into table
    table.insert("", "end", values=(name, email, mobile))

    # Clear entry fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("700x450")

# Form Frame
form = ttk.Frame(root, padding=10)
form.pack(fill="x")

# Name
ttk.Label(form, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(form, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Email
ttk.Label(form, text="Email").grid(row=1, column=0, padx=5, pady=5)
email_entry = ttk.Entry(form, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Mobile
ttk.Label(form, text="Mobile").grid(row=2, column=0, padx=5, pady=5)
mobile_entry = ttk.Entry(form, width=30)
mobile_entry.grid(row=2, column=1, padx=5, pady=5)

# Submit Button
submit_btn = ttk.Button(form, text="Submit", command=submit)
submit_btn.grid(row=3, column=1, pady=10)

# Table Frame
table_frame = ttk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create Table
columns = ("Name", "Email", "Mobile")
table = ttk.Treeview(table_frame, columns=columns, show="headings")

table.heading("Name", text="Name")
table.heading("Email", text="Email")
table.heading("Mobile", text="Mobile")

table.column("Name", width=180)
table.column("Email", width=250)
table.column("Mobile", width=150)

# Scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)

table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()