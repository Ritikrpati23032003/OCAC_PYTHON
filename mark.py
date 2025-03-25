import tkinter as tk
from tkinter import messagebox

# Sample student database
students = {}

# Function to add a student
def add_student():
    name = entry_name.get()
    id_number = entry_id.get()
    reg_number = entry_reg.get()
    phone_number = entry_phone.get()
    marks = entry_marks.get()
    if name and id_number and reg_number and phone_number and marks:
        students[id_number] = {
            "name": name,
            "reg_number": reg_number,
            "phone_number": phone_number,
            "marks": marks,
        }
        messagebox.showinfo("Success", f"Student {name} added with ID {id_number}")
    else:
        messagebox.showwarning("Error", "Please enter all details")

# Function to delete a student
def delete_student():
    id_number = entry_id.get()
    if id_number in students:
        del students[id_number]
        messagebox.showinfo("Success", f"Student with ID {id_number} deleted")
    else:
        messagebox.showwarning("Error", "Student ID not found")

# Function to view students
def view_students():
    if students:
        student_list = "\n".join(
            [
                f"ID: {id_num}, Name: {info['name']}, Reg No: {info['reg_number']}, "
                f"Phone: {info['phone_number']}, Marks: {info['marks']}"
                for id_num, info in students.items()
            ]
        )
        messagebox.showinfo("Student List", student_list)
    else:
        messagebox.showinfo("Student List", "No students in the database")

# Function to update a student
def update_student():
    name = entry_name.get()
    id_number = entry_id.get()
    reg_number = entry_reg.get()
    phone_number = entry_phone.get()
    marks = entry_marks.get()
    if id_number in students:
        students[id_number] = {
            "name": name,
            "reg_number": reg_number,
            "phone_number": phone_number,
            "marks": marks,
        }
        messagebox.showinfo("Success", f"Student ID {id_number} updated")
    else:
        messagebox.showwarning("Error", "Student ID not found")

# Function to handle button clicks
def handle_action(action):
    actions = {
        "Add": add_student,
        "Delete": delete_student,
        "View": view_students,
        "Update": update_student,
    }
    action_function = actions.get(action)
    if action_function:
        action_function()

# Creating the main window
root = tk.Tk()
root.title("Student Database")

# Setting the window background color
root.configure(bg='lightyellow')

# Creating input fields and labels with colors
tk.Label(root, text="Student Name", bg='lightyellow', fg='purple').grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Student ID", bg='lightyellow', fg='purple').grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Registration No.", bg='lightyellow', fg='purple').grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Phone No.", bg='lightyellow', fg='purple').grid(row=3, column=0, padx=10, pady=5)
tk.Label(root, text="Marks", bg='lightyellow', fg='purple').grid(row=4, column=0, padx=10, pady=5)

entry_name = tk.Entry(root)
entry_id = tk.Entry(root)
entry_reg = tk.Entry(root)
entry_phone = tk.Entry(root)
entry_marks = tk.Entry(root)

entry_name.grid(row=0, column=1, padx=10, pady=5)
entry_id.grid(row=1, column=1, padx=10, pady=5)
entry_reg.grid(row=2, column=1, padx=10, pady=5)
entry_phone.grid(row=3, column=1, padx=10, pady=5)
entry_marks.grid(row=4, column=1, padx=10, pady=5)

# Creating buttons for different actions with colors
actions = ["Add", "Delete", "View", "Update"]
button_colors = {"Add": "green", "Delete": "red", "View": "blue", "Update": "orange"}

for idx, action in enumerate(actions):
    button = tk.Button(root, text=action, command=lambda a=action: handle_action(a), bg=button_colors[action], fg='white')
    button.grid(row=5, column=idx, padx=10, pady=10)

# Running the main loop
root.mainloop()