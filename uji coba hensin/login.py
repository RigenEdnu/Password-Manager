import tkinter as tk
from tkinter import messagebox
import signup  # Tetap impor file signup.py untuk digunakan

def login_window():
    def login_action():
        username = username_entry.get()
        password = password_entry.get()
        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    stored_username, stored_password = user.strip().split(",")
                    if username == stored_username and password == stored_password:
                        messagebox.showinfo("Success", "Login Berhasil!")
                        root.destroy()  # Menutup jendela login setelah berhasil
                        return
                messagebox.showerror("Error", "Username atau password salah!")
        except FileNotFoundError:
            messagebox.showerror("Error", "Database pengguna tidak ditemukan!")

    def open_signup():
        root.destroy()  # Menutup jendela login
        signup.signup_window()  # Buka jendela sign-up

    root = tk.Tk()
    root.title("Login")

    tk.Label(root, text="Username:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    tk.Button(root, text="Login", command=login_action).pack(pady=10)
    tk.Button(root, text="Sign Up", command=open_signup).pack(pady=5)

    root.mainloop()

# Menjalankan program langsung dari file ini
if __name__ == "__main__":
    login_window()
