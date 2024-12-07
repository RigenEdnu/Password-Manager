import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import getpass

# Halaman Login
login=tk.Tk()
login.title('Login')
login.geometry('925x500+300+200')
login.configure(bg="#fff")

def signin():
    username = user.get()
    password = pw.get()

    if username == 'admin' and password == '1234':
        print('Welcome to Password Manager')
        screen = Toplevel(login)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello Everyone!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()

# load Image login
img = PhotoImage(file='login.png')
Label(login, image=img, bg='white').place(x=50,y=50)

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
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=signin).place(x=35, y=204)
label=Label(frame, text="Belum memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

# Sign up Button
sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

login.mainloop()