import tkinter as tk
from tkcalendar import Calendar
import openpyxl

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
    path = "C:/Users/insen/OneDrive/Desktop/Coding/Python/Projects/Excel_App/Employee_List.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active  # Choose the active sheet from the Excel File

    list_values = list(sheet.values)
    print(list_values)

    for index, col_name in enumerate(list_values[0]):
        self.treeview.column(f"# {index + 1}", anchor="w")
        self.treeview.heading(f"# {index + 1}", text=col_name)

    for value in list_values[1:]:
        self.treeview.insert("", "end", values=value)
    
    