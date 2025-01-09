from tkinter import *


root = Tk()
root.geometry('600x400')
root.title('ListBox in GUI')

# Create ListBox
listbox = Listbox(root)
listbox.pack()

# Add Text in ListBox
listbox.insert(END, 'Item 1')
listbox.insert(END,'Item 2')


root.mainloop()