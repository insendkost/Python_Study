<<<<<<< HEAD

from common import ttk,tk
import functions as func
from application import Application

departments_list = ["BI","Personal Banking","Corporate Banking","Finance","HR","IT","Marketing","Operations", "Risk","Sales", "Security","Treasury","R&D","Other"]


class ExtendedApplication:
    def __init__(self,root):
        
        self.root = root
        
        self.calendar_window = None
        self.cal = None
        
        self.style = ttk.Style(root)
        self.style.theme_use('forest-dark')
        
        frame_ext = ttk.Frame(root)
        frame_ext.pack()

       
        
        #ADDING ENTRY FIELDS
        #FIRST NAME 
        fisrt_name_entry = ttk.Entry(frame_ext)
        fisrt_name_entry.insert(0, "First Name")
        fisrt_name_entry.bind("<FocusIn>", lambda e: fisrt_name_entry.delete(0, "end"))
        fisrt_name_entry.grid(row=0, column=0,padx=5,pady=(0,5), sticky="ew")
        #LAST NAME
        self.last_name_entry = ttk.Entry(frame_ext)
=======
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
>>>>>>> fe4573b6fde9d32d55748c1b298dd8d691690983
        self.last_name_entry.insert(0, "Last Name")
        self.last_name_entry.bind("<FocusIn>", lambda e: self.last_name_entry.delete(0, "end"))
        self.last_name_entry.grid(row=1, column=0,padx=5,pady=(0,5), sticky="ew")
        #PHONE NUMBER
<<<<<<< HEAD
        self.phone = ttk.Entry(frame_ext)
=======
        self.phone = ttk.Entry(self.widgets_frame)
>>>>>>> fe4573b6fde9d32d55748c1b298dd8d691690983
        self.phone.insert(0, "Phone Number")
        self.phone.bind("<FocusIn>", lambda e: self.phone.delete(0, "end"))
        self.phone.grid(row=2, column=0,padx=5,pady=(0,5), sticky="ew")

        #CALENDAR BUTTON
        
<<<<<<< HEAD
        self.select_date_button = ttk.Button(frame_ext, text="Date of Birth", command=lambda: func.open_calendar(self))
        self.select_date_button.grid(row=3, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #DEPARTMENT DROPDOWN
        self.department_entry = ttk.Combobox(frame_ext, values=departments_list)
=======
        self.select_date_button = ttk.Button(self.widgets_frame, text="Date of Birth", command=lambda: open_calendar(self))
        self.select_date_button.grid(row=3, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #DEPARTMENT DROPDOWN
        self.department_entry = ttk.Combobox(self.widgets_frame, values=departments_list)
>>>>>>> fe4573b6fde9d32d55748c1b298dd8d691690983
        self.department_entry.insert(0, "Select from a dropdown list")
        #self.department_entry.bind("<FocusIn>", lambda e: self.department_entry.delete(None))
        self.department_entry.grid(row=4, column=0,padx=5,pady=(0,5), sticky="ew")
        
        #CHECKBUTTON
        
        a = tk.BooleanVar()
<<<<<<< HEAD
        self.checkbuttom = ttk.Checkbutton(frame_ext, text="Bank Employee",variable=a)
=======
        self.checkbuttom = ttk.Checkbutton(self.widgets_frame, text="Bank Employee",variable=a)
>>>>>>> fe4573b6fde9d32d55748c1b298dd8d691690983
        self.checkbuttom.grid(row=5, column=0,padx=5,pady=(0,5), sticky="nsew")

        #SUBMIT BUTTON
        
<<<<<<< HEAD
        self.submit_button = ttk.Button(frame_ext, text="Submit") #, command=lambda: submit(self))
=======
        self.submit_button = ttk.Button(self.widgets_frame, text="Submit") #, command=lambda: submit(self))
>>>>>>> fe4573b6fde9d32d55748c1b298dd8d691690983
        self.submit_button.grid(row=6, column=0,padx=5,pady=(0,5), sticky="ew")
        