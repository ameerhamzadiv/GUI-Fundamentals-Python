from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.geometry('600x400')
root.title('Radio Button')

def gender():
    print(f'You are a {val.get()}')
    tmsg.showinfo('Gender',f'You are a {val.get()}')

Label(root, text='Gender', font='robots 15 bold').pack()

val = StringVar()
val.set('none')
radio = Radiobutton(root, text='Male', variable=val, value='Male').pack()
radio = Radiobutton(root, text='Female', variable=val, value='Female').pack()

Button(root, text='Submit', command=gender).pack()


root.mainloop()