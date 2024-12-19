import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import keyboard
import json

# Frame page
app = tk.Tk()
app.title('Password Manager')
app.geometry('925x500+300+200')
app.configure(bg="#fff")
app.minsize(925, 500)  # Set minimum window size

# sign in page
def show_sign_in_page():
    keyboard.unhook_all()
    for widget in app.winfo_children():
        widget.destroy()

    # memuat gambar sign in
    img = PhotoImage(file="sign_in.png")
    app.img = img
    Label(app, image=img, bg='white').place(x=70, y=50)

    frame = Frame(app, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # username input sign in
    user = ctk.CTkEntry(frame, placeholder_text="Username", width=250, text_color='black', border_width=0, fg_color='white', font=('Microsoft YaHei UI Light', 16))
    user.place(x=30, y=80)
    ctk.CTkFrame(frame, width=295, height=2, bg_color="black").place(x=25, y=107)

    # password input
    pw = ctk.CTkEntry(frame, placeholder_text="Password", width=250, text_color='black', border_width=0, fg_color='white', font=('Microsoft YaHei UI Light', 16), show="*")
    pw.place(x=30, y=150)
    ctk.CTkFrame(frame, width=295, height=2, bg_color="black").place(x=25, y=177)

    # validasi dan sign in
    def validate_and_signin():
        with open("data.json", "r") as file:
            data = json.load(file)
            auth = data["auth"]

        username = user.get()
        password = pw.get()

        authenticated = False
        for user_data in auth:
            if username == user_data["username"] and password == user_data["password"]:
                authenticated = True
                show_main_menu()
                break

        if not authenticated:
            messagebox.showerror("Error", "username atau password salah")

    # event ketika tombol enter ditekan menjalankan fungsi validate_and_signin pada sign in page
    def on_key_press(event):
        if app.focus_get() is not None:
            if event.name == 'enter':
                validate_and_signin()
    keyboard.on_press(on_key_press)

    # tombol sign in
    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=validate_and_signin).place(x=35, y=204)
    label = Label(frame, text="Belum memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    # tombol sign up
    sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_sign_up_page)
    sign_up.place(x=215, y=270)

# sign up page
def show_sign_up_page():
    keyboard.unhook_all()
    for widget in app.winfo_children():
        widget.destroy()

    # memuat gambar sign up
    img = PhotoImage(file='sign_up.png')
    app.img = img
    Label(app, image=img, bg='white').place(x=50, y=60)

    frame = Frame(app, width=350, height=390, bg="white")
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # username input
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

    # password input
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

    # confirm password input
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

    # validasi sign_up
    def validate_and_signup():
        username = user.get()
        password = pw.get()
        confirm_password = confirm_pw.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Password tidak sama")
        else:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}

            if "auth" not in data:
                data["auth"] = []

            data["auth"].append({
                "id_user" : len(data["auth"]) + 1,
                "username" : username,
                "password" : password
            })
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

            messagebox.showinfo("Success", "Sign-up berhasil!")
            show_sign_in_page()

    confirm_pw.bind('<FocusIn>', on_enter_confirm_password)
    confirm_pw.bind('<FocusOut>', on_leave_confirm_password)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    def on_key_press(event):
        if app.focus_get() is not None:
            if event.name == 'enter':
                validate_and_signup()
    keyboard.on_press(on_key_press)

    # tombol sign up
    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=validate_and_signup).place(x=35, y=280)

    # tombol kembali ke sign in
    label = Label(frame, text="Sudah memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=80, y=340)
    sign_in = Button(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 9), border=0, cursor='hand2', command=show_sign_in_page)
    sign_in.place(x=210, y=340)

# main menu
def show_main_menu():
    keyboard.unhook_all()
    for widget in app.winfo_children():
        widget.destroy()

    # memuat gambar logo
    img = PhotoImage(file='logo.png')
    app.img = img
    Label(app, image=img, bg='white').place(x=3, y=1, anchor='nw')

    # label nama aplikasi
    app_name = Label(app, text="Password Manager", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 15, 'bold'))
    app_name.place(x=60, y=10)

    # label selamat datang
    welcome_label = Label(app, text="Selamat Datang!", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    welcome_label.pack(pady=50)

    # tombol generate password
    generate_button = Button(app, width=50, pady=10, text='Generate Password', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=pw_generate)
    generate_button.pack(pady=10)

    # tombol save password
    save_button = Button(app,  width=50, pady=10, text='Save Passowrd', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    save_button.pack(pady=10)

    # tombol archive password
    archive_button = Button(app,  width=50, pady=10, text='Archive Password', bg='#57a1f8', fg='white', border=0, cursor='hand2')
    archive_button.pack(pady=10)

    # tombol logout
    logout_button = Button(app,  width=50, pady=10, text='Log Out', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=show_sign_in_page)
    logout_button.pack(pady=10)

# generate password page
def pw_generate():
    for widget in app.winfo_children():
        widget.destroy()

    # memuat gambar logo
    img = PhotoImage(file='logo.png')
    app.img = img
    Label(app, image=img, bg='white').place(x=3, y=1, anchor='nw')

    # label nama aplikasi
    app_name = Label(app, text="Password Manager", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 15, 'bold'))
    app_name.place(x=60, y=10)

show_sign_in_page()
app.mainloop()