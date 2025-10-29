import tkinter as tk
from tkinter import PhotoImage
import os
from taskbar import Taskbar
from window_manager import WindowManager
from apps import AppLauncher

class NeoXP:
    def __init__(self, root):
        self.root = root
        self.root.title("NeoXP")
        
        # Make full screen
        self.root.attributes('-fullscreen', True)
        
        # Get screen dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.root.configure(bg="#3A6EA5")  # XP blue background
        
        # Create desktop
        self.desktop = tk.Frame(root, bg="#3A6EA5")
        self.desktop.pack(fill=tk.BOTH, expand=True)
        
        # Create desktop icons
        self.create_desktop_icons()
        
        # Initialize window manager
        self.window_manager = WindowManager(self.desktop)
        
        # Initialize app launcher
        self.app_launcher = AppLauncher(self.window_manager)
        
        # Create taskbar
        self.taskbar = Taskbar(root, self.app_launcher, self.window_manager)
        
        # Pass taskbar reference to window manager
        self.window_manager.set_taskbar(self.taskbar)
        
        # Set up desktop background
        self.set_desktop_background()
        
        # Bind escape key to exit full screen
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        
        # Add right-click context menu to desktop
        self.create_desktop_context_menu()
        
    def create_desktop_context_menu(self):
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Refresh", command=self.refresh_desktop)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="New Folder", command=self.create_new_folder)
        self.context_menu.add_command(label="New Text Document", command=self.create_new_text_document)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Properties", command=self.show_desktop_properties)
        self.context_menu.add_command(label="Change Background", command=self.change_background)
        
        self.desktop.bind("<Button-3>", self.show_context_menu)
        
    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)
        
    def refresh_desktop(self):
        # Simple refresh animation
        self.desktop.config(bg="#5A7EB5")
        self.root.after(100, lambda: self.desktop.config(bg="#3A6EA5"))
        
    def create_new_folder(self):
        # Create a new folder on desktop
        folder_frame = tk.Frame(self.desktop, bg="#3A6EA5", relief=tk.RAISED, bd=1)
        folder_frame.place(x=100, y=100)
        
        folder_icon = tk.Label(folder_frame, text="📁", font=("Arial", 20), bg="#3A6EA5")
        folder_icon.pack()
        
        folder_label = tk.Label(folder_frame, text="New Folder", font=("Arial", 9), bg="#3A6EA5", fg="white")
        folder_label.pack()
        
        # Make folder draggable
        self.make_draggable(folder_frame)
        
    def create_new_text_document(self):
        # Create a new text document on desktop
        doc_frame = tk.Frame(self.desktop, bg="#3A6EA5", relief=tk.RAISED, bd=1)
        doc_frame.place(x=100, y=100)
        
        doc_icon = tk.Label(doc_frame, text="📄", font=("Arial", 20), bg="#3A6EA5")
        doc_icon.pack()
        
        doc_label = tk.Label(doc_frame, text="New Text Document.txt", font=("Arial", 9), bg="#3A6EA5", fg="white")
        doc_label.pack()
        
        # Make document draggable
        self.make_draggable(doc_frame)
        
    def make_draggable(self, widget):
        def start_drag(event):
            widget._drag_start_x = event.x
            widget._drag_start_y = event.y
            
        def drag(event):
            x = widget.winfo_x() + event.x - widget._drag_start_x
            y = widget.winfo_y() + event.y - widget._drag_start_y
            widget.place(x=x, y=y)
            
        widget.bind("<Button-1>", start_drag)
        widget.bind("<B1-Motion>", drag)
        
    def show_desktop_properties(self):
        self.app_launcher.open_app("desktop_properties")
        
    def change_background(self):
        self.app_launcher.open_app("background_settings")
        
    def create_desktop_icons(self):
        # Create desktop icons frame
        icons_frame = tk.Frame(self.desktop, bg="#3A6EA5")
        icons_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # My Computer
        my_computer = tk.Frame(icons_frame, bg="#3A6EA5", relief=tk.RAISED, bd=1)
        my_computer.grid(row=0, column=0, padx=5, pady=5)
        
        my_computer_icon = tk.Label(my_computer, text="💻", font=("Arial", 20), bg="#3A6EA5")
        my_computer_icon.pack()
        
        my_computer_label = tk.Label(my_computer, text="My Computer", font=("Arial", 9), bg="#3A6EA5", fg="white")
        my_computer_label.pack()
        
        my_computer.bind("<Button-1>", lambda e: self.app_launcher.open_app("my_computer"))
        my_computer_icon.bind("<Button-1>", lambda e: self.app_launcher.open_app("my_computer"))
        my_computer_label.bind("<Button-1>", lambda e: self.app_launcher.open_app("my_computer"))
        
        # My Documents
        my_documents = tk.Frame(icons_frame, bg="#3A6EA5", relief=tk.RAISED, bd=1)
        my_documents.grid(row=1, column=0, padx=5, pady=5)
        
        my_documents_icon = tk.Label(my_documents, text="📁", font=("Arial", 20), bg="#3A6EA5")
        my_documents_icon.pack()
        
        my_documents_label = tk.Label(my_documents, text="My Documents", font=("Arial", 9), bg="#3A6EA5", fg="white")
        my_documents_label.pack()
        
        my_documents.bind("<Button-1>", lambda e: self.app_launcher.open_app("my_documents"))
        my_documents_icon.bind("<Button-1>", lambda e: self.app_launcher.open_app("my_documents"))
        my_documents_label.bind("<Button-1>", lambda e: self.app_launcher.open_app("my_documents"))
        
        # Recycle Bin
        recycle_bin = tk.Frame(icons_frame, bg="#3A6EA5", relief=tk.RAISED, bd=1)
        recycle_bin.grid(row=2, column=0, padx=5, pady=5)
        
        recycle_bin_icon = tk.Label(recycle_bin, text="🗑️", font=("Arial", 20), bg="#3A6EA5")
        recycle_bin_icon.pack()
        
        recycle_bin_label = tk.Label(recycle_bin, text="Recycle Bin", font=("Arial", 9), bg="#3A6EA5", fg="white")
        recycle_bin_label.pack()
        
        recycle_bin.bind("<Button-1>", lambda e: self.app_launcher.open_app("recycle_bin"))
        recycle_bin_icon.bind("<Button-1>", lambda e: self.app_launcher.open_app("recycle_bin"))
        recycle_bin_label.bind("<Button-1>", lambda e: self.app_launcher.open_app("recycle_bin"))
        
    def set_desktop_background(self):
        # Create a simple gradient background
        canvas = tk.Canvas(self.desktop, width=self.screen_width, height=self.screen_height-30, bg="#3A6EA5", highlightthickness=0)
        canvas.place(x=0, y=0)
        
        # Create gradient effect
        gradient_height = self.screen_height - 30
        for i in range(100):
            # Calculate color values, ensuring they stay within valid range (0-255)
            r = min(58 + i * 2, 255)  # Red component
            g = min(110 + i, 255)     # Green component
            b = min(165 + i, 255)     # Blue component
            
            # Format as hex color
            color = f"#{r:02x}{g:02x}{b:02x}"
            
            # Draw gradient line
            y_pos = i * gradient_height / 100
            canvas.create_line(0, y_pos, self.screen_width, y_pos, fill=color, width=gradient_height/100 + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = NeoXP(root)
    root.mainloop()