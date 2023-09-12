#Language: Python
#Author: Cerberus16731

"""
                                 ---DOCSTRING---
This program is a simple GUI program that helps adds and removes from a To Do List.
"""

#importing dependancies
import tkinter as tk
import tkinter.ttk as ttk
import random

def main():
    my_labels = {}
    #adds labels, linked to button press
    def add():
        text = entry_task.get()
        new_label = ttk.Label(root,text=f"{text}")
        my_labels[(text,random.random())] = new_label
        new_label.grid(column = 2)
    #removes labels, linked to button press
    def remove():
        text = entry_task.get()
        for (label_name,key),label in my_labels.items():
            if label_name == text:
                label.destroy()
    #exports to do list to a textfile on the system
    def export():
        root.destroy()
        with open("todo.txt","a") as f:
            from datetime import datetime as dt
            f.write(f"{dt.today(),dt.now()} \n")
            for (label_name,key),label in my_labels.items():
                f.write(label_name+"\n")
            f.flush()

    #GUI Window layout
    root = tk.Tk()
    root.title("Tasks")
    root.geometry("300x300")
    label_task = ttk.Label(root, text = "Task:")
    entry_task = ttk.Entry(root)
    button_add = ttk.Button(root, text = "Add Task", command = add)
    button_remove = ttk.Button(root,text = "Remove Task",command = remove)
    button_export =ttk.Button(root,text = "Export",command =  export)
    label_task.grid(row = 1,column = 2)
    entry_task.grid(row = 2, column= 2)
    button_add.grid(row = 3, column = 1)
    button_remove.grid(row = 3, column= 2)
    button_export.grid(row = 3,column =3)
    root.mainloop()

if __name__ == '__main__':
     main()



