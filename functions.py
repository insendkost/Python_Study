import tkinter as tk
import openpyxl
import extended_application

from tkcalendar import Calendar
from tkinter import filedialog


def open_calendar(app):
    if app.calendar_window is None or not app.calendar_window.winfo_exists():
        app.calendar_window = tk.Toplevel(app.root)
        app.calendar_window.geometry("230x200")
        app.calendar_window.title("Calendar")
        app.cal = Calendar(app.calendar_window, selectmode='day')
        app.cal.grid(row=0, column=0, sticky="ew")
        
def switch_mode(self):
    if self.style.theme_use() == "forest-dark":
        self.style.theme_use("forest-light")
    else:
        self.style.theme_use("forest-dark")
        
def load_data(self):
    #path = "/Users/evgenykost/Desktop/Coding/PythonProjects/GUI_Projects/Excel_App/Python_Study/Python_Study/Employee_List.xlsx"
    #ALTERNATIVE PATH
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active  # Choose the active sheet from the Excel File

    list_values = list(sheet.values)
    print(list_values)

    for index, col_name in enumerate(list_values[0]):
        self.treeview.column(f"# {index + 1}", anchor="w")
        self.treeview.heading(f"# {index + 1}", text=col_name)

    for value in list_values[1:]:
        self.treeview.insert("", "end", values=value)
    
    workbook.close()
    
def create_new_file(table_cols):
    #Creating a new Excel Files with specific column headers
    workbook = openpyxl.Workbook()
    sheet = workbook.active #Choose the active sheet from the Excel File
    sheet.title = "New Employee List"
    sheet.append(table_cols)
    
    #Open a file dialog to save the file
    root = tk.Tk()
    root.withdraw() #Hides the root window
    
    file_path = filedialog.asksaveasfilename(filetypes=[("Excel Files", "*.xlsx")])
    
    if file_path:
        # Save the file
        workbook.save(file_path)
        workbook.close()
        
        print(f"File saved to {file_path}")

def open_extended_window(self):
    extended_window = tk.Toplevel(self.root)
    extended_app = ExtendedApplication(extended_window)