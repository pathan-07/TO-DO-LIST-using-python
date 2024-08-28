import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_status()
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        update_status()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")

def clear_tasks():
    task_listbox.delete(0, tk.END)
    update_status()

def mark_important():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        if task.startswith("❗"):
            task = task[1:].strip()
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, task)
        else:
            task = f"❗ {task}"
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, task)
        update_status()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as important!")

def update_status():
    task_count = task_listbox.size()
    status_label.config(text=f"Total Tasks: {task_count}")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

# Icons
Image_icon = tk.PhotoImage(file="icons/task.png")
root.iconphoto(False, Image_icon)

# Top bar
top_bar_frame = tk.Frame(root, bg="#4a90e2", height=100)
top_bar_frame.pack(fill=tk.X)

heading = tk.Label(top_bar_frame, text="To-Do List", font=("Helvetica", 24, "bold"), fg="white", bg="#4a90e2")
heading.pack(pady=20)

# Task entry frame
task_entry_frame = tk.Frame(root, bg="#ffffff")
task_entry_frame.place(x=20, y=120, width=360, height=50)

task_entry = tk.Entry(task_entry_frame, font=("Helvetica", 14), width=24)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(task_entry_frame, text="Add", font=("Helvetica", 14), command=add_task, bg="#4a90e2", fg="white")
add_button.pack(side=tk.LEFT, padx=10)

# Task list frame
task_list_frame = tk.Frame(root, bg="#ffffff")
task_list_frame.place(x=20, y=180, width=360, height=350)

task_listbox = tk.Listbox(task_list_frame, font=("Helvetica", 14), width=24, height=15, bd=0, selectbackground="#4a90e2")
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, pady=10)

scrollbar = tk.Scrollbar(task_list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons frame
buttons_frame = tk.Frame(root, bg="#f5f5f5")
buttons_frame.place(x=20, y=540, width=360, height=50)

delete_button = tk.Button(buttons_frame, text="Delete", font=("Helvetica", 14), width=10, command=delete_task, bg="#e74c3c", fg="white")
delete_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(buttons_frame, text="Clear", font=("Helvetica", 14), width=10, command=clear_tasks, bg="#e67e22", fg="white")
clear_button.pack(side=tk.LEFT, padx=5)

important_button = tk.Button(buttons_frame, text="Important", font=("Helvetica", 14), width=10, command=mark_important, bg="#f1c40f", fg="white")
important_button.pack(side=tk.LEFT, padx=5)

# Status bar
status_label = tk.Label(root, text="Total Tasks: 0", font=("Helvetica", 12), bg="#4a90e2", fg="white")
status_label.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()