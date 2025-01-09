from tkinter import *


root = Tk()
root.geometry('500x400')
root.title('ScrollBar in GUI')

scrollbar  = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)

for i in range(100):
    listbox.insert(END,f'Item {i}')

listbox.pack()
scrollbar.config(command=listbox.yview)


root.mainloop()