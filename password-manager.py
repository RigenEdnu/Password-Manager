import random
import string
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

# System GUI settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Function to generate password
def passgen(length):
    try:
        length = int(length)
        if length <= 0:
            show_error("Password length must be greater than 0.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        showpw(password)
    except ValueError:
        show_error("Please enter a valid number for password length.")

# Error message display
def show_error(message):
    clear_widgets()
    error_label = customtkinter.CTkLabel(app, text=message, text_color="red")
    error_label.pack(padx=10, pady=10)
    back_button = customtkinter.CTkButton(app, text="Back", command=buatpassword)
    back_button.pack(padx=10, pady=10)


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

# Function to build the initial password input form
def buatpassword():
    clear_widgets()
    # UI elements
    title = customtkinter.CTkLabel(app, text="Enter Password Length:")
    title.pack(padx=10, pady=10)

    long_entry = customtkinter.CTkEntry(app, width=350, height=40)
    long_entry.pack(padx=10, pady=10)

    submit_button = customtkinter.CTkButton(app, text="Generate", command=lambda: passgen(long_entry.get()))
    submit_button.pack(padx=10, pady=10)

# Display the generated password
def showpw(password):
    clear_widgets()
    # UI elements
    title = customtkinter.CTkLabel(app, text="Generated Password:")
    title.pack(padx=10, pady=10)

    password_entry = customtkinter.CTkEntry(app, width=350, height=40, state="readonly")
    password_entry.insert(0, password)
    password_entry.pack(padx=10, pady=10)

    copy_button = customtkinter.CTkButton(app, text="Copy to Clipboard", command=lambda: copy_to_clipboard(password))
    copy_button.pack(padx=10, pady=10)

    back_button = customtkinter.CTkButton(app, text="Generate Another", command=buatpassword)
    back_button.pack(padx=10, pady=10)

# Function to copy password to clipboard
def copy_to_clipboard(password):
    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()

# Clear widgets from the window
def clear_widgets():
    for widget in app.winfo_children():
        widget.pack_forget()

# Main application
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Password Manager")

buatpassword()

# Run the application
app.mainloop()

