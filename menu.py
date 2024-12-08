import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import os

# File to store passwords persistently
PASSWORD_FILE = "passwords.txt"

# Function to load passwords from the file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return file.read().splitlines()
    return []

# Function to save passwords to the file
def save_passwords():
    with open(PASSWORD_FILE, "w") as file:
        for password in stored_passwords:
            file.write(password + "\n")

# Function to generate password
def passgen(length):
    try:
        length = int(length)
        if length <= 0:
            show_error("Password length must be greater than 0.")
            return
        
        huruf = string.ascii_letters
        numbers = string.digits
        symbol = string.punctuation
        characters = huruf + numbers + symbol
        password = ''.join(random.choice(characters) for _ in range(length))
        show_password(password)
    except ValueError:
        show_error("Please enter a valid number for password length.")

# Function to show error message
def show_error(message):
    messagebox.showerror("Error", message)

# Function to show the generated password
def show_password(password):
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

# Function to copy password to clipboard
def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(password_entry.get())
    app.update()

# fungsi copy password ke clipboard
def copy_password():
    try:
        selected_index = password_listbox.curselection()[0]
        app.clipboard_clear()
        app.clipboard_append(stored_passwords[selected_index])
        app.update()
        messagebox.showinfo("Success", "Password telah disalin di clipboard")
    except IndexError:
        messagebox.showwarning("Warning", "Tidak ada password yang dipilih")

# Function to save password
def save_password():
    password = password_entry.get()
    if password:
        stored_passwords.append(password)
        update_password_list()
        save_passwords()  # Save passwords to file
        messagebox.showinfo("Success", "Password saved successfully!")
        clear_password_field()
    else:
        messagebox.showwarning("Peringatan", "No password to save!")

# Function to clear the password input field
def clear_password_field():
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

# Function to update the list of stored passwords
def update_password_list():
    password_listbox.delete(0, tk.END)
    for password in stored_passwords:
        password_listbox.insert(tk.END, password)

# Function to delete a selected password
def delete_password():
    try:
        selected_index = password_listbox.curselection()[0]
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected password?")
        if confirm:
            del stored_passwords[selected_index]
            update_password_list()
            save_passwords()  # Save the updated list to file
            messagebox.showinfo("Success", "Password deleted successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "No password selected!")


# Main window
app = tk.Tk()
app.title("Password Manager")
app.geometry("500x600")
app.configure(bg="#121212")

# List to store passwords
stored_passwords = load_passwords()  # Load stored passwords from file


# Header
header_frame = tk.Frame(app, bg="#075E54", height=50)
header_frame.pack(fill=tk.X)

header_label = tk.Label(
    header_frame,
    text="Password Manager",
    bg="#075E54",
    fg="white",
    font=("Arial", 20, "bold"),
)
header_label.pack(pady=10)

# Notebook for tabs
notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill=tk.BOTH)

# Tab for Password Generation
password_tab = tk.Frame(notebook, bg="#121212")
notebook.add(password_tab, text="Generate Password")

# Tab for Password Storage
storage_tab = tk.Frame(notebook, bg="#121212")
notebook.add(storage_tab, text="Stored Passwords")

# Password generation UI
gen_label = tk.Label(password_tab, text="Enter Password Length:", bg="#121212", fg="white")
gen_label.pack(padx=10, pady=10)

length_entry = tk.Entry(password_tab, width=20)
length_entry.pack(padx=10, pady=10)

generate_button = tk.Button(password_tab, text="Generate Password", command=lambda: passgen(length_entry.get()))
generate_button.pack(padx=10, pady=10)

password_entry = tk.Entry(password_tab, width=30, state="readonly")
password_entry.pack(padx=10, pady=10)

copy_button = tk.Button(password_tab, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(padx=10, pady=10)

save_button = tk.Button(password_tab, text="Save Password", command=save_password)
save_button.pack(padx=10, pady=10)

# Stored passwords UI
password_listbox = tk.Listbox(storage_tab, width=50, height=10)
password_listbox.pack(padx=10, pady=10)

delete_button = tk.Button(storage_tab, text="Copy Password", command=copy_password)
delete_button.pack(padx=10, pady=10)

delete_button = tk.Button(storage_tab, text="Delete Selected Password", command=delete_password)
delete_button.pack(padx=10, pady=10)

# Update the list of stored passwords initially
update_password_list()

# Run the application
app.mainloop()
