import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class TreeviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Treeview Example")

        # Frame untuk Treeview
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)

        # Membuat Treeview
        self.tree = ttk.Treeview(self.frame, columns=("Value"), show="tree")
        self.tree.pack(side=tk.LEFT)

        # Scrollbar untuk Treeview
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Menambahkan item ke Treeview
        self.tree.bind("<Double-1>", self.on_item_double_click)

        # Entry untuk menambah item
        self.entry = ttk.Entry(self.root)
        self.entry.pack(pady=10)

        # Tombol untuk menambah item
        self.add_button = ttk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=5)

        # Tombol untuk menambah sub-item
        self.add_sub_button = ttk.Button(self.root, text="Add Sub-Item", command=self.add_sub_item)
        self.add_sub_button.pack(pady=5)

    def add_item(self):
        item_text = self.entry.get()
        if item_text:
            self.tree.insert("", "end", item_text, text=item_text)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a value.")

    def add_sub_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            sub_item_text = simpledialog.askstring("Add Sub-Item", "Enter sub-item name:")
            if sub_item_text:
                self.tree.insert(selected_item[0], "end", sub_item_text, text=sub_item_text)
            else:
                messagebox.showwarning("Warning", "Please enter a sub-item name.")
        else:
            messagebox.showwarning("Warning", "Please select an item to add a sub-item.")

    def on_item_double_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_text = self.tree.item(selected_item[0], "text")
            messagebox.showinfo("Item Selected", f"You selected: {item_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TreeviewApp(root)
    root.mainloop()