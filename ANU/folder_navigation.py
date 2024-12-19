import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog


class FolderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Navigation")

        # Data utama
        # Pastikan data diinisialisasi hanya sekali
        if not hasattr(self, "data"):
            self.data = {}

        # Frame untuk Treeview
        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)

        # Treeview untuk daftar utama
        self.tree = ttk.Treeview(self.tree_frame, columns=("count"), show="tree")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Tombol untuk menambah kategori baru
        self.add_button = ttk.Button(
            self.tree_frame, text="Add New List", command=self.add_new_list
        )
        self.add_button.pack(pady=10)

        # Memasukkan item ke Treeview
        self.update_treeview()

        # Variabel untuk menyimpan item saat ini di hover
        self.current_hover = None

        # Event untuk hover
        self.tree.bind("<Motion>", self.on_hover)
        self.tree.bind("<Leave>", self.on_leave)

        # Event untuk memilih item
        self.tree.bind("<<TreeviewSelect>>", self.open_folder)

    def update_treeview(self):
        # Bersihkan Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Masukkan data ke Treeview
        for category, items in self.data.items():
            self.tree.insert("", tk.END, category, text=category)

    def add_new_list(self):
        # Dialog untuk input kategori baru
        category = simpledialog.askstring("New List", "Enter list name:")
        if category and category not in self.data:
            # Tambahkan kategori baru
            self.data[category] = []

            # Dialog untuk input item dalam kategori baru
            while True:
                item = simpledialog.askstring(
                    "Add Item", f"Enter item for '{category}' (or leave blank to finish):"
                )
                if not item:  # Jika input kosong, selesai
                    break
                self.data[category].append(item)

            # Update tampilan Treeview
            self.update_treeview()

    def on_hover(self, event):
        # Hitung item di bawah kursor
        row_id = self.tree.identify_row(event.y)

        if row_id != self.current_hover:
            # Jika item baru di-hover, ubah warna latar belakang
            if self.current_hover:
                self.tree.item(self.current_hover, tags="")

            self.current_hover = row_id
            if self.current_hover:
                self.tree.item(self.current_hover, tags=("hover",))
                self.tree.tag_configure("hover", background="#e6f7ff", foreground="#000000")

    def on_leave(self, event):
        # Reset efek hover saat kursor keluar dari widget
        if self.current_hover:
            self.tree.item(self.current_hover, tags="")
            self.current_hover = None

    def open_folder(self, event):
        selected_item = self.tree.selection()  # Ambil item yang dipilih
        if selected_item:
            category = self.tree.item(selected_item[0], "text")
            if category in self.data:  # Jika kategori ditemukan, buka halaman baru
                self.show_items(category)

    def show_items(self, category):
        # Hapus halaman utama
        for widget in self.root.winfo_children():
            widget.destroy()

        # Frame untuk halaman baru
        page_frame = ttk.Frame(self.root)
        page_frame.pack(fill=tk.BOTH, expand=True)

        # Label judul
        title_label = ttk.Label(page_frame, text=f"{category} Items", font=("Arial", 16))
        title_label.pack(pady=10)

        # List item di halaman baru
        for item in self.data[category]:
            item_label = ttk.Label(page_frame, text=f"- {item}", font=("Arial", 12))
            item_label.pack(anchor="w", padx=20)

        # Tombol untuk kembali
        back_button = ttk.Button(page_frame, text="Back", command=self.go_back)
        back_button.pack(pady=10)

    def go_back(self):
        # Kembali ke halaman utama
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)  # Panggil ulang dengan data yang tetap


root = tk.Tk()
app = FolderApp(root)
root.mainloop()
