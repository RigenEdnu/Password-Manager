import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import keyboard

# ambil data user, password dari data.json
import json
with open("data.json", "r") as file:
    data = json.load(file)
    auth = data["auth"]

# Halaman Login
login = tk.Tk()
login.title('Password Manager')
login.geometry('925x500+300+200')
login.configure(bg="#fff")

def auth():
    for widget in login.winfo_children():
        widget.pack_forget

    # Load Image login
    img = PhotoImage(file='login.png')
    Label(login, image=img, bg='white').place(x=70, y=50)

    # Frame sign in, sign up
    frame = Frame(login, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
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

    # Sign in Button
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

    # Sign up Button
    sign_up_button = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: open_signup(login))
    sign_up_button.place(x=215, y=270)

    # Prototipe untuk show_main_menu password manager
    def disable_enter_key():
        keyboard.unhook_all()

    def open_signup(parent):
        for widget in parent.winfo_children():
            widget.destroy()

        img = PhotoImage(file='sign_up.png')
        Label(login, image=img, bg='white').place(x=70, y=50)

        sign_up_frame = Frame(parent, width=350, height=390, bg="white")
        sign_up_frame.place(x=480, y=50)

        heading = Label(sign_up_frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        # Input Username
        username_placeholder = "Username"
        user_signup = Entry(sign_up_frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        user_signup.insert(0, username_placeholder)
        user_signup.place(x=30, y=80)

        def on_enter_username_signup(e):
            if user_signup.get() == username_placeholder:
                user_signup.delete(0, 'end')
                user_signup.configure(show="")
                user_signup.configure(fg="black")

        def on_leave_username_signup(e):
            if user_signup.get() == "":
                user_signup.insert(0, username_placeholder)
                user_signup.configure(show="")
                user_signup.configure(fg="gray")

        user_signup.bind('<FocusIn>', on_enter_username_signup)
        user_signup.bind('<FocusOut>', on_leave_username_signup)
        Frame(sign_up_frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Input Password
        password_placeholder = "Password"
        pw_signup = Entry(sign_up_frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        pw_signup.insert(0, password_placeholder)
        pw_signup.place(x=30, y=150)

        def on_enter_password_signup(e):
            if pw_signup.get() == password_placeholder:
                pw_signup.delete(0, 'end')
                pw_signup.configure(show="*")
                pw_signup.configure(fg="black")

        def on_leave_password_signup(e):
            if pw_signup.get() == "":
                pw_signup.insert(0, password_placeholder)
                pw_signup.configure(show="")
                pw_signup.configure(fg="gray")

        pw_signup.bind('<FocusIn>', on_enter_password_signup)
        pw_signup.bind('<FocusOut>', on_leave_password_signup)
        Frame(sign_up_frame, width=295, height=2, bg="black").place(x=25, y=177)

        # Confirm Password
        confirm_password_placeholder = "Confirm Password"
        confirm_pw_signup = Entry(sign_up_frame, width=25, fg='gray', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        confirm_pw_signup.insert(0, confirm_password_placeholder)
        confirm_pw_signup.place(x=30, y=220)

        def on_enter_confirm_password_signup(e):
            if confirm_pw_signup.get() == confirm_password_placeholder:
                confirm_pw_signup.delete(0, 'end')
                confirm_pw_signup.configure(show="*")
                confirm_pw_signup.configure(fg="black")

        def on_leave_confirm_password_signup(e):
            if confirm_pw_signup.get() == "":
                confirm_pw_signup.insert(0, confirm_password_placeholder)
                confirm_pw_signup.configure(show="")
                confirm_pw_signup.configure(fg="gray")

        confirm_pw_signup.bind('<FocusIn>', on_enter_confirm_password_signup)
        confirm_pw_signup.bind('<FocusOut>', on_leave_confirm_password_signup)
        Frame(sign_up_frame, width=295, height=2, bg="black").place(x=25, y=247)

        # Sign up Button
        Button(sign_up_frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white ', border=0, cursor='hand2').place(x=35, y=280)
        label = Label(sign_up_frame, text="Sudah memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=80, y=340)

        # Sign in Button
        sign_in_button = Button(sign_up_frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 9), border=0, cursor='hand2', command=lambda: auth())
        sign_in_button.place(x=210, y=340)

def show_main_menu():

    welcome_label = Label(login, text="Selamat Datang!", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',  23, 'bold'))
    welcome_label.pack(pady=50)

    create_button = Button(login, width=39, pady=7, text='Create', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    create_button.pack(pady=10)

    update_button = Button(login, width=39, pady=7, text='Update', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    update_button.pack(pady=10)

    delete_button = Button(login, width=39, pady=7, text='Delete', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    delete_button.pack(pady=10)

    logout_button = Button(login, width=39, pady=7, text='LogOut', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=open_signup)
    logout_button.pack(pady=10)

    login.mainloop()

auth()