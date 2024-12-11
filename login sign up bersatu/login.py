import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import keyboard
import os
import json

with open("data.json", "r") as file:
    data = json.load(file)
    auth_data = data["auth"]

# Frame page
app = tk.Tk()
app.title('Login')
app.geometry('925x500+300+200')
app.configure(bg="#fff")

def show_login_page():
    for widget in app.winfo_children():
        widget.destroy()

    img = PhotoImage(file="login.png")
    app.img = img
    Label(app, image=img, bg='white').place(x=70, y=50)

    frame = Frame(app, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

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

    def validate_and_signin():
        with open("data.json", "r") as file:
            data = json.load(file)
            auth = data["auth"]

        username = user.get()
        password = pw.get()

        if username == auth["username"] and password == auth["password"]:
            show_main_menu()
        else:
            messagebox.showerror("Error", "username atau password salah")

    def on_key_press(event):
        if event.name == 'enter':
            validate_and_signin()
    keyboard.on_press(on_key_press)

    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=validate_and_signin).place(x=35, y=204)
    label = Label(frame, text="Belum memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_sign_up_page)
    sign_up.place(x=215, y=270)

def show_sign_up_page():
    for widget in app.winfo_children():
        widget.destroy()

    img = PhotoImage(file='sign_up.png')
    app.img = img
    Label(app, image=img, bg='white').place(x=50, y=60)

    frame = Frame(app, width=350, height=390, bg="white")
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

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

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, cursor='hand2').place(x=35, y=280)
    label = Label(frame, text="Sudah memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=80, y=340)

    sign_in = Button(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 9), border=0, cursor='hand2', command=show_login_page)
    sign_in.place(x=210, y=340)

def show_main_menu():
    keyboard.unhook_all()
    for widget in app.winfo_children():
        widget.destroy()

    app.geometry('925x500+300+200')
    app.configure(bg="#fff")

    welcome_label = Label(app, text="Selamat Datang!", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    welcome_label.pack(pady=50)

    create_button = Button(app, width=39, pady=7, text='Generate Password', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    create_button.pack(pady=10)

    delete_button = Button(app, width=39, pady=7, text='Save Passowrd', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    delete_button.pack(pady=10)

    update_button = Button(app, width=39, pady=7, text='Storage', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    update_button.pack(pady=10)

    logout_button = Button(app, width=39, pady=7, text='LogOut', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=show_login_page)
    logout_button.pack(pady=10)

show_login_page()
app.mainloop()
