from tkinter import *
import tkinter.messagebox as tmsg


root  = Tk()
root.geometry('600x400')
root.title('Popups in GUI')

def rateus():
    print('you clicked on: Rate Us')
    value = tmsg.askyesno('Rate','Was your experience good?')
    print(value)
    if value:
        tmsg.showinfo('Thank You', 'Thank you for your answer')

def info():
    print('you clicked on: Info')
    tmsg.showinfo('Info Message', 'You click on Info and this is Info box')


my_manu = Menu(root)
my_manu.add_command(label='Home', command=quit)
my_manu.add_command(label='Rate Us', command=rateus)
my_manu.add_command(label='Info', command=info)

root.config(menu=my_manu)

root.mainloop()