import tkinter as tk
from tkinter import PhotoImage
import time
from datetime import datetime

class Taskbar:
    def __init__(self, root, app_launcher, window_manager):
        self.root = root
        self.app_launcher = app_launcher
        self.window_manager = window_manager
        
        # Get screen dimensions
        self.screen_width = root.winfo_screenwidth()
        
        # Create taskbar frame
        self.taskbar = tk.Frame(root, bg="#0A246A", height=30)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Create start button
        self.start_button = tk.Button(
            self.taskbar, 
            text="Start", 
            bg="#0A246A", 
            fg="white", 
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            bd=1,
            padx=10,
            command=self.toggle_start_menu
        )
        self.start_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Add hover effect to start button
        self.start_button.bind("<Enter>", lambda e: self.start_button.config(bg="#2A447A"))
        self.start_button.bind("<Leave>", lambda e: self.start_button.config(bg="#0A246A"))
        
        # Create quick launch area
        self.quick_launch = tk.Frame(self.taskbar, bg="#0A246A", height=26)
        self.quick_launch.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Add quick launch buttons
        self.ie_button = tk.Button(
            self.quick_launch,
            text="🌐",
            bg="#0A246A",
            fg="white",
            font=("Arial", 10),
            relief=tk.FLAT,
            width=2,
            command=lambda: self.app_launcher.open_app("browser")
        )
        self.ie_button.pack(side=tk.LEFT, padx=1)
        
        # Add hover effect to IE button
        self.ie_button.bind("<Enter>", lambda e: self.ie_button.config(bg="#2A447A"))
        self.ie_button.bind("<Leave>", lambda e: self.ie_button.config(bg="#0A246A"))
        
        # Create taskbar buttons area
        self.taskbar_buttons = tk.Frame(self.taskbar, bg="#0A246A")
        self.taskbar_buttons.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Create system tray
        self.system_tray = tk.Frame(self.taskbar, bg="#0A246A")
        self.system_tray.pack(side=tk.RIGHT, padx=5, pady=2)
        
        # Add volume icon
        self.volume_button = tk.Button(
            self.system_tray,
            text="🔊",
            bg="#0A246A",
            fg="white",
            font=("Arial", 10),
            relief=tk.FLAT,
            width=2,
            command=self.toggle_volume
        )
        self.volume_button.pack(side=tk.RIGHT, padx=1)
        
        # Add hover effect to volume button
        self.volume_button.bind("<Enter>", lambda e: self.volume_button.config(bg="#2A447A"))
        self.volume_button.bind("<Leave>", lambda e: self.volume_button.config(bg="#0A246A"))
        
        # Add clock
        self.clock_label = tk.Label(
            self.system_tray,
            text="",
            bg="#0A246A",
            fg="white",
            font=("Arial", 9)
        )
        self.clock_label.pack(side=tk.RIGHT, padx=5)
        self.update_clock()
        
        # Create start menu (initially hidden)
        self.start_menu = None
        self.start_menu_visible = False
        
        # Volume state
        self.volume_on = True
        
    def toggle_volume(self):
        self.volume_on = not self.volume_on
        if self.volume_on:
            self.volume_button.config(text="🔊")
        else:
            self.volume_button.config(text="🔇")
            
    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M")
        current_date = datetime.now().strftime("%d/%m/%Y")
        self.clock_label.config(text=f"{current_time}\n{current_date}")
        self.root.after(60000, self.update_clock)  # Update every minute
        
    def toggle_start_menu(self):
        if self.start_menu_visible:
            self.hide_start_menu()
        else:
            self.show_start_menu()
            
    def show_start_menu(self):
        if self.start_menu is None:
            self.create_start_menu()
            
        # Position the start menu
        self.start_menu.place(x=0, y=self.root.winfo_screenheight() - 30 - 300)
        self.start_menu_visible = True
        
        # Change start button appearance
        self.start_button.config(relief=tk.SUNKEN)
        
        # Animate start menu appearance
        self.animate_start_menu_appearance()
        
    def hide_start_menu(self):
        if self.start_menu is not None:
            self.animate_start_menu_disappearance()
            
    def animate_start_menu_appearance(self):
        # Initial state
        self.start_menu.place(x=-200, y=self.root.winfo_screenheight() - 30 - 300)
        
        # Animation steps
        steps = 10
        dx = 200 / steps
        
        def animate_step(step):
            if step < steps:
                new_x = -200 + dx * step
                self.start_menu.place(x=new_x, y=self.root.winfo_screenheight() - 30 - 300)
                self.root.after(20, lambda: animate_step(step + 1))
                
        animate_step(0)
        
    def animate_start_menu_disappearance(self):
        # Animation steps
        steps = 10
        dx = 200 / steps
        
        def animate_step(step):
            if step < steps:
                new_x = 0 - dx * step
                self.start_menu.place(x=new_x, y=self.root.winfo_screenheight() - 30 - 300)
                self.root.after(20, lambda: animate_step(step + 1))
            else:
                self.start_menu.place_forget()
                self.start_menu_visible = False
                # Reset start button appearance
                self.start_button.config(relief=tk.RAISED)
                
        animate_step(0)
            
    def create_start_menu(self):
        self.start_menu = tk.Frame(self.root, bg="#ECE9D8", width=200, height=300, relief=tk.RAISED, bd=2)
        
        # User section
        user_frame = tk.Frame(self.start_menu, bg="#0A246A", height=50)
        user_frame.pack(fill=tk.X)
        user_frame.pack_propagate(False)
        
        user_label = tk.Label(
            user_frame,
            text="NeoXP User",
            bg="#0A246A",
            fg="white",
            font=("Arial", 10, "bold")
        )
        user_label.pack(pady=15)
        
        # Programs section
        programs_frame = tk.Frame(self.start_menu, bg="#ECE9D8")
        programs_frame.pack(fill=tk.BOTH, expand=True)
        
        # Program items
        programs = [
            ("📁 Windows Explorer", "explorer"),
            ("📝 Notepad", "notepad"),
            ("🧮 Calculator", "calculator"),
            ("🎨 Paint", "paint"),
            ("🌐 Internet", "browser"),
            ("⚙️ Settings", "settings"),
            ("🖼️ Desktop Background", "background_settings"),
            ("📊 Desktop Properties", "desktop_properties")
        ]
        
        for text, app_id in programs:
            program_item = tk.Label(
                programs_frame,
                text=text,
                bg="#ECE9D8",
                font=("Arial", 9),
                anchor=tk.W,
                padx=10,
                pady=3
            )
            program_item.pack(fill=tk.X, anchor=tk.W)
            program_item.bind("<Button-1>", lambda e, a=app_id: self.on_program_click(a))
            program_item.bind("<Enter>", lambda e, w=program_item: w.config(bg="#316AC5", fg="white"))
            program_item.bind("<Leave>", lambda e, w=program_item: w.config(bg="#ECE9D8", fg="black"))
            
        # Bottom section
        bottom_frame = tk.Frame(self.start_menu, bg="#ECE9D8", height=30)
        bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # All Programs button
        all_programs = tk.Button(
            bottom_frame,
            text="All Programs ►",
            bg="#ECE9D8",
            fg="black",
            font=("Arial", 9),
            relief=tk.FLAT,
            anchor=tk.W,
            padx=10
        )
        all_programs.pack(fill=tk.X, side=tk.LEFT)
        
        # Log Off button
        log_off = tk.Button(
            bottom_frame,
            text="Log Off",
            bg="#ECE9D8",
            fg="black",
            font=("Arial", 9),
            relief=tk.FLAT,
            padx=10
        )
        log_off.pack(side=tk.RIGHT)
        
        # Turn Off button
        turn_off = tk.Button(
            bottom_frame,
            text="Turn Off Computer",
            bg="#ECE9D8",
            fg="black",
            font=("Arial", 9),
            relief=tk.FLAT,
            padx=10
        )
        turn_off.pack(side=tk.RIGHT)
        
    def on_program_click(self, app_id):
        self.hide_start_menu()
        self.app_launcher.open_app(app_id)
        
    def add_taskbar_button(self, window_id, title):
        button = tk.Button(
            self.taskbar_buttons,
            text=title,
            bg="#0A246A",
            fg="white",
            font=("Arial", 9),
            relief=tk.RAISED,
            bd=1,
            padx=5,
            command=lambda: self.window_manager.focus_window(window_id)
        )
        button.pack(side=tk.LEFT, padx=2)
        
        # Add hover effect
        button.bind("<Enter>", lambda e: button.config(bg="#2A447A"))
        button.bind("<Leave>", lambda e: button.config(bg="#0A246A"))
        
        return button
        
    def remove_taskbar_button(self, button):
        button.destroy()