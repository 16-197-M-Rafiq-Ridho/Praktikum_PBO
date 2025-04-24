import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class DailyCatalogApp:
    def __init__(self, root):
        self.root = root # menyimpan referensi ke jendela utama
        self.root.title("Diary Harian") # membuat judul pada pojok kiri atas
        self.root.geometry("900x500") # ukuran dari jendela aplikasi
        
        # Data structure for notes
        self.notes = [] # list kosong untuk menyimpan catatan
        
        # Create UI components
        self.create_widgets() # memanggil fungsi untuk membuat elemen ui
    
    def create_widgets(self):
        # Frame for input area
        input_frame = tk.Frame(self.root, pady=10) # Membuat frame area input
        input_frame.pack(fill=tk.X)
        
        # membuat frame input judul
        tk.Label(input_frame, text="Judul Diary:").grid(row=0, column=0, padx=5, sticky=tk.W)
        self.title_entry = tk.Entry(input_frame, width=53)
        self.title_entry.grid(row=0, column=1, padx=5, sticky=tk.W)
        
        # Membuat frame input isi
        tk.Label(input_frame, text="Isi Diary:").grid(row=1, column=0, padx=5, sticky=tk.W+tk.N)
        self.content_text = tk.Text(input_frame, width=40, height=5)
        self.content_text.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons
        button_frame = tk.Frame(self.root, pady=5)
        button_frame.pack(fill=tk.X)
        # Button tambah diary
        self.save_button = tk.Button(button_frame, text="Tambah ke diary", command=self.add_note)
        self.save_button.pack(side=tk.LEFT, padx=20)
        # Button hapus diary
        self.delete_button = tk.Button(button_frame, text="Hapus diary", command=self.delete_note)
        self.delete_button.pack(side=tk.LEFT, padx=20)
        # Button edit diary
        self.edit_button = tk.Button(button_frame, text="Edit diary", command=self.edit_note)
        self.edit_button.pack(side=tk.LEFT, padx=20)
        
        # frame untuk daftar catatan
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        # Label untuk daftar diary
        tk.Label(list_frame, text="Daftar Diary:").pack(anchor=tk.W)
        
        # Membuat scrollbar
        self.notes_listbox = tk.Listbox(list_frame, width=40, height=10)
        self.notes_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.notes_listbox.bind('<<ListboxSelect>>', self.on_select_note)
        
        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure scrollbar for listbox
        self.notes_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.notes_listbox.yview)
        
        # Note detail view (read-only)
        tk.Label(self.root, text="Isi Catatan:").pack(anchor=tk.W, padx=20)
        self.detail_text = tk.Text(self.root, width=80, height=10, state=tk.DISABLED)
        self.detail_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        # Create menu
        self.create_menu()
        
        # Update notes listbox
        self.update_notes_list()
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Keluar", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Bantuan", command=self.show_help)
        menubar.add_cascade(label="Menu", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def add_note(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()
        
        # Validate input
        if not title:
            messagebox.showerror("Error", "Judul Diary tidak boleh kosong!")
            return
        
        if not content:
            messagebox.showerror("Error", "Isi Diary tidak boleh kosong!")
            return
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create note object
        note = {
            "title": title,
            "content": content,
            "timestamp": timestamp
        }
        
        self.notes.append(note)
        self.update_notes_list()
        
        # Clear input fields
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        
        messagebox.showinfo("Horee", "Diary berhasil ditambahkan!")
    
    def on_select_note(self, event):
        if not self.notes_listbox.curselection():
            return
        
        index = self.notes_listbox.curselection()[0]
        note = self.notes[index]
        
        # Update detail view
        self.detail_text.config(state=tk.NORMAL)
        self.detail_text.delete("1.0", tk.END)
        self.detail_text.insert(tk.END, f"Tanggal: {note['timestamp']}\n\n{note['content']}")
        self.detail_text.config(state=tk.DISABLED)
    
    def delete_note(self):
        if not self.notes_listbox.curselection():
            messagebox.showwarning("Hayoo", "Catatan belum dipilih nihh!!")
            return
            
        index = self.notes_listbox.curselection()[0]
        title = self.notes[index]['title']
        
        confirm = messagebox.askyesno("Konfirmasi", f"Yakin Dihapus??? 'Judul: {title}'?")
        if confirm:
            del self.notes[index]
            self.update_notes_list()
            
            # Clear detail view
            self.detail_text.config(state=tk.NORMAL)
            self.detail_text.delete("1.0", tk.END)
            self.detail_text.config(state=tk.DISABLED)
            
            messagebox.showinfo("Yeyy", "Berhasil dihapus!")
    
    def edit_note(self):
        if not self.notes_listbox.curselection():
            messagebox.showwarning("cuyyy", "Belum dipilih diary nya!!")
            return
            
        index = self.notes_listbox.curselection()[0]
        note = self.notes[index]
        
        # Create a custom dialog for editing
        edit_dialog = tk.Toplevel(self.root)
        edit_dialog.title("Edit Diary")
        edit_dialog.geometry("500x400")
        edit_dialog.grab_set()  # Make it modal
        
        tk.Label(edit_dialog, text="Judul:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        edit_title = tk.Entry(edit_dialog, width=40)
        edit_title.grid(row=0, column=1, padx=5, pady=5)
        edit_title.insert(0, note['title'])
        
        tk.Label(edit_dialog, text="Isi:").grid(row=1, column=0, sticky=tk.W + tk.N, padx=5, pady=5)
        edit_content = tk.Text(edit_dialog, width=40, height=10)
        edit_content.grid(row=1, column=1, padx=5, pady=5)
        edit_content.insert(tk.END, note['content'])
        
        # Save button for the edit dialog
        def save_edit():
            new_title = edit_title.get().strip()
            new_content = edit_content.get("1.0", tk.END).strip()
            
            if not new_title:
                messagebox.showerror("Error", "Judul tidak boleh kosong!", parent=edit_dialog)
                return
            
            if not new_content:
                messagebox.showerror("Error", "Isi Diary tidak boleh kosong!", parent=edit_dialog)
                return
            
            # Update diary
            self.notes[index]['title'] = new_title
            self.notes[index]['content'] = new_content
            self.notes[index]['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " (Diedit)"
            
            self.update_notes_list()
            edit_dialog.destroy()
            
            # Update the selection
            self.notes_listbox.selection_set(index)
            self.on_select_note(None)
            
            messagebox.showinfo("Sukses", "Catatan berhasil diperbarui!")
        
        tk.Button(edit_dialog, text="Simpan Perubahan", command=save_edit).grid(row=2, column=1, pady=10)
    
    def update_notes_list(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            self.notes_listbox.insert(tk.END, note['title'])

    def show_help(self):
        help_text = """
Catatan Harian - Panduan Penggunaan

1. Menambah Catatan:
   - Isi judul dan konten catatan
   - Klik tombol "Tambah Catatan"

2. Melihat Catatan:
   - Pilih catatan dari daftar
   - Detail catatan akan ditampilkan di bagian bawah

3. Menghapus Catatan:
   - Pilih catatan dari daftar
   - Klik tombol "Hapus Catatan"
   - Konfirmasi penghapusan

4. Mengedit Catatan:
   - Pilih catatan dari daftar
   - Klik tombol "Edit Catatan"
   - Ubah judul atau isi catatan
   - Klik "Simpan Perubahan"

Catatan: Data tidak disimpan setelah aplikasi ditutup.
        """
        
        help_dialog = tk.Toplevel(self.root)
        help_dialog.title("Bantuan")
        help_dialog.geometry("500x400")
        
        # Create a Text widget with scrollbar
        help_text_widget = tk.Text(help_dialog, wrap=tk.WORD, height=20)
        help_text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        help_text_widget.insert(tk.END, help_text)
        help_text_widget.config(state=tk.DISABLED)
        
        scrollbar = tk.Scrollbar(help_dialog, orient=tk.VERTICAL, command=help_text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        help_text_widget.config(yscrollcommand=scrollbar.set)

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyCatalogApp(root)
    root.mainloop()