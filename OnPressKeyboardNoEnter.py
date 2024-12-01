import keyboard

def on_key_press(event):
    if event.name == 'a':
        print("Tombol 'A' ditekan!")
    elif event.name == 'b':
        print("Tombol 'B' ditekan!")
    elif event.name == '1':
        print("Program dihentikan.")
        # Menghentikan listener
        return False  

# Menambahkan listener untuk menangkap penekanan tombol
keyboard.on_press(on_key_press)

print("Tekan 'A' atau 'B' untuk melihat hasilnya. Tekan 'Esc' untuk keluar.")

# Menjaga program tetap berjalan
keyboard.wait('1')  # Menunggu sampai tombol 'esc' ditekan