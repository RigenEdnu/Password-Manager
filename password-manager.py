import random
import string
import tkinter as tk
import customtkinter

#system gui
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def passgen(long):
    long = int(long)
    huruf = (string.ascii_letters)
    numbers = (string.digits)
    symbol = (string.punctuation)
    mix = huruf + numbers + symbol
    mixed_result = [random.choice(mix) for _ in range(long)]
    password = ''.join(mixed_result)

    showpw(password)

    #frame app
    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("Password Manager")

    def buatpassword():
        for widget in app.winfo_children():
            widget.pack_forget
        # ui element 
        title = customtkinter.CTkLabel(app, text="Masukan Panjang Password")
        title.pack(padx=10, pady=10)

        #long password
        long = customtkinter.CTkEntry(app, width=350, height=40)
        long.pack(padx=10, pady=10)

        # sumbit button 
        sumbit = customtkinter.CTkButton(app, text='sumbit', command=lambda: passgen(long.get()))
        sumbit.pack()

        def showpw(password):
            for widget in app.winfo_children():
                widget.pack_forget
            # ui element
            title = customtkinter.CTkEntry(app, text=password, state="disable")
            title.pack(padx=10, pady=10)

        buatpassword()

        #run app 
        app.mainloop()