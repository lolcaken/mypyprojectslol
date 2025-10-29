import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self, parent, title, width, height, window_id, window_manager):
        self.parent = parent
        self.title = title
        self.width = width
        self.height = height
        self.window_id = window_id
        self.window_manager = window_manager
        self.is_minimized = False
        self.is_maximized = False
        
        # Create window frame
        self.frame = tk.Frame(
            parent,
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=2,
            width=width,
            height=height
        )
        
        # Create title bar
        self.title_bar = tk.Frame(
            self.frame,
            bg="#0058E8",
            relief=tk.RAISED,
            bd=1,
            height=25
        )
        self.title_bar.pack(fill=tk.X)
        self.title_bar.pack_propagate(False)
        
        # Title bar title
        self.title_label = tk.Label(
            self.title_bar,
            text=title,
            bg="#0058E8",
            fg="white",
            font=("Arial", 9)
        )
        self.title_label.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Title bar buttons
        self.minimize_button = tk.Button(
            self.title_bar,
            text="—",
            bg="#0058E8",
            fg="white",
            font=("Arial", 9, "bold"),
            relief=tk.FLAT,
            bd=1,
            width=2,
            command=self.minimize
        )
        self.minimize_button.pack(side=tk.RIGHT, padx=1)
        
        self.maximize_button = tk.Button(
            self.title_bar,
            text="□",
            bg="#0058E8",
            fg="white",
            font=("Arial", 9, "bold"),
            relief=tk.FLAT,
            bd=1,
            width=2,
            command=self.maximize
        )
        self.maximize_button.pack(side=tk.RIGHT, padx=1)
        
        self.close_button = tk.Button(
            self.title_bar,
            text="✕",
            bg="#0058E8",
            fg="white",
            font=("Arial", 9, "bold"),
            relief=tk.FLAT,
            bd=1,
            width=2,
            command=self.close
        )
        self.close_button.pack(side=tk.RIGHT, padx=1)
        
        # Content area
        self.content = tk.Frame(
            self.frame,
            bg="white",
            width=width,
            height=height-25
        )
        self.content.pack(fill=tk.BOTH, expand=True)
        
        # Make window draggable
        self.title_bar.bind("<Button-1>", self.start_drag)
        self.title_bar.bind("<B1-Motion>", self.drag)
        self.title_label.bind("<Button-1>", self.start_drag)
        self.title_label.bind("<B1-Motion>", self.drag)
        
        # Store initial position
        self.x = 100
        self.y = 100
        self.place_window()
        
        # Store drag start position
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # Add hover effects to buttons
        self.add_button_effects()
        
    def add_button_effects(self):
        # Minimize button hover effect
        self.minimize_button.bind("<Enter>", lambda e: self.minimize_button.config(bg="#4080E8"))
        self.minimize_button.bind("<Leave>", lambda e: self.minimize_button.config(bg="#0058E8"))
        
        # Maximize button hover effect
        self.maximize_button.bind("<Enter>", lambda e: self.maximize_button.config(bg="#4080E8"))
        self.maximize_button.bind("<Leave>", lambda e: self.maximize_button.config(bg="#0058E8"))
        
        # Close button hover effect
        self.close_button.bind("<Enter>", lambda e: self.close_button.config(bg="#FF0000"))
        self.close_button.bind("<Leave>", lambda e: self.close_button.config(bg="#0058E8"))
        
    def place_window(self):
        self.frame.place(x=self.x, y=self.y)
        
    def start_drag(self, event):
        # Store the initial mouse position and window position
        self.drag_start_x = event.x_root
        self.drag_start_y = event.y_root
        self.window_start_x = self.x
        self.window_start_y = self.y
        
    def drag(self, event):
        # Calculate the new position based on mouse movement
        dx = event.x_root - self.drag_start_x
        dy = event.y_root - self.drag_start_y
        
        # Update window position
        self.x = self.window_start_x + dx
        self.y = self.window_start_y + dy
        
        # Keep window within screen bounds
        screen_width = self.parent.winfo_width()
        screen_height = self.parent.winfo_height()
        
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x + self.width > screen_width:
            self.x = screen_width - self.width
        if self.y + self.height > screen_height - 30:  # Account for taskbar
            self.y = screen_height - self.height - 30
            
        # Place window at new position
        self.frame.place(x=self.x, y=self.y)
        
    def minimize(self):
        self.is_minimized = True
        # Animate minimization
        self.animate_minimize()
        
    def animate_minimize(self):
        # Get current position and size
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        
        # Calculate target position (taskbar)
        target_x = x + width/2 - 50
        target_y = self.parent.winfo_height() - 30
        
        # Animation steps
        steps = 10
        dx = (target_x - x) / steps
        dy = (target_y - y) / steps
        dw = width / steps
        dh = height / steps
        
        def animate_step(step):
            if step < steps:
                new_x = x + dx * step
                new_y = y + dy * step
                new_width = width - dw * step
                new_height = height - dh * step
                
                self.frame.place(x=new_x, y=new_y, width=new_width, height=new_height)
                self.parent.after(20, lambda: animate_step(step + 1))
            else:
                self.frame.place_forget()
                self.window_manager.minimize_window(self.window_id)
                
        animate_step(0)
        
    def maximize(self):
        if self.is_maximized:
            # Restore to original size and position
            self.is_maximized = False
            self.frame.place(x=self.x, y=self.y)
            self.maximize_button.config(text="□")
        else:
            # Maximize to fill desktop
            self.is_maximized = True
            self.frame.place(x=0, y=0)
            self.maximize_button.config(text="❐")
            
    def close(self):
        # Animate closing
        self.animate_close()
        
    def animate_close(self):
        # Get current position and size
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        
        # Animation steps
        steps = 10
        dw = width / steps
        dh = height / steps
        
        def animate_step(step):
            if step < steps:
                new_x = x + dw * step / 2
                new_y = y + dh * step / 2
                new_width = width - dw * step
                new_height = height - dh * step
                
                self.frame.place(x=new_x, y=new_y, width=new_width, height=new_height)
                self.parent.after(20, lambda: animate_step(step + 1))
            else:
                self.window_manager.close_window(self.window_id)
                
        animate_step(0)
        
    def focus(self):
        # Bring window to front
        self.frame.lift()
        # Update title bar color to indicate focus
        self.title_bar.config(bg="#0058E8")
        self.title_label.config(bg="#0058E8")
        self.minimize_button.config(bg="#0058E8")
        self.maximize_button.config(bg="#0058E8")
        self.close_button.config(bg="#0058E8")
        
    def unfocus(self):
        # Update title bar color to indicate unfocus
        self.title_bar.config(bg="#8492B5")
        self.title_label.config(bg="#8492B5")
        self.minimize_button.config(bg="#8492B5")
        self.maximize_button.config(bg="#8492B5")
        self.close_button.config(bg="#8492B5")

class WindowManager:
    def __init__(self, desktop):
        self.desktop = desktop
        self.windows = {}
        self.window_count = 0
        self.active_window = None
        self.taskbar_buttons = {}
        self.taskbar = None
        
    def set_taskbar(self, taskbar):
        self.taskbar = taskbar
        
    def create_window(self, title, width=400, height=300):
        window_id = f"window_{self.window_count}"
        self.window_count += 1
        
        window = Window(self.desktop, title, width, height, window_id, self)
        self.windows[window_id] = window
        
        # Add to taskbar
        if self.taskbar:
            button = self.taskbar.add_taskbar_button(window_id, title)
            self.taskbar_buttons[window_id] = button
        
        # Set as active window
        self.focus_window(window_id)
        
        return window
        
    def close_window(self, window_id):
        if window_id in self.windows:
            window = self.windows[window_id]
            window.frame.destroy()
            del self.windows[window_id]
            
            # Remove from taskbar
            if window_id in self.taskbar_buttons and self.taskbar:
                self.taskbar.remove_taskbar_button(self.taskbar_buttons[window_id])
                del self.taskbar_buttons[window_id]
                
            # Set new active window if needed
            if self.active_window == window_id and self.windows:
                next_window_id = list(self.windows.keys())[-1]
                self.focus_window(next_window_id)
            elif self.active_window == window_id:
                self.active_window = None
                
    def focus_window(self, window_id):
        if window_id in self.windows:
            # Unfocus previous window
            if self.active_window and self.active_window in self.windows:
                self.windows[self.active_window].unfocus()
                
            # Focus new window
            self.windows[window_id].focus()
            self.active_window = window_id
            
    def minimize_window(self, window_id):
        if window_id in self.windows:
            # Unfocus if it was the active window
            if self.active_window == window_id:
                self.active_window = None
                # Find another window to focus
                if self.windows:
                    for wid, w in self.windows.items():
                        if not w.is_minimized:
                            self.focus_window(wid)
                            break
                            
    def restore_window(self, window_id):
        if window_id in self.windows:
            window = self.windows[window_id]
            if window.is_minimized:
                window.is_minimized = False
                window.place_window()
                self.focus_window(window_id)