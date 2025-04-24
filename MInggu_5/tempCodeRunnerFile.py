def create_menu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Keluar", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Bantuan", command=self.show_help)
        menubar.add_cascade(label="Menu", menu=help_menu)
        
        self.root.config(menu=menubar)