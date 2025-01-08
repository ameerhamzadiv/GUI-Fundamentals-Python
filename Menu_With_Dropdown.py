from tkinter import *

root = Tk()
root.geometry('700x500')
root.title('Menu With Dropdown in GUI')

def newfile_submenu():
    print('you click on: new file')
def save_submenu():
    print('you click on: Save')
def export_submenu():
    print('you click on: Export')

# initialize main menu
main_menu = Menu(root)

# initialize submenu for File menu
file_sub = Menu(main_menu, tearoff=0)

# initialize submenu items for File menu
file_sub.add_command(label='New File', command=newfile_submenu)
file_sub.add_command(label='Save', command=save_submenu)
# for line between menus
file_sub.add_separator()
file_sub.add_command(label='Export', command=export_submenu)

# Create File menu and add submenu items in File menu
main_menu.add_cascade(label='File', menu=file_sub)

# Create main Tool menu
main_menu.add_command(label='Tools', command=quit)

# Add main menu into window body
root.config(menu=main_menu)



root.mainloop()