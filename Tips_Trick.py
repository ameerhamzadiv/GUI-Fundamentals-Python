from tkinter import *


root = Tk()
root.geometry('500x300')

# Change GUI Title
root.title('How to change GUI Icon')

# Change GUI Icon
root.wm_iconbitmap('favicon.ico')

# Change GUI Background Color etc
root.configure(background='red')

# check width height of laptop screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f'{width}x{height}')



root.mainloop()