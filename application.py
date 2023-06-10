
from tkinter import ttk

from functions import *

departments_list = ["BI","Personal Banking","Corporate Banking","Finance","HR","IT","Marketing","Operations", "Risk","Sales", "Security","Treasury","R&D","Other"]
                                                                       
table_cols = ("First Name", "Last Name", "Phone Number","ID", "Department")
class Application:
    def __init__(self, root):
        self.root = root
        self.calendar_window = None
        self.cal = None

        self.style = ttk.Style(root)
        self.frame = ttk.Frame(root)
        
        style = ttk.Style(self.root)
        self.root.tk.call("source", "C:/Users/insen/OneDrive/Desktop/Coding/Python/Projects/Excel_App/Forest-ttk-theme/forest-dark.tcl")
        self.root.tk.call("source", "C:/Users/insen/OneDrive/Desktop/Coding/Python/Projects/Excel_App/Forest-ttk-theme/forest-light.tcl")
        style.theme_use('forest-dark')
        
        self.frame.pack()

        self.widgets_frame = ttk.LabelFrame(self.frame, text="Insert Row")
        self.widgets_frame.grid(row=0, column=0, padx=20, pady = 10)

        self.fisrt_name_entry = ttk.Entry(self.widgets_frame)
        self.fisrt_name_entry.insert(0, "First Name")
        self.fisrt_name_entry.bind("<FocusIn>", lambda e: self.fisrt_name_entry.delete(0, "end"))
        self.fisrt_name_entry.grid(row=0, column=0,padx=5,pady=(0,5), sticky="ew")
        
        self.last_name_entry = ttk.Entry(self.widgets_frame)
        self.last_name_entry.insert(0, "Last Name")
        self.last_name_entry.bind("<FocusIn>", lambda e: self.last_name_entry.delete(0, "end"))
        self.last_name_entry.grid(row=1, column=0,padx=5,pady=(0,5), sticky="ew")
        
        self.phone = ttk.Entry(self.widgets_frame)
        self.phone.insert(0, "Phone Number")
        self.phone.bind("<FocusIn>", lambda e: self.phone.delete(0, "end"))
        self.phone.grid(row=2, column=0,padx=5,pady=(0,5), sticky="ew")


        self.select_date_button = ttk.Button(self.widgets_frame, text="Date of Birth", command=lambda: open_calendar(self))
        self.select_date_button.grid(row=3, column=0,padx=5,pady=(0,5), sticky="ew")
        
        self.department_entry = ttk.Combobox(self.widgets_frame, values=departments_list)
        self.department_entry.insert(0, "Select from a dropdown list")
        #self.department_entry.bind("<FocusIn>", lambda e: self.department_entry.delete(None))
        self.department_entry.grid(row=4, column=0,padx=5,pady=(0,5), sticky="ew")
        
        
        a = tk.BooleanVar()
        self.checkbuttom = ttk.Checkbutton(self.widgets_frame, text="Bank Employee",variable=a)
        self.checkbuttom.grid(row=5, column=0,padx=5,pady=(0,5), sticky="nsew")

        self.submit_button = ttk.Button(self.widgets_frame, text="Submit") #, command=lambda: submit(self))
        self.submit_button.grid(row=6, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #ADDING A SEPARATOR
        
        self.separator = ttk.Separator(self.widgets_frame, orient="horizontal")
        self.separator.grid(row=7, column=0, sticky="ew", pady=10)
        
        #LIGHT THEME BUTTON
        
        self.switch_mode_button = ttk.Checkbutton(self.widgets_frame, text = "Mode", style="Switch",command=lambda: switch_mode(self))
        self.switch_mode_button.grid(row=8, column=0, padx = 5 ,pady=10,sticky="nsew")

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
        
        load_data(self)
        
#NEXT STEPS: 
# 1.UPDATE FIELDS WITH THE SELECTED ROW
# 2. ADD A DELETE BUTTON
# 3. ADD A SEARCH BUTTON
# 4. ADD AN OPTION TO EDIT A DATA INSIDE THE EXCEL FILE FROM THE APP
# 5. ADD A FUNCTION THAT WILL CLEAR THE WHITESPACES IN APP VIEW
# 6. ADD AN OPTION TO SAVE BY CLOSING THE APP
# 7. ADD A BUTTON + DOUBLE CLICK TO GET A FULL DATA OF THE SELECTED ROW
# 8. ADD A FUNCTION THAT WILL LIMIT THE NUMBER OF CHARACTERS IN THE ENTRY FIELDS
# 8. ADD A FUNCTION THAT WILL LIMIT NEW ROWS TO BE ADDED IF EXISTS
    
    