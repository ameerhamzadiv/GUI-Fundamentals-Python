from tkinter import *

error = False
errorval = 'ok'
root = Tk()

def userdata():
    if nameval.get().strip() or emailval.get().strip():  # Check if the value is not empty after removing leading/trailing spaces
        print("name is:", nameval.get())
        print("email is:", emailval.get())
        with open('usersdata.txt','a') as u:
            u.write(f'Name: {nameval.get()},\nEmail: {emailval.get()}\n\n')
        nameval.set('')
        emailval.set('')

    else:
        print("Value is empty")
        error = True
        errorval = 'Required'
        print(error)
        print(errorval)


root.geometry('500x400')

name_label = Label(root, text='Name')
email_label = Label(root, text='Email')

name_label.grid(row = 0, column = 0, sticky = W, pady=2)
email_label.grid(row = 1, column = 0, sticky = W, pady=2)

nameval = StringVar()
emailval = StringVar()

name_input = Entry(root, textvariable=nameval)
email_input = Entry(root, textvariable=emailval)

name_input.grid(row = 0, column = 1, pady=2)
email_input.grid(row = 1, column = 1, pady=2)

btn = Button(root, text='Submit', command=userdata).grid()


if error:
   Label(root, text=errorval, fg='red').grid()



root.mainloop()