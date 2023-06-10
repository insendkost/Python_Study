import customtkinter as ctk
import commands


theme = ctk.set_default_color_theme("app_theme.json")

ctk.set_appearance_mode("dark")

root = ctk.CTk()  # Create a root window
root.title("To Do List")  # Set title of the root window
root.geometry("500x500")  # Set geometry of the root window


tasks = {}  # Create a dictionary to store tasks


# Set default color theme

title_label = ctk.CTkLabel(
    root,
    text="Daily Tasks",
    font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"),
)  # Create a label

# Create a scrollable frame

scrollable_frame = ctk.CTkScrollableFrame(root, height=250)

# create a lsit box

# list_box = ctk.CTkListBox(scrollable_frame)
# list_box.pack(fill="x")
# create an entry

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add a task...")

# Create an add button

add_button = ctk.CTkButton(
    root,
    text="Add",
    width=100,
    fg_color="gray",
    command=lambda: commands.add_todo(entry, scrollable_frame, ctk, tasks),
)

spacer = ctk.CTkLabel(root, text="", width=10)

delete_button = ctk.CTkButton(
    root,
    text="Delete",
    width=100,
    fg_color="gray",
    command=commands.delete_todo(entry, tasks),
)


# Pack the label
title_label.pack(padx=10, pady=(40, 20))
scrollable_frame.pack(fill="x", pady=5)
entry.pack(fill="x")

add_button.pack(side=ctk.LEFT, padx=10, pady=10)
spacer.pack(side=ctk.LEFT, pady=30)
delete_button.pack(side=ctk.LEFT, padx=10, pady=10)

root.mainloop()
