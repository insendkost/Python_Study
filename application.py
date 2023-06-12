
from common import ttk,tk
import functions as func


                                                                       
table_cols = ("First Name", "Last Name", "Phone Number","ID", "Department")
class BaseWindow:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style(root)
        self.frame = ttk.Frame(root)
        self.frame.pack()
        
    def apply_theme(self):
        style = ttk.Style(self.root)
        style.theme_use('forest-dark')
    


class Application(BaseWindow):
    def __init__(self, root):
        super().__init__(root) #This super().__init__(root) calls the __init__ method of BaseApplication 
        
        

        self.apply_theme()
        
        
        self.style.configure('Custom.TButton', foreground='white', background='black')
        self.style.map('Custom.TButton',
                       foreground=[('disabled', 'white')],
                       background=[('disabled', 'lightgray')])
        
        self.widgets_frame = ttk.LabelFrame(self.frame, text="Rows Control")
        self.widgets_frame.grid(row=0, column=0, padx=20, pady = 10)

        self.file_buttons_frame = ttk.LabelFrame(self.frame, text="Files")
        self.file_buttons_frame.grid(row=1, column=1, padx=20, pady = 10)
        
        # #ADDING ENTRY FIELDS
        # #FIRST NAME 
        # self.fisrt_name_entry = ttk.Entry(self.widgets_frame)
        # self.fisrt_name_entry.insert(0, "First Name")
        # self.fisrt_name_entry.bind("<FocusIn>", lambda e: self.fisrt_name_entry.delete(0, "end"))
        # self.fisrt_name_entry.grid(row=0, column=0,padx=5,pady=(0,5), sticky="ew")
        # #LAST NAME
        # self.last_name_entry = ttk.Entry(self.widgets_frame)
        # self.last_name_entry.insert(0, "Last Name")
        # self.last_name_entry.bind("<FocusIn>", lambda e: self.last_name_entry.delete(0, "end"))
        # self.last_name_entry.grid(row=1, column=0,padx=5,pady=(0,5), sticky="ew")
        # #PHONE NUMBER
        # self.phone = ttk.Entry(self.widgets_frame)
        # self.phone.insert(0, "Phone Number")
        # self.phone.bind("<FocusIn>", lambda e: self.phone.delete(0, "end"))
        # self.phone.grid(row=2, column=0,padx=5,pady=(0,5), sticky="ew")

        # #CALENDAR BUTTON
        
        # self.select_date_button = ttk.Button(self.widgets_frame, text="Date of Birth", command=lambda: func.open_calendar(self))
        # self.select_date_button.grid(row=3, column=0,padx=5,pady=(0,5), sticky="ew")
        
        # #DEPARTMENT DROPDOWN
        # self.department_entry = ttk.Combobox(self.widgets_frame, values=departments_list)
        # self.department_entry.insert(0, "Select from a dropdown list")
        # #self.department_entry.bind("<FocusIn>", lambda e: self.department_entry.delete(None))
        # self.department_entry.grid(row=4, column=0,padx=5,pady=(0,5), sticky="ew")
        
        # #CHECKBUTTON
        
        # a = tk.BooleanVar()
        # self.checkbuttom = ttk.Checkbutton(self.widgets_frame, text="Bank Employee",variable=a)
        # self.checkbuttom.grid(row=5, column=0,padx=5,pady=(0,5), sticky="nsew")

        # #SUBMIT BUTTON
        
        # self.submit_button = ttk.Button(self.widgets_frame, text="Submit") #, command=lambda: submit(self))
        # self.submit_button.grid(row=6, column=0,padx=5,pady=(0,5), sticky="ew")
        
        
        
        #INSERT BUTTON
        
        self.insert_button = ttk.Button(self.widgets_frame, text="Add new record", command=lambda:func.open_extended_window(self),style="Custom.TButton")
        #
        self.insert_button.grid(row=0, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #EDIT BUTTON
        
        self.edit_button = ttk.Button(self.widgets_frame, text="Edit Row", command=lambda:func.delete_row(self),style="Custom.TButton")
        self.edit_button.grid(row=1, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #FIND BUTTON
        self.search_button = ttk.Button(self.widgets_frame, text="Search", command=lambda:func.search_row(self),style="Custom.TButton")
        self.search_button.grid(row=2, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #DELETE BUTTON
        self.delete_button = ttk.Button(self.widgets_frame, text="Delete Row", command=lambda:func.delete_row(self),style="Custom.TButton")
        self.delete_button.grid(row=3, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #DEFAULT 
        data_loaded = False
        if data_loaded == False:
            func.disable_buttons(self.widgets_frame)
        
            
        #ADDING A SEPARATOR
        
        self.separator = ttk.Separator(self.frame, orient="horizontal")
        self.separator.grid(row=5, column=0, sticky="ew", pady=10)
        
        #LIGHT THEME BUTTON
        
        self.switch_mode_button = ttk.Checkbutton(self.frame, text = "Mode", style="Switch",command=lambda: func.switch_mode(self))
        self.switch_mode_button.grid(row=6, column=0, padx = 5 ,pady=10,sticky="nsew")

        #CREATE A NEW EXCEL FILE
        
        self.create_file_button = ttk.Button(self.file_buttons_frame, text="Create Data File",command=lambda: execute_create_new_file())
        
        def execute_create_new_file():
            func.create_new_file(table_cols)
            func.enable_buttons(self.widgets_frame)
        
        self.create_file_button.grid(row=0, column=0, padx = 5 ,pady=10,sticky="ew")
        
        
        #ADDING A BROWSE FILE BUTTON
        
        self.browse_file_button = ttk.Button(self.file_buttons_frame, text="Browse Files", command=lambda: execute_load_data())
        self.browse_file_button.grid(row=0, column=1, padx = 5 ,pady=10,sticky="ew")
        
        def execute_load_data():
            func.load_data(self)
            func.enable_buttons(self.widgets_frame)
        
        # if data_loaded == True:
        #     func.enable_buttons(self.file_buttons_frame)
        
        #ADDING A EXEL TREE FRAME
        
        self.excel_tree_frame = ttk.Frame(self.frame)
        self.excel_tree_frame.grid(row=0,column=1,pady = 10)
        
        treeScroll = ttk.Scrollbar(self.excel_tree_frame)
        treeScroll.pack(side="right", fill="y")
        
        self.treeview = ttk.Treeview(self.excel_tree_frame,  show="headings",yscrollcommand=treeScroll.set,  columns=table_cols,height=10,)
        
        #SETTING A COLUMNS WIDTH
        
        self.treeview.column("First Name", width=75, anchor="center")
        self.treeview.column("Last Name", width=75, anchor="center")
        self.treeview.column("Phone Number", width=100, anchor="center")
        self.treeview.column("ID", width=100, anchor="center")
        self.treeview.column("Department", width=100, anchor="center")
        
        
        
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview) #tree moves with axe Y
        
        
        

    
    