import tkinter as tk

from application import Application
    
def main():     
    root = tk.Tk()
    
    root.tk.call("source", "forest-dark.tcl")
    root.tk.call("source", "forest-light.tcl")
    
    root.title("Excel App")
    app = Application(root) #It calls the __init__ method of Application.
    root.mainloop()
    
if __name__ == "__main__":
    main()