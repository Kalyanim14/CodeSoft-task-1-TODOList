import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Advanced To-Do List")
root.geometry("800x600")
root.config(bg="#e6e6e6")

# To-Do list container to store task, description, and status
todo_list = []

# Function to update the listbox with tasks
def update_listbox():
    # Clear all items from the task frame
    for widget in task_frame.winfo_children():
        widget.destroy()

    # Display all tasks in the task frame
    for idx, (task, desc, completed) in enumerate(todo_list):
        var = tk.BooleanVar(value=completed)

        # Checkbox to mark task as completed
        checkbox = tk.Checkbutton(task_frame, variable=var, onvalue=True, offvalue=False,
                                  command=lambda idx=idx, var=var: toggle_task(idx, var), bg="#e6e6e6")
        checkbox.grid(row=idx, column=0, sticky="w", padx=10)

        # Label for task
        task_label = tk.Label(task_frame, text=task, font=("Arial", 14, "bold"), anchor="w", wraplength=300, bg="#e6e6e6")
        task_label.grid(row=idx, column=1, sticky="w", padx=10)

        # Label for description
        desc_label = tk.Label(task_frame, text=desc, font=("Arial", 12), anchor="w", wraplength=300, bg="#e6e6e6")
        desc_label.grid(row=idx, column=2, sticky="w", padx=10)

        # Button to edit the task
        edit_button = tk.Button(task_frame, text="Edit", command=lambda idx=idx: edit_task(idx), bg="#f0ad4e", fg="white")
        edit_button.grid(row=idx, column=3, padx=5)

# Function to toggle task completion
def toggle_task(idx, var):
    todo_list[idx] = (todo_list[idx][0], todo_list[idx][1], var.get())
    update_listbox()

# Function to add a new task
def add_task():
    task = entry_task.get()
    desc = entry_desc.get()
    if task and desc:
        todo_list.append((task, desc, False))  # Task is initially marked as incomplete
        update_listbox()
        entry_task.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both task and description.")

# Function to delete completed tasks
def remove_task():
    global todo_list
    todo_list = [task for task in todo_list if not task[2]]  # Remove tasks that are marked completed
    update_listbox()

# Function to edit a task
def edit_task(idx):
    task, desc, completed = todo_list[idx]
    entry_task.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_task.insert(0, task)
    entry_desc.insert(0, desc)
    update_button.config(command=lambda: update_existing_task(idx))  # Modify the Update button for editing

# Function to update an existing task
def update_existing_task(idx):
    task = entry_task.get()
    desc = entry_desc.get()
    if task and desc:
        todo_list[idx] = (task, desc, todo_list[idx][2])  # Keep the completion status unchanged
        update_listbox()
        entry_task.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
        update_button.config(command=add_task)  # Reset the Update button back to adding new tasks
    else:
        messagebox.showwarning("Input Error", "Please enter both task and description.")

# Function to mark all tasks as complete
def complete_all_tasks():
    for idx in range(len(todo_list)):
        todo_list[idx] = (todo_list[idx][0], todo_list[idx][1], True)
    update_listbox()

# Heading Label
heading = tk.Label(root, text="To-Do List", font=("Helvetica", 18), bg="#e6e6e6", pady=10)
heading.pack()

# Frame for task input
input_frame = tk.Frame(root, bg="#e6e6e6")
input_frame.pack(pady=10)

# Entry field for task
entry_task = tk.Entry(input_frame, width=40, font=("Arial", 14))
entry_task.grid(row=0, column=0, padx=5)
task_label = tk.Label(input_frame, text="Task", font=("Arial", 12), bg="#e6e6e6")
task_label.grid(row=0, column=1, padx=5)

# Entry field for description
entry_desc = tk.Entry(input_frame, width=40, font=("Arial", 14))
entry_desc.grid(row=1, column=0, padx=5)
desc_label = tk.Label(input_frame, text="Description", font=("Arial", 12), bg="#e6e6e6")
desc_label.grid(row=1, column=1, padx=5)

# Add task button
update_button = tk.Button(input_frame, text="Add Task", width=20, command=add_task, bg="#5cb85c", fg="white", font=("Arial", 12))
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Frame for displaying tasks
task_frame = tk.Frame(root, bg="#e6e6e6", width=750)
task_frame.pack(pady=10)

# Frame to hold action buttons (Remove and Complete All)
button_frame = tk.Frame(root, bg="#e6e6e6")
button_frame.pack(pady=5)

# Remove completed tasks button
remove_button = tk.Button(button_frame, text="Remove Completed", width=20, command=remove_task, bg="#d9534f", fg="white", font=("Arial", 12))
remove_button.grid(row=0, column=0, padx=5)

# Mark all tasks as complete button
complete_button = tk.Button(button_frame, text="Complete All Tasks", width=20, command=complete_all_tasks, bg="#0275d8", fg="white", font=("Arial", 12))
complete_button.grid(row=0, column=1, padx=5)

# Start the application
root.mainloop()
