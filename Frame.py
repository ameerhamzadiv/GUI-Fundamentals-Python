from tkinter import *

root = Tk()
root.title('Frame Practice')
root.geometry('600x400')

left_sidebar = Frame(root, bg="black", pady=20, padx=20)
left_sidebar.pack(side=LEFT, fill=Y)
right_side = Frame(root, bg='red', pady=5, padx=5)
right_side.pack(side=TOP, fill=X)

home = Label(left_sidebar, text='Home', bg='black', fg='white', pady=5).pack()
about = Label(left_sidebar, text='About', bg='black', fg='white', pady=5).pack()
shop = Label(left_sidebar, text='Shop', bg='black', fg='white', pady=5).pack()
contact = Label(left_sidebar, text='Contact Us', bg='black', fg='white', pady=5).pack()

welcome = Label(right_side, text='Welcome to Python').pack()
left_box1 = Label(right_side, text='Box 1', bg='yellow', pady=22,padx=22, borderwidth=2, relief='raised').pack(side=LEFT, fill=X)
left_box2 = Label(right_side, text='Box 2', bg='yellow', pady=22,padx=22, borderwidth=2, relief='raised').pack(side=LEFT, fill=X)
left_box3 = Label(right_side, text='Box 3', bg='yellow', pady=22,padx=22, borderwidth=2, relief='raised').pack(side=LEFT, fill=X)
left_box4 = Label(right_side, text='Box 4', bg='yellow', pady=22,padx=22, borderwidth=2, relief='raised').pack(side=LEFT, fill=X)
left_box5 = Label(right_side, text='Box 5', bg='yellow', pady=22,padx=22, borderwidth=2, relief='raised').pack(side=LEFT, fill=X)
left_box6 = Label(right_side, text='Box 6', bg='yellow', pady=22,padx=22, borderwidth=2, relief='raised').pack(side=LEFT, fill=X)



root.mainloop()
