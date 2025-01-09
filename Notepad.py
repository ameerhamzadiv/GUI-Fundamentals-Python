from tkinter import *
from  tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('545x445')
root.title('Untitled - Notepad',)
root.wm_iconbitmap('favicon.ico')


# File
def newFile():
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(
        defaultextension='.txt',
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')]
    )
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + ' - Notepad')
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(
            initialfile='Untitled.txt',
            defaultextension='.txt',
            filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')]
        )
        if file == '':
           file = None
        else:
            # Save New File
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + ' - Notepad')

    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def exitFile():
    global file
    content = TextArea.get(1.0, END).strip()
    if content:
        if file == None:
           box = tmsg.askyesnocancel('Notepad',f'Do you want to save changes to Untitled')
        else:
            box = tmsg.askyesnocancel('Notepad', f'Do you want to save changes to {os.path.basename(file)}')
        if box:
            if file == None:
                file = asksaveasfilename(
                    initialfile='Untitled.txt',
                    defaultextension='.txt',
                    filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')]
                )
                if file == '':
                    file = None
                else:
                    # Save New File
                    f = open(file, 'w')
                    f.write(TextArea.get(1.0, END))
                    f.close()
                    root.title(os.path.basename(file) + ' - Notepad')
                    root.destroy()
            else:
                f = open(file, 'w')
                f.write(TextArea.get(1.0, END))
                f.close()
                root.destroy()
        elif box == None:
            print('none')
        else:
             root.destroy()
    else:
        root.destroy()



   # root.destroy()
# Exit
def cut():
    # Cut the selected Text
    TextArea.event_generate(('<<Cut>>'))

def copy():
    # Get the start and end indexes of the selected text
    start = TextArea.index("sel.first")
    end = TextArea.index("sel.last")

    # Copy Text
    TextArea.event_generate(('<<Copy>>'))

    # Clear the selection
    TextArea.tag_remove("sel", start, end)

def paste():
    TextArea.event_generate(('<<Paste>>'))

def delete():
    # Get the start and end indexes of the selected text
    start = TextArea.index("sel.first")
    end = TextArea.index("sel.last")
    # Delete the selected text
    TextArea.delete(start, end)

def undo():
    try:
        TextArea.edit_undo()  # Undo the last action
    except TclError:
        TextArea.edit_redo()



# Create ScrollBar
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

TextArea = Text(root, yscrollcommand=scrollbar.set, font='lucida 13', borderwidth=1, relief='sunken', wrap=WORD, undo=True)
TextArea.pack(fill=BOTH)
scrollbar.config(command=TextArea.yview)
file = None

# Menu
main_menu = Menu(root)

# File menu
file_submenu = Menu(main_menu, tearoff=0)
file_submenu.add_command(label='New', command=newFile)
file_submenu.add_command(label='Open', command=openFile)
file_submenu.add_command(label='Save', command=saveFile)
file_submenu.add_separator()
file_submenu.add_command(label='Exit', command=exitFile)
main_menu.add_cascade(label='File', menu=file_submenu)

# Edit menu
edit_submenu = Menu(main_menu, tearoff=0)
edit_submenu.add_command(label='Undo', command=undo)
edit_submenu.add_separator()
edit_submenu.add_command(label='Cut', command=cut)
edit_submenu.add_command(label='Copy', command=copy)
edit_submenu.add_command(label='Paste', command=paste)
edit_submenu.add_command(label='Delete', command=delete)
main_menu.add_cascade(label='Edit', menu=edit_submenu)

root.config(menu=main_menu)





root.bind("<Control-z>", lambda event: undo())
root.protocol("WM_DELETE_WINDOW", exitFile)
root.mainloop()