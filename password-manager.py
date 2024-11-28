import random
import string
import tkinter as tk
import customtkinter

# system gui
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def passgen(long):
    long = int(long)
    huruf = string.ascii_letters
    numbers = string.digits
    symbol = string.punctuation
    mix = huruf + numbers + symbol
    mixed_result = [random.choice(mix) for _ in range(long)]
    password = ''.join(mixed_result)

    showpw(password)

def showpw(password):
    for widget in app.winfo_children():
        widget.pack_forget()  # Memastikan widget dihapus dengan benar
    
    # Menampilkan password menggunakan CTkLabel atau CTkEntry dengan placeholder_text
    # Menggunakan CTkLabel untuk menampilkan password
    title = customtkinter.CTkLabel(app, text="Generated Password: " + password)
    title.pack(padx=10, pady=10)

    # Jika Anda ingin menampilkan password menggunakan CTkEntry, Anda bisa menggunakan placeholder_text
    # password_entry = customtkinter.CTkEntry(app, placeholder_text=password, state="disabled", width=350, height=40)
    # password_entry.pack(padx=10, pady=10)

def buatpassword():
    for widget in app.winfo_children():
        widget.pack_forget()  # Memastikan widget dihapus dengan benar
    
    # Elemen UI untuk input panjang password
    title = customtkinter.CTkLabel(app, text="Masukkan Panjang Password")
    title.pack(padx=10, pady=10)

    # Input panjang password
    long = customtkinter.CTkEntry(app, width=350, height=40)
    long.pack(padx=10, pady=10)

    # Tombol submit untuk menghasilkan password
    submit = customtkinter.CTkButton(app, text='Submit', command=lambda: passgen(long.get()))
    submit.pack(padx=10, pady=10)

# Membuat window aplikasi
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Password Manager")

buatpassword()  # Menjalankan fungsi buatpassword untuk memulai UI

# Menjalankan aplikasi GUI
app.mainloop()  # Pemanggilan mainloop hanya sekali di akhir
