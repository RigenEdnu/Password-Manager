import random
import string

import os
import json
with open ("password.json", "r") as file:
    data = json.load(file)
    pass_storage = data["pass_storage"]


# pada generate password
def generatepassword(length):
    huruf = string.ascii_letters
    numbers = string.digits
    symbol = string.punctuation
    mix = huruf + numbers + symbol
    mixed_result = [random.choice(mix) for _ in range(length)]
    password = ''.join(mixed_result)
    return password

# 3 SAVE PASSWORD
def savepassword(label, password):
    with open("password.json", "w") as file:
        pass_storage[label] = password
        json.dump(data, file)
        
def showpassword():
    with open("password.json", "r") as file:
        data = json.load(file)
        for label, password in data["pass_storage"].items():
            print(f"{label} : {password}")

def removepassword(label):
    with open("password.txt", "r") as file:
        lines = file.readlines()
    with open("password.txt", "w") as file:
        password_found = False
        for line in lines:
            if label in line:
                password_found = True
            else:
                file.write(line)
        if not password_found:
            print("Password tidak ditemukan")

def replacepassword(label, password):
    with open("password.txt", "r") as file:
        lines = file.readlines()
    with open("password.txt", "w") as file:
        for line in lines:
            if label in line:
                file.write(f"{label} : {password}\n")
            else:
                file.write(line)

def main():
    while True:
        print("\nSelamat Datang di Password Manager")
        print("1. Password Generate\n2. Save Password\n3. Show Password\n4. Remove Password\n5. Replace Password\n6. Exit")
        mainmenu = input("Pilih menu: ")
        if mainmenu == "1":
            length = int(input("Masukan panjang sandi Anda: "))
            password = generatepassword(length)
            print(f"Password selesai dibuat {password}")
        elif mainmenu == "2":
            label = input("Masukan label password: ")
            length = int(input("Masukan panjang sandi Anda: "))
            password = generatepassword(length)
            savepassword(label, password)
            print(f"Password untuk {label} telah disimpan di password.txt")
        elif mainmenu == "3":
            showpassword()
        elif mainmenu == "4":
            label = input("Masukan label password yang ingin dihapus: ")
            removepassword(label)
            print(f"Password untuk {label} telah dihapus")
        elif mainmenu == "5":
            label = input("Masukan label password yang ingin diganti: ")
            length = int(input("Masukan panjang sandi Anda: "))
            password = generatepassword(length)
            replacepassword(label, password)
            print(f"Password untuk {label} telah diganti")
        elif mainmenu == "6":
            print("Terima kasih telah menggunakan Password Manager")
            break
        else:
            print("Menu tidak tersedia")        

main()