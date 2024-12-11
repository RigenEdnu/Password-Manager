import tkinter as tk
from tkinter import *
import customtkinter as ctk

sign_up = tk.Tk()
sign_up.title('Login')
sign_up.geometry('925x500+300+200')
sign_up.configure(bg="#fff")
sign_up.resizable(False, False)

img = PhotoImage(file='sign_up.png')
Label(sign_up, image=img, bg='white').place(x=50, y=60)

frame = Frame(sign_up, width=350, height=390, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Input Username
username_placeholder = "Username"
user = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.insert(0, username_placeholder)
user.place(x=30, y=80)

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

user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Input Password
password_placeholder = "Password"
pw = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
pw.insert(0, password_placeholder)
pw.place(x=30, y=150)

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

pw.bind('<FocusIn>', on_enter_password)
pw.bind('<FocusOut>', on_leave_password)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Confirm Password
confirm_password_placeholder = "Confirm Password"
confirm_pw = Entry(frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_pw.insert(0, confirm_password_placeholder)
confirm_pw.place(x=30, y=220)

def on_enter_confirm_password(e):
    if confirm_pw.get() == confirm_password_placeholder:
        confirm_pw.delete(0, 'end')
        confirm_pw.configure(show="*")
        confirm_pw.configure(fg="black")

def on_leave_confirm_password(e):
    if confirm_pw.get() == "":
        confirm_pw.insert(0, confirm_password_placeholder)
        confirm_pw.configure(show="")
        confirm_pw.configure(fg="gray")

confirm_pw.bind('<FocusIn>', on_enter_confirm_password)
confirm_pw.bind('<FocusOut>', on_leave_confirm_password)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

# Sign up Button
Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, cursor='hand2').place(x=35, y=280)
label = Label(frame, text="Belum memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=80, y=340)

# Sign in Button
sign_in = Button(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 9), border=0, cursor='hand2')
sign_in.place(x=210, y=340)

sign_up.mainloop()