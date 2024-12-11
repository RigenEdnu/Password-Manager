import random
import string
import tkinter as tk
import customtkinter
from tkinter import messagebox
import pyperclip

# System GUI Setup
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Fungsi untuk menangani aksi tombol pada menu
def menu1_action():
    show_generate_password_screen()

def menu2_action():
    messagebox.showinfo("Menu 2", "Menu 2 dipilih!")

def menu3_action():
    messagebox.showinfo("Menu 3", "Menu 3 dipilih!")

# Fungsi untuk menampilkan tampilan pembuatan password
def show_generate_password_screen():
    for widget in app.winfo_children():
        widget.pack_forget()  # Hapus widget sebelumnya
    
    # Elemen UI untuk input panjang password
    title = customtkinter.CTkLabel(app, text="Masukkan Panjang Password")
    title.pack(padx=10, pady=10)

    # Input panjang password
    long_entry = customtkinter.CTkEntry(app, width=350, height=40)
    long_entry.pack(padx=10, pady=10)

    # Tombol submit untuk menghasilkan password
    submit_button = customtkinter.CTkButton(app, text='Generate Password', command=lambda: menuGenerate(long_entry.get()))
    submit_button.pack(padx=10, pady=10)

    # Tombol kembali ke menu utama
    back_button = customtkinter.CTkButton(app, text="Kembali ke Menu Utama", command=show_main_menu)
    back_button.pack(padx=10, pady=10)

# Fungsi untuk menghasilkan password
def menuGenerate(long):
    try:
        long = int(long)  # Konversi panjang password menjadi integer
        huruf = string.ascii_letters
        numbers = string.digits
        symbol = string.punctuation
        mix = huruf + numbers + symbol
        mixed_result = [random.choice(mix) for _ in range(long)]
        password = ''.join(mixed_result)
        showpw(password)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan panjang password yang valid!")

# Fungsi untuk menampilkan password
def showpw(password):
    for widget in app.winfo_children():
        widget.pack_forget()  # Hapus widget sebelumnya
    
    # Tampilkan password
    title = customtkinter.CTkLabel(app, text="Password telah dibuat: " + password)
    title.pack(padx=10, pady=10)

    # Tombol untuk menyalin password ke clipboard
    copy_button = customtkinter.CTkButton(app, text="Copy Password", command=lambda: copy_to_clipboard(password))
    copy_button.pack(padx=10, pady=10)

    # Tombol kembali ke menu utama
    back_button = customtkinter.CTkButton(app, text="Kembali ke Menu Utama", command=show_main_menu)
    back_button.pack(padx=10, pady=10)

# fungsi menyalin password
def copy_to_clipboard(password):
    pyperclip.copy(password)
    messagebox.showinfo("Copy", "Password berhasil di copy ke clipboard")

# Fungsi untuk menampilkan menu utama
def show_main_menu():
    for widget in app.winfo_children():
        widget.pack_forget()  # Hapus widget sebelumnya
    
    # Frame untuk tombol menu
    frame = customtkinter.CTkFrame(app)
    frame.pack(expand=True)

    # Membuat 3 tombol menu
    menu_button_1 = customtkinter.CTkButton(frame, text="Menu 1: Generate Password", width=20, height=3, command=menu1_action)
    menu_button_1.grid(row=0, column=0, padx=10, pady=10)

    menu_button_2 = customtkinter.CTkButton(frame, text="Menu 2", width=20, height=2, command=menu2_action)
    menu_button_2.grid(row=1, column=0, padx=10, pady=10)

    menu_button_3 = customtkinter.CTkButton(frame, text="Menu 3", width=20, height=2, command=menu3_action)
    menu_button_3.grid(row=2, column=0, padx=10, pady=10)

# Membuat window aplikasi
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Password Manager")

# Menampilkan menu utama pertama kali
show_main_menu()

# Menjalankan aplikasi GUI
app.mainloop()
