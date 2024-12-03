import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Halaman Login
login=tk.Tk()
login.title('Login')
login.geometry('925x500+300+200')
login.configure(bg="#fff")

# Memuat Gambar
img = PhotoImage(file='login.png')
Label(login, image=img, bg='white').place(x=50,y=50)

# Frame sign in, sign up
frame = Frame(login, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Input Username
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Input Password
pw = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
pw.place(x=30, y=150)
pw.insert(0, 'Password')
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Sign in Button
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0).place(x=35, y=204)
label=Label(frame, text="Belum memiliki akun?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

# Sign up Button

login.mainloop()