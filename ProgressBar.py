from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.geometry('600x400')
root.title('Progress Bar')

def rateus():
    print('you submitted')
    tmsg.showinfo('Rate',f'You Rate us {bar.get()} points')

Label(root, text='Rate us',font=('robots',15,'bold')).pack()
bar = Scale(root, from_=0, to=10, orient="horizontal")
bar.pack()

Button(root, text='Submit', command=rateus).pack()


root.mainloop()