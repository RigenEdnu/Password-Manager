import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import keyboard

import os
import json
with open ("data.json", "r") as file:
    data = json.load(file)
    auth = data["auth"]

# Halaman Login
login=tk.Tk()
login.title('Login')
login.geometry('925x500+300+200')
login.configure(bg="#fff")

# load Image login
img = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'login.png'))
Label(login, image=img, bg='white').place(x=70,y=50)

# Frame sign in, sign up
frame = Frame(login, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Input Username
def on_enter_username(e):
    if user.get() == username_placeholder:
        user.delete(0, 'end')
        user.configure(show="")
        user.configure(fg="black")

def on_leave_username(e):
    if user.get() == "":
        user.insert(0, username_placeholder)
        user.configure(show="")
        user.configure(fg="gray")

username_placeholder = "Username"
user = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.insert(0, username_placeholder)
user.place(x=30, y=80)
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Input Password
def on_enter_password(e):
    if pw.get() == password_placeholder:
        pw.delete(0, 'end')
        pw.configure(show="*")
        pw.configure(fg="black")

def on_leave_password(e):
    if pw.get() == "":
        pw.insert(0, password_placeholder)
        pw.configure(show="")
        pw.configure(fg="gray")

password_placeholder = "Password"
pw = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
pw.insert(0, password_placeholder)
pw.place(x=30, y=150)
pw.bind('<FocusIn>', on_enter_password)
pw.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Sign in Button
def validate_and_signin():
    with open("data.json", "r") as file:
        data = json.load(file)
        auth = data["auth"]

    username = user.get()
    password = pw.get()

    if username == auth["username"] and password == auth["password"]:
        menu()
    else:
        messagebox.showerror("Error", "username atau password salah")

# Sign in Button
def on_key_press(event):
    if event.name == 'enter':
        validate_and_signin()
keyboard.on_press(on_key_press)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=validate_and_signin).place(x=35, y=204)
label=Label(frame, text="Belum memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

# Sign up Button
sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)


# prototipe untuk menu password manager
def disable_enter_key():
    keyboard.unhook_all()

def menu():
    disable_enter_key()
    for widget in login.winfo_children():
        widget.destroy()

    login.geometry('925x500+300+200')
    login.configure(bg="#fff")

    welcome_label = Label(login, text="Selamat Datang!", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    welcome_label.pack(pady=50)

    create_button = Button(login, width=39, pady=7, text='Create', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    create_button.pack(pady=10)

    update_button = Button(login, width=39, pady=7, text='Update', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    update_button.pack(pady=10)

    delete_button = Button(login, width=39, pady=7, text='Delete', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    delete_button.pack(pady=10)
    
    logout_button = Button(login, width=39, pady=7, text='LogOut', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    logout_button.pack(pady=10)

login.mainloop()