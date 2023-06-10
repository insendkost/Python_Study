# add_todo


def add_todo(entry, scrollable_frame, ctk, tasks):
    print("add_todo called")
    todo = entry.get()
    print(f"Adding task: {todo}")
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()
    tasks[todo] = label  # Add the task to the dictionary
    entry.delete(0, ctk.END)  # clear the entry
    print("Task was added")


def delete_todo(entry, tasks):
    todo = entry.get()
    if todo in tasks:
        tasks[todo].destroy()
        del tasks[todo]
