class ExtendedApplication:
    def __init__(self,root):
        self.root = root
        self.frame = ttk.Frame(root)
        self.frame.pack()
        
        
        #ADDING ENTRY FIELDS
        #FIRST NAME 
        self.fisrt_name_entry = ttk.Entry(self.widgets_frame)
        self.fisrt_name_entry.insert(0, "First Name")
        self.fisrt_name_entry.bind("<FocusIn>", lambda e: self.fisrt_name_entry.delete(0, "end"))
        self.fisrt_name_entry.grid(row=0, column=0,padx=5,pady=(0,5), sticky="ew")
        #LAST NAME
        self.last_name_entry = ttk.Entry(self.widgets_frame)
        self.last_name_entry.insert(0, "Last Name")
        self.last_name_entry.bind("<FocusIn>", lambda e: self.last_name_entry.delete(0, "end"))
        self.last_name_entry.grid(row=1, column=0,padx=5,pady=(0,5), sticky="ew")
        #PHONE NUMBER
        self.phone = ttk.Entry(self.widgets_frame)
        self.phone.insert(0, "Phone Number")
        self.phone.bind("<FocusIn>", lambda e: self.phone.delete(0, "end"))
        self.phone.grid(row=2, column=0,padx=5,pady=(0,5), sticky="ew")

        #CALENDAR BUTTON
        
        self.select_date_button = ttk.Button(self.widgets_frame, text="Date of Birth", command=lambda: open_calendar(self))
        self.select_date_button.grid(row=3, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #DEPARTMENT DROPDOWN
        self.department_entry = ttk.Combobox(self.widgets_frame, values=departments_list)
        self.department_entry.insert(0, "Select from a dropdown list")
        #self.department_entry.bind("<FocusIn>", lambda e: self.department_entry.delete(None))
        self.department_entry.grid(row=4, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #CHECKBUTTON
        
        a = tk.BooleanVar()
        self.checkbuttom = ttk.Checkbutton(self.widgets_frame, text="Bank Employee",variable=a)
        self.checkbuttom.grid(row=5, column=0,padx=5,pady=(0,5), sticky="nsew")

        #SUBMIT BUTTON
        
        self.submit_button = ttk.Button(self.widgets_frame, text="Submit") #, command=lambda: submit(self))
        self.submit_button.grid(row=6, column=0,padx=5,pady=(0,5), sticky="ew")
        