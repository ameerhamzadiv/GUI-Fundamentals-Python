from tkinter import *


root = Tk()
root.geometry('600x400')
root.title('Radio Button')

def gender():
    if val.get() == 1:
        print('You are a Male')
    elif val.get() == 2:
        print('You are a Female')
Label(root, text='Gender', font='robots 15 bold').pack()

val = IntVar()

radio = Radiobutton(root, text='Male', variable=val, value=1).pack()
radio = Radiobutton(root, text='Female', variable=val, value=2).pack()

Button(root, text='Submit', command=gender).pack()


root.mainloop()