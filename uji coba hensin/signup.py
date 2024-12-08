import tkinter as tk
from tkinter import messagebox
import login

def signup_window():
    def signup_action():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Semua kolom harus diisi!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Password tidak cocok!")
            return

        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")
        messagebox.showinfo("Success", "Akun berhasil dibuat!")
        root.destroy()  # Menutup jendela sign-up
        login.login_window()  # Kembali ke jendela login

    root = tk.Tk()
    root.title("Sign Up")

    tk.Label(root, text="Username:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    tk.Label(root, text="Konfirmasi Password:").pack(pady=5)
    confirm_password_entry = tk.Entry(root, show="*")
    confirm_password_entry.pack(pady=5)

    tk.Button(root, text="Sign Up", command=signup_action).pack(pady=10)

    root.mainloop()
