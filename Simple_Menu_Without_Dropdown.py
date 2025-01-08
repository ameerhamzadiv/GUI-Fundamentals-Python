from tkinter import *

root = Tk()

root.geometry('700x500')
root.title('Add Simple menu in GUI')

def home_menu():
    print('You click on Home menu')
def view_menu():
    print('You click on view menu')
def tools_menu():
    print('You click on Tools menu')
def window_menu():
    print('You click on Window menu')


mymenu = Menu(root)
mymenu.add_command(label='Home', command=home_menu)
mymenu.add_command(label='View', command=view_menu)
mymenu.add_command(label='Tools', command=tools_menu)
mymenu.add_command(label='Window', command=window_menu)
root.config(menu=mymenu)




root.mainloop()