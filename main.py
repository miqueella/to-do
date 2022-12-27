from tkinter import *

root = Tk()
root.title("To-Do")
root.geometry("400x650+400+100")
root.resizable(False,False)
root.config(bg="#F3F3F3")

task_list=[]

def deleteTask():
    global  task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt', 'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete(ANCHOR)

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open('tasklist.txt', 'a') as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END, task)

def openTaskFile():
    try:
        global task_list
        with open('tasklist.txt', 'r') as taskfile:
            tasks = taskfile.readlines()
    
        for task in tasks:
          if task !='\n':
            task_list.append(task)
            listbox.insert(END, task)
    
    except:
        file = open('tasklist.txt', 'w')
        file.close()


github = Label(text="TO-DO LIST!")
github.place(x=167,y=0)

frame = Frame(root,width=400,height=50,bg="#fff")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="Arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()


button = Button(frame, text="ADD", font="Arial 20 bold", width=6, bg="#e5e5e5",fg="#212121", command=addTask)
button.place(x=300,y=0)

frame_list = Frame(root, bd=3, width=700, height=280, bg="#e7e7e7")
frame_list.pack(pady=(250,0))

listbox = Listbox(frame_list, font="Arial 12", width=40, height=16, bg="#fff", fg="#212121", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame_list)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

delete = Button(root, text="Delete", bd=0, height=300, font="Arial 20",command=deleteTask)
delete.pack(side=BOTTOM, pady=0)

openTaskFile()

root.mainloop()