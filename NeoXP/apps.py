import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import math

class AppLauncher:
    def __init__(self, window_manager):
        self.window_manager = window_manager
        self.open_apps = {}
        
    def open_app(self, app_id):
        if app_id in self.open_apps:
            # App is already open, focus it
            self.window_manager.focus_window(self.open_apps[app_id])
            return
            
        if app_id == "notepad":
            self.open_notepad()
        elif app_id == "calculator":
            self.open_calculator()
        elif app_id == "paint":
            self.open_paint()
        elif app_id == "browser":
            self.open_browser()
        elif app_id == "my_computer":
            self.open_my_computer()
        elif app_id == "my_documents":
            self.open_my_documents()
        elif app_id == "recycle_bin":
            self.open_recycle_bin()
        elif app_id == "explorer":
            self.open_explorer()
        elif app_id == "settings":
            self.open_settings()
        elif app_id == "desktop_properties":
            self.open_desktop_properties()
        elif app_id == "background_settings":
            self.open_background_settings()
            
    def open_notepad(self):
        window = self.window_manager.create_window("Untitled - Notepad", 500, 400)
        window_id = window.window_id
        self.open_apps["notepad"] = window_id
        
        # Create menu bar
        menu_bar = tk.Frame(window.content, bg="#F0F0F0", height=20)
        menu_bar.pack(fill=tk.X)
        menu_bar.pack_propagate(False)
        
        file_menu = tk.Menubutton(menu_bar, text="File", bg="#F0F0F0", relief=tk.FLAT)
        file_menu.pack(side=tk.LEFT)
        
        file_menu.menu = tk.Menu(file_menu, tearoff=0)
        file_menu.menu.add_command(label="New")
        file_menu.menu.add_command(label="Open")
        file_menu.menu.add_command(label="Save")
        file_menu.menu.add_separator()
        file_menu.menu.add_command(label="Exit", command=lambda: self.window_manager.close_window(window_id))
        file_menu["menu"] = file_menu.menu
        
        edit_menu = tk.Menubutton(menu_bar, text="Edit", bg="#F0F0F0", relief=tk.FLAT)
        edit_menu.pack(side=tk.LEFT)
        
        edit_menu.menu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.menu.add_command(label="Cut")
        edit_menu.menu.add_command(label="Copy")
        edit_menu.menu.add_command(label="Paste")
        edit_menu["menu"] = edit_menu.menu
        
        # Create text area
        text_area = scrolledtext.ScrolledText(
            window.content,
            bg="white",
            fg="black",
            font=("Courier New", 10),
            wrap=tk.WORD
        )
        text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def open_calculator(self):
        window = self.window_manager.create_window("Calculator", 250, 300)
        window_id = window.window_id
        self.open_apps["calculator"] = window_id
        
        # Calculator display
        display = tk.Entry(
            window.content,
            bg="white",
            fg="black",
            font=("Arial", 14),
            justify=tk.RIGHT,
            bd=2
        )
        display.pack(fill=tk.X, padx=10, pady=10)
        
        # Calculator buttons
        buttons_frame = tk.Frame(window.content, bg="#ECE9D8")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Button layout
        buttons = [
            ("MC", "MR", "MS", "M+", "M-"),
            ("7", "8", "9", "/", "sqrt"),
            ("4", "5", "6", "*", "%"),
            ("1", "2", "3", "-", "1/x"),
            ("0", "+/-", ".", "+", "=")
        ]
        
        calc = CalculatorLogic(display)
        
        for row in buttons:
            row_frame = tk.Frame(buttons_frame, bg="#ECE9D8")
            row_frame.pack(fill=tk.X, pady=2)
            
            for text in row:
                if text == "=":
                    btn = tk.Button(
                        row_frame,
                        text=text,
                        bg="#ECE9D8",
                        width=5,
                        height=2,
                        command=calc.calculate
                    )
                else:
                    btn = tk.Button(
                        row_frame,
                        text=text,
                        bg="#ECE9D8",
                        width=5,
                        height=2,
                        command=lambda t=text: calc.append(t)
                    )
                btn.pack(side=tk.LEFT, padx=2)
                
                # Add hover effect
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#D0D0D0"))
                btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#ECE9D8"))
                
    def open_paint(self):
        window = self.window_manager.create_window("untitled - Paint", 600, 400)
        window_id = window.window_id
        self.open_apps["paint"] = window_id
        
        # Create menu bar
        menu_bar = tk.Frame(window.content, bg="#F0F0F0", height=20)
        menu_bar.pack(fill=tk.X)
        menu_bar.pack_propagate(False)
        
        file_menu = tk.Menubutton(menu_bar, text="File", bg="#F0F0F0", relief=tk.FLAT)
        file_menu.pack(side=tk.LEFT)
        
        file_menu.menu = tk.Menu(file_menu, tearoff=0)
        file_menu.menu.add_command(label="New")
        file_menu.menu.add_command(label="Open")
        file_menu.menu.add_command(label="Save")
        file_menu.menu.add_separator()
        file_menu.menu.add_command(label="Exit", command=lambda: self.window_manager.close_window(window_id))
        file_menu["menu"] = file_menu.menu
        
        # Create toolbar
        toolbar = tk.Frame(window.content, bg="#ECE9D8", height=30)
        toolbar.pack(fill=tk.X)
        toolbar.pack_propagate(False)
        
        # Add drawing tools
        tools = ["Pencil", "Line", "Rectangle", "Circle", "Eraser"]
        self.current_tool = "Pencil"
        
        for tool in tools:
            tool_btn = tk.Button(
                toolbar,
                text=tool,
                bg="#ECE9D8",
                relief=tk.RAISED,
                bd=1,
                command=lambda t=tool: self.select_tool(t)
            )
            tool_btn.pack(side=tk.LEFT, padx=2, pady=2)
            
            # Add hover effect
            tool_btn.bind("<Enter>", lambda e, b=tool_btn: b.config(bg="#D0D0D0"))
            tool_btn.bind("<Leave>", lambda e, b=tool_btn: b.config(bg="#ECE9D8"))
            
        # Color picker
        color_frame = tk.Frame(toolbar, bg="#ECE9D8")
        color_frame.pack(side=tk.LEFT, padx=10)
        
        self.current_color = "black"
        colors = ["black", "red", "green", "blue", "yellow", "purple"]
        
        for color in colors:
            color_btn = tk.Button(
                color_frame,
                bg=color,
                width=2,
                height=1,
                command=lambda c=color: self.select_color(c)
            )
            color_btn.pack(side=tk.LEFT, padx=1)
            
        # Create canvas
        self.canvas = tk.Canvas(
            window.content,
            bg="white",
            highlightthickness=1,
            highlightbackground="black"
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Drawing functionality
        self.setup_paint_drawing()
        
    def select_tool(self, tool):
        self.current_tool = tool
        
    def select_color(self, color):
        self.current_color = color
        
    def setup_paint_drawing(self):
        old_x = None
        old_y = None
        
        def start_paint(event):
            nonlocal old_x, old_y
            old_x = event.x
            old_y = event.y
            
        def paint(event):
            nonlocal old_x, old_y
            if old_x and old_y:
                if self.current_tool == "Pencil":
                    self.canvas.create_line(old_x, old_y, event.x, event.y, width=2, fill=self.current_color, capstyle=tk.ROUND, smooth=tk.TRUE)
                elif self.current_tool == "Line":
                    self.canvas.delete("temp_line")
                    self.canvas.create_line(old_x, old_y, event.x, event.y, width=2, fill=self.current_color, tags="temp_line")
                elif self.current_tool == "Rectangle":
                    self.canvas.delete("temp_rect")
                    self.canvas.create_rectangle(old_x, old_y, event.x, event.y, outline=self.current_color, tags="temp_rect")
                elif self.current_tool == "Circle":
                    self.canvas.delete("temp_circle")
                    radius = math.sqrt((event.x - old_x)**2 + (event.y - old_y)**2)
                    self.canvas.create_oval(old_x - radius, old_y - radius, old_x + radius, old_y + radius, outline=self.current_color, tags="temp_circle")
                elif self.current_tool == "Eraser":
                    self.canvas.create_line(old_x, old_y, event.x, event.y, width=10, fill="white", capstyle=tk.ROUND, smooth=tk.TRUE)
                    
                old_x = event.x
                old_y = event.y
                
        def end_paint(event):
            if self.current_tool in ["Line", "Rectangle", "Circle"]:
                self.canvas.delete("temp_line")
                self.canvas.delete("temp_rect")
                self.canvas.delete("temp_circle")
                
                if self.current_tool == "Line":
                    self.canvas.create_line(old_x, old_y, event.x, event.y, width=2, fill=self.current_color)
                elif self.current_tool == "Rectangle":
                    self.canvas.create_rectangle(old_x, old_y, event.x, event.y, outline=self.current_color)
                elif self.current_tool == "Circle":
                    radius = math.sqrt((event.x - old_x)**2 + (event.y - old_y)**2)
                    self.canvas.create_oval(old_x - radius, old_y - radius, old_x + radius, old_y + radius, outline=self.current_color)
                    
        self.canvas.bind("<Button-1>", start_paint)
        self.canvas.bind("<B1-Motion>", paint)
        self.canvas.bind("<ButtonRelease-1>", end_paint)
        
    def open_browser(self):
        window = self.window_manager.create_window("NeoXP Browser", 700, 500)
        window_id = window.window_id
        self.open_apps["browser"] = window_id
        
        # Create toolbar
        toolbar = tk.Frame(window.content, bg="#ECE9D8", height=30)
        toolbar.pack(fill=tk.X)
        toolbar.pack_propagate(False)
        
        # Back button
        back_btn = tk.Button(
            toolbar,
            text="←",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        back_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Forward button
        forward_btn = tk.Button(
            toolbar,
            text="→",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        forward_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Refresh button
        refresh_btn = tk.Button(
            toolbar,
            text="↻",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        refresh_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Address bar
        address_bar = tk.Entry(
            toolbar,
            bg="white",
            fg="black"
        )
        address_bar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=2)
        address_bar.insert(0, "http://www.neoxp.com")
        
        # Go button
        go_btn = tk.Button(
            toolbar,
            text="Go",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        go_btn.pack(side=tk.RIGHT, padx=2, pady=2)
        
        # Add hover effects
        back_btn.bind("<Enter>", lambda e: back_btn.config(bg="#D0D0D0"))
        back_btn.bind("<Leave>", lambda e: back_btn.config(bg="#ECE9D8"))
        
        forward_btn.bind("<Enter>", lambda e: forward_btn.config(bg="#D0D0D0"))
        forward_btn.bind("<Leave>", lambda e: forward_btn.config(bg="#ECE9D8"))
        
        refresh_btn.bind("<Enter>", lambda e: refresh_btn.config(bg="#D0D0D0"))
        refresh_btn.bind("<Leave>", lambda e: refresh_btn.config(bg="#ECE9D8"))
        
        go_btn.bind("<Enter>", lambda e: go_btn.config(bg="#D0D0D0"))
        go_btn.bind("<Leave>", lambda e: go_btn.config(bg="#ECE9D8"))
        
        # Create browser content
        browser_content = tk.Frame(window.content, bg="white")
        browser_content.pack(fill=tk.BOTH, expand=True)
        
        # Welcome page
        welcome_label = tk.Label(
            browser_content,
            text="Welcome to NeoXP Browser!\n\nThis is a simulated browser interface.\nIn a real implementation, this would display web content.",
            bg="white",
            fg="black",
            font=("Arial", 12),
            justify=tk.CENTER
        )
        welcome_label.pack(expand=True)
        
    def open_my_computer(self):
        window = self.window_manager.create_window("My Computer", 500, 400)
        window_id = window.window_id
        self.open_apps["my_computer"] = window_id
        
        # Create toolbar
        toolbar = tk.Frame(window.content, bg="#ECE9D8", height=30)
        toolbar.pack(fill=tk.X)
        toolbar.pack_propagate(False)
        
        # Back button
        back_btn = tk.Button(
            toolbar,
            text="←",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        back_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Forward button
        forward_btn = tk.Button(
            toolbar,
            text="→",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        forward_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Up button
        up_btn = tk.Button(
            toolbar,
            text="↑",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        up_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Address bar
        address_frame = tk.Frame(toolbar, bg="#ECE9D8")
        address_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=2)
        
        address_label = tk.Label(
            address_frame,
            text="Address",
            bg="#ECE9D8"
        )
        address_label.pack(side=tk.LEFT)
        
        address_bar = tk.Entry(
            address_frame,
            bg="white",
            fg="black"
        )
        address_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        address_bar.insert(0, "My Computer")
        
        # Create content area
        content = tk.Frame(window.content, bg="white")
        content.pack(fill=tk.BOTH, expand=True)
        
        # Create file list
        file_list_frame = tk.Frame(content, bg="white")
        file_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Hard disk drives
        drives_frame = tk.LabelFrame(
            file_list_frame,
            text="Hard Disk Drives",
            bg="white",
            fg="black",
            font=("Arial", 10, "bold")
        )
        drives_frame.pack(fill=tk.X, pady=5)
        
        # Local Disk (C:)
        c_drive = tk.Frame(drives_frame, bg="white")
        c_drive.pack(fill=tk.X, padx=10, pady=5)
        
        c_icon = tk.Label(c_drive, text="💾", font=("Arial", 16), bg="white")
        c_icon.pack(side=tk.LEFT, padx=5)
        
        c_info = tk.Frame(c_drive, bg="white")
        c_info.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        c_name = tk.Label(c_info, text="Local Disk (C:)", bg="white", fg="black", font=("Arial", 10), anchor=tk.W)
        c_name.pack(fill=tk.X)
        
        c_size = tk.Label(c_info, text="10.0 GB free of 20.0 GB", bg="white", fg="gray", font=("Arial", 8), anchor=tk.W)
        c_size.pack(fill=tk.X)
        
        # Devices with Removable Storage
        devices_frame = tk.LabelFrame(
            file_list_frame,
            text="Devices with Removable Storage",
            bg="white",
            fg="black",
            font=("Arial", 10, "bold")
        )
        devices_frame.pack(fill=tk.X, pady=5)
        
        # 3½ Floppy (A:)
        a_drive = tk.Frame(devices_frame, bg="white")
        a_drive.pack(fill=tk.X, padx=10, pady=5)
        
        a_icon = tk.Label(a_drive, text="💿", font=("Arial", 16), bg="white")
        a_icon.pack(side=tk.LEFT, padx=5)
        
        a_name = tk.Label(a_drive, text="3½ Floppy (A:)", bg="white", fg="black", font=("Arial", 10), anchor=tk.W)
        a_name.pack(side=tk.LEFT)
        
    def open_my_documents(self):
        window = self.window_manager.create_window("My Documents", 500, 400)
        window_id = window.window_id
        self.open_apps["my_documents"] = window_id
        
        # Create toolbar
        toolbar = tk.Frame(window.content, bg="#ECE9D8", height=30)
        toolbar.pack(fill=tk.X)
        toolbar.pack_propagate(False)
        
        # Back button
        back_btn = tk.Button(
            toolbar,
            text="←",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        back_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Forward button
        forward_btn = tk.Button(
            toolbar,
            text="→",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        forward_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Up button
        up_btn = tk.Button(
            toolbar,
            text="↑",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        up_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Address bar
        address_frame = tk.Frame(toolbar, bg="#ECE9D8")
        address_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=2)
        
        address_label = tk.Label(
            address_frame,
            text="Address",
            bg="#ECE9D8"
        )
        address_label.pack(side=tk.LEFT)
        
        address_bar = tk.Entry(
            address_frame,
            bg="white",
            fg="black"
        )
        address_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        address_bar.insert(0, "C:\\Documents and Settings\\User\\My Documents")
        
        # Create content area
        content = tk.Frame(window.content, bg="white")
        content.pack(fill=tk.BOTH, expand=True)
        
        # Create file list
        file_list_frame = tk.Frame(content, bg="white")
        file_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Sample files and folders
        items = [
            ("📁", "My Pictures", "Folder"),
            ("📁", "My Music", "Folder"),
            ("📁", "My Videos", "Folder"),
            ("📄", "document.txt", "Text Document"),
            ("📄", "presentation.ppt", "PowerPoint Presentation"),
            ("📄", "spreadsheet.xls", "Excel Spreadsheet")
        ]
        
        for icon, name, type in items:
            item_frame = tk.Frame(file_list_frame, bg="white")
            item_frame.pack(fill=tk.X, pady=2)
            
            item_icon = tk.Label(item_frame, text=icon, font=("Arial", 16), bg="white")
            item_icon.pack(side=tk.LEFT, padx=5)
            
            item_name = tk.Label(item_frame, text=name, bg="white", fg="black", font=("Arial", 10), anchor=tk.W)
            item_name.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            item_type = tk.Label(item_frame, text=type, bg="white", fg="gray", font=("Arial", 8))
            item_type.pack(side=tk.RIGHT, padx=10)
            
    def open_recycle_bin(self):
        window = self.window_manager.create_window("Recycle Bin", 500, 400)
        window_id = window.window_id
        self.open_apps["recycle_bin"] = window_id
        
        # Create toolbar
        toolbar = tk.Frame(window.content, bg="#ECE9D8", height=30)
        toolbar.pack(fill=tk.X)
        toolbar.pack_propagate(False)
        
        # Back button
        back_btn = tk.Button(
            toolbar,
            text="←",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        back_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Forward button
        forward_btn = tk.Button(
            toolbar,
            text="→",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        forward_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Up button
        up_btn = tk.Button(
            toolbar,
            text="↑",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        up_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Empty Recycle Bin button
        empty_btn = tk.Button(
            toolbar,
            text="Empty Recycle Bin",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        empty_btn.pack(side=tk.RIGHT, padx=5, pady=2)
        
        # Restore All button
        restore_btn = tk.Button(
            toolbar,
            text="Restore All",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        restore_btn.pack(side=tk.RIGHT, padx=5, pady=2)
        
        # Create content area
        content = tk.Frame(window.content, bg="white")
        content.pack(fill=tk.BOTH, expand=True)
        
        # Empty message
        empty_label = tk.Label(
            content,
            text="The Recycle Bin is empty.\n\nTo restore items from the Recycle Bin, right-click the item,\nand then click Restore.",
            bg="white",
            fg="black",
            font=("Arial", 10),
            justify=tk.CENTER
        )
        empty_label.pack(expand=True)
        
    def open_explorer(self):
        window = self.window_manager.create_window("Windows Explorer", 700, 500)
        window_id = window.window_id
        self.open_apps["explorer"] = window_id
        
        # Create toolbar
        toolbar = tk.Frame(window.content, bg="#ECE9D8", height=30)
        toolbar.pack(fill=tk.X)
        toolbar.pack_propagate(False)
        
        # Back button
        back_btn = tk.Button(
            toolbar,
            text="←",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        back_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Forward button
        forward_btn = tk.Button(
            toolbar,
            text="→",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        forward_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Up button
        up_btn = tk.Button(
            toolbar,
            text="↑",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        up_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Folders button
        folders_btn = tk.Button(
            toolbar,
            text="Folders",
            bg="#ECE9D8",
            relief=tk.SUNKEN,
            bd=1
        )
        folders_btn.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Views button
        views_btn = tk.Button(
            toolbar,
            text="Views",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        views_btn.pack(side=tk.RIGHT, padx=5, pady=2)
        
        # Create content area with splitter
        content = tk.Frame(window.content, bg="white")
        content.pack(fill=tk.BOTH, expand=True)
        
        # Left pane (folders)
        left_pane = tk.Frame(content, bg="#F0F0F0", width=200)
        left_pane.pack(side=tk.LEFT, fill=tk.Y)
        left_pane.pack_propagate(False)
        
        # Folder tree
        folder_tree = tk.Frame(left_pane, bg="#F0F0F0")
        folder_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Desktop
        desktop_frame = tk.Frame(folder_tree, bg="#F0F0F0")
        desktop_frame.pack(fill=tk.X, pady=2)
        
        desktop_icon = tk.Label(desktop_frame, text="🖥️", font=("Arial", 12), bg="#F0F0F0")
        desktop_icon.pack(side=tk.LEFT, padx=5)
        
        desktop_label = tk.Label(desktop_frame, text="Desktop", bg="#F0F0F0", fg="black", font=("Arial", 9), anchor=tk.W)
        desktop_label.pack(side=tk.LEFT)
        
        # My Documents
        my_docs_frame = tk.Frame(folder_tree, bg="#F0F0F0")
        my_docs_frame.pack(fill=tk.X, pady=2)
        
        my_docs_icon = tk.Label(my_docs_frame, text="📁", font=("Arial", 12), bg="#F0F0F0")
        my_docs_icon.pack(side=tk.LEFT, padx=5)
        
        my_docs_label = tk.Label(my_docs_frame, text="My Documents", bg="#F0F0F0", fg="black", font=("Arial", 9), anchor=tk.W)
        my_docs_label.pack(side=tk.LEFT)
        
        # My Computer
        my_comp_frame = tk.Frame(folder_tree, bg="#F0F0F0")
        my_comp_frame.pack(fill=tk.X, pady=2)
        
        my_comp_icon = tk.Label(my_comp_frame, text="💻", font=("Arial", 12), bg="#F0F0F0")
        my_comp_icon.pack(side=tk.LEFT, padx=5)
        
        my_comp_label = tk.Label(my_comp_frame, text="My Computer", bg="#F0F0F0", fg="black", font=("Arial", 9), anchor=tk.W)
        my_comp_label.pack(side=tk.LEFT)
        
        # Right pane (files)
        right_pane = tk.Frame(content, bg="white")
        right_pane.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # File list
        file_list_frame = tk.Frame(right_pane, bg="white")
        file_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Sample files and folders
        items = [
            ("📁", "My Pictures", "Folder"),
            ("📁", "My Music", "Folder"),
            ("📁", "My Videos", "Folder"),
            ("📄", "document.txt", "Text Document"),
            ("📄", "presentation.ppt", "PowerPoint Presentation"),
            ("📄", "spreadsheet.xls", "Excel Spreadsheet")
        ]
        
        for icon, name, type in items:
            item_frame = tk.Frame(file_list_frame, bg="white")
            item_frame.pack(fill=tk.X, pady=2)
            
            item_icon = tk.Label(item_frame, text=icon, font=("Arial", 16), bg="white")
            item_icon.pack(side=tk.LEFT, padx=5)
            
            item_name = tk.Label(item_frame, text=name, bg="white", fg="black", font=("Arial", 10), anchor=tk.W)
            item_name.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            item_type = tk.Label(item_frame, text=type, bg="white", fg="gray", font=("Arial", 8))
            item_type.pack(side=tk.RIGHT, padx=10)
            
    def open_settings(self):
        window = self.window_manager.create_window("Settings", 500, 400)
        window_id = window.window_id
        self.open_apps["settings"] = window_id
        
        # Create tabbed interface
        notebook = ttk.Notebook(window.content)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # General tab
        general_tab = tk.Frame(notebook, bg="white")
        notebook.add(general_tab, text="General")
        
        # Background color setting
        bg_frame = tk.Frame(general_tab, bg="white")
        bg_frame.pack(fill=tk.X, padx=10, pady=10)
        
        bg_label = tk.Label(bg_frame, text="Desktop Background:", bg="white", fg="black", font=("Arial", 10))
        bg_label.pack(side=tk.LEFT, padx=5)
        
        bg_var = tk.StringVar(value="Blue")
        bg_options = ["Blue", "Green", "Classic"]
        bg_menu = tk.OptionMenu(bg_frame, bg_var, *bg_options)
        bg_menu.pack(side=tk.LEFT)
        
        # Theme setting
        theme_frame = tk.Frame(general_tab, bg="white")
        theme_frame.pack(fill=tk.X, padx=10, pady=10)
        
        theme_label = tk.Label(theme_frame, text="Theme:", bg="white", fg="black", font=("Arial", 10))
        theme_label.pack(side=tk.LEFT, padx=5)
        
        theme_var = tk.StringVar(value="Windows XP")
        theme_options = ["Windows XP", "Classic", "NeoXP"]
        theme_menu = tk.OptionMenu(theme_frame, theme_var, *theme_options)
        theme_menu.pack(side=tk.LEFT)
        
        # Apply button
        apply_btn = tk.Button(
            general_tab,
            text="Apply",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        apply_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Display tab
        display_tab = tk.Frame(notebook, bg="white")
        notebook.add(display_tab, text="Display")
        
        # Resolution setting
        res_frame = tk.Frame(display_tab, bg="white")
        res_frame.pack(fill=tk.X, padx=10, pady=10)
        
        res_label = tk.Label(res_frame, text="Screen Resolution:", bg="white", fg="black", font=("Arial", 10))
        res_label.pack(side=tk.LEFT, padx=5)
        
        res_var = tk.StringVar(value="1024x768")
        res_options = ["800x600", "1024x768", "1280x1024"]
        res_menu = tk.OptionMenu(res_frame, res_var, *res_options)
        res_menu.pack(side=tk.LEFT)
        
        # Color quality setting
        color_frame = tk.Frame(display_tab, bg="white")
        color_frame.pack(fill=tk.X, padx=10, pady=10)
        
        color_label = tk.Label(color_frame, text="Color Quality:", bg="white", fg="black", font=("Arial", 10))
        color_label.pack(side=tk.LEFT, padx=5)
        
        color_var = tk.StringVar(value="Medium (16 bit)")
        color_options = ["Low (8 bit)", "Medium (16 bit)", "High (32 bit)"]
        color_menu = tk.OptionMenu(color_frame, color_var, *color_options)
        color_menu.pack(side=tk.LEFT)
        
        # Apply button
        apply_btn = tk.Button(
            display_tab,
            text="Apply",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        apply_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
    def open_desktop_properties(self):
        window = self.window_manager.create_window("Display Properties", 400, 400)
        window_id = window.window_id
        self.open_apps["desktop_properties"] = window_id
        
        # Create tabbed interface
        notebook = ttk.Notebook(window.content)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Themes tab
        themes_tab = tk.Frame(notebook, bg="white")
        notebook.add(themes_tab, text="Themes")
        
        theme_label = tk.Label(themes_tab, text="Theme:", bg="white", fg="black", font=("Arial", 10))
        theme_label.pack(anchor=tk.W, padx=10, pady=5)
        
        theme_var = tk.StringVar(value="Windows XP")
        theme_options = ["Windows XP", "Classic", "NeoXP"]
        theme_menu = tk.OptionMenu(themes_tab, theme_var, *theme_options)
        theme_menu.pack(fill=tk.X, padx=10, pady=5)
        
        # Desktop tab
        desktop_tab = tk.Frame(notebook, bg="white")
        notebook.add(desktop_tab, text="Desktop")
        
        desktop_label = tk.Label(desktop_tab, text="Background:", bg="white", fg="black", font=("Arial", 10))
        desktop_label.pack(anchor=tk.W, padx=10, pady=5)
        
        desktop_var = tk.StringVar(value="Bliss")
        desktop_options = ["Bliss", "Autumn", "Azul", "Classic"]
        desktop_menu = tk.OptionMenu(desktop_tab, desktop_var, *desktop_options)
        desktop_menu.pack(fill=tk.X, padx=10, pady=5)
        
        # Screen Saver tab
        screensaver_tab = tk.Frame(notebook, bg="white")
        notebook.add(screensaver_tab, text="Screen Saver")
        
        screensaver_label = tk.Label(screensaver_tab, text="Screen saver:", bg="white", fg="black", font=("Arial", 10))
        screensaver_label.pack(anchor=tk.W, padx=10, pady=5)
        
        screensaver_var = tk.StringVar(value="(None)")
        screensaver_options = ["(None)", "Bliss", "3D Text", "Mystify"]
        screensaver_menu = tk.OptionMenu(screensaver_tab, screensaver_var, *screensaver_options)
        screensaver_menu.pack(fill=tk.X, padx=10, pady=5)
        
        # Settings tab
        settings_tab = tk.Frame(notebook, bg="white")
        notebook.add(settings_tab, text="Settings")
        
        resolution_label = tk.Label(settings_tab, text="Screen resolution:", bg="white", fg="black", font=("Arial", 10))
        resolution_label.pack(anchor=tk.W, padx=10, pady=5)
        
        resolution_var = tk.StringVar(value="1024 x 768")
        resolution_options = ["800 x 600", "1024 x 768", "1280 x 1024"]
        resolution_menu = tk.OptionMenu(settings_tab, resolution_var, *resolution_options)
        resolution_menu.pack(fill=tk.X, padx=10, pady=5)
        
        color_quality_label = tk.Label(settings_tab, text="Color quality:", bg="white", fg="black", font=("Arial", 10))
        color_quality_label.pack(anchor=tk.W, padx=10, pady=5)
        
        color_quality_var = tk.StringVar(value="Medium (16 bit)")
        color_quality_options = ["Low (8 bit)", "Medium (16 bit)", "High (32 bit)"]
        color_quality_menu = tk.OptionMenu(settings_tab, color_quality_var, *color_quality_options)
        color_quality_menu.pack(fill=tk.X, padx=10, pady=5)
        
        # Apply button
        apply_btn = tk.Button(
            settings_tab,
            text="Apply",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        apply_btn.pack(side=tk.RIGHT, padx=10, pady=10)
        
    def open_background_settings(self):
        window = self.window_manager.create_window("Desktop Background", 500, 400)
        window_id = window.window_id
        self.open_apps["background_settings"] = window_id
        
        # Create content area
        content = tk.Frame(window.content, bg="white")
        content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Background selection
        bg_label = tk.Label(content, text="Background:", bg="white", fg="black", font=("Arial", 10))
        bg_label.pack(anchor=tk.W, pady=5)
        
        # Background options
        bg_frame = tk.Frame(content, bg="white")
        bg_frame.pack(fill=tk.X, pady=5)
        
        bg_var = tk.StringVar(value="Bliss")
        bg_options = ["Bliss", "Autumn", "Azul", "Classic", "None"]
        
        for option in bg_options:
            rb = tk.Radiobutton(
                bg_frame,
                text=option,
                variable=bg_var,
                value=option,
                bg="white",
                fg="black",
                font=("Arial", 9),
                anchor=tk.W
            )
            rb.pack(fill=tk.X, pady=2)
            
        # Position selection
        pos_label = tk.Label(content, text="Position:", bg="white", fg="black", font=("Arial", 10))
        pos_label.pack(anchor=tk.W, pady=5)
        
        pos_frame = tk.Frame(content, bg="white")
        pos_frame.pack(fill=tk.X, pady=5)
        
        pos_var = tk.StringVar(value="Stretch")
        pos_options = ["Stretch", "Tile", "Center"]
        
        for option in pos_options:
            rb = tk.Radiobutton(
                pos_frame,
                text=option,
                variable=pos_var,
                value=option,
                bg="white",
                fg="black",
                font=("Arial", 9),
                anchor=tk.W
            )
            rb.pack(fill=tk.X, pady=2)
            
        # Color selection
        color_label = tk.Label(content, text="Color:", bg="white", fg="black", font=("Arial", 10))
        color_label.pack(anchor=tk.W, pady=5)
        
        color_frame = tk.Frame(content, bg="white")
        color_frame.pack(fill=tk.X, pady=5)
        
        color_var = tk.StringVar(value="Blue")
        color_options = ["Blue", "Green", "Red", "Yellow", "Purple", "Black"]
        
        for option in color_options:
            rb = tk.Radiobutton(
                color_frame,
                text=option,
                variable=color_var,
                value=option,
                bg="white",
                fg="black",
                font=("Arial", 9),
                anchor=tk.W
            )
            rb.pack(fill=tk.X, pady=2)
            
        # Apply button
        apply_btn = tk.Button(
            content,
            text="Apply",
            bg="#ECE9D8",
            relief=tk.RAISED,
            bd=1
        )
        apply_btn.pack(side=tk.RIGHT, padx=10, pady=10)

class CalculatorLogic:
    def __init__(self, display):
        self.display = display
        self.expression = ""
        
    def append(self, value):
        self.expression += value
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        
    def calculate(self):
        try:
            # Replace display symbols with Python operators
            expression = self.expression.replace("×", "*").replace("÷", "/")
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""