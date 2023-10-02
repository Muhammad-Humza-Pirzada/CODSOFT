import tkinter as tk
from tkinter import *

root = Tk()
root.title("Todo List")
root.geometry("300x550+500+80")
root.resizable(False, False)

task_list=[
    
]

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open('tasklist.txt', 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listBox.insert( END, task)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listBox.insert(END, task)
    except:
        file=open('tasklist.txt', 'w')
        file.close()
    
def deleteTask():
    global task_list
    task = str(listBox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt', 'a') as taskfile:  # Open the file in 'a' (append) mode
            taskfile.write(task + "\n")   
        listBox.delete(ANCHOR)
       

# icon image
Image_icon = PhotoImage(file="Image/note.png")
root.iconphoto(False, Image_icon)

# top bar

TopImage = PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage).pack()


# text_label = tk.Label(text="Hello, Tkinter!")
# text_label.pack(pady=20)

# heading
heading = Label(root, text='Todo List', font='YourCustomHandwritingFont', fg='orange')
heading.place(x=110, y=20)


# main
frame = Frame(root, width=400, height=50, bg='white')
frame.place(x=0, y=100)

task=StringVar()
task_entry = Entry(frame, width=25, font='YourCustomHandwritingFont', bd=2)
task_entry.place(x=11, y=10)
task_entry.focus()

# add button
addButton = Button(text="Add", font='YourCustomHandwritingFont',fg='black', width=10, bg='lightblue' , bd=2, command=addTask)
addButton.place(x=90, y=150)

# list box
frame1 = Frame(root, bd=3, width=400, height=300, bg='lightgreen')
frame1.pack(pady=(130,0))

listBox = Listbox(frame1, font=('YourCustomHandwritingFont', 12), width=30, height=10, bg='lightblue', fg='black', cursor='hand2', selectbackground='red')
listBox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=LEFT, fill=BOTH)

listBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listBox.yview)

# delete button
deleteButton = Button(text="Delete", font='YourCustomHandwritingFont',fg='white', width=10, bg='Red' ,bd=2, command=deleteTask)
deleteButton.place(x=90, y=450)

# funtion of task
openTaskFile()

root.mainloop()