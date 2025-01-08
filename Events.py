from tkinter import *

root = Tk()

def clickonbtn(event):
    print('you clicked on button')
def middleclick(event):
    print('Middle Clicked')
def rightclick(event):
    print('Right Clicked')
def Mouse_Position(event):
    print('mouse Position')
    print(event.x, event.y)
def Mouse_Pointer(event):
    print('mouse Pointer')
    print(event.x, event.y)
def Enter_Widget(event):
    print('You Enter in Widget')
def Leave_Widget(event):
    print('You Leave the Widget')
def Any_Key(event):
    print(f'You Press: {event.char}')
def on_configure(event):
    print(f"Window resized: {event.width}x{event.height}")
def Enter_Key_Press(event):
    print("You Press: Enter Key!")


root.geometry('700x500')

btn = Button(root, text='Click here')
btn.pack()

label = Label(root, bg='red', padx=30, pady=30, text='This website contains a free and extensive online tutorial by Bernd Klein, using material from his classroom\n Python training courses.')
label.pack()
# Events
btn.bind('<Button-1>', clickonbtn) # When click on btn then call the function
btn.bind('<Button-2>', middleclick) # When mouse middle click on btn then call the function
btn.bind('<Button-3>', rightclick) # When mouse right click on btn then call the function
# <Button-4> | Scroll up from mouse
# <Button-5> | Scroll down from mouse
btn.bind('<Double-1>', quit) # When double-click on btn then call the function | Default Right double-click
# <Double-Button-1> | Left Double-click
# <Double-Button-2> | middle Double-click
# <Double-Button-3> | right Double-click
btn.bind('<Motion>', Mouse_Position) # When hover on box check mouse position
btn.bind('<ButtonRelease>', Mouse_Pointer) # The current/last position of the mouse pointer when release click
label.bind('<Enter>', Enter_Widget) # When Enter in box then call function
label.bind('<Leave>', Leave_Widget) # When Leave the box then call function
# <FocusIn> | Keyboard focus was moved to this widget, or to a child of this widget.
# <FocusOut> | Keyboard focus was moved from this widget to another widget.
root.bind('<Key>', Any_Key) # When press any key from keyboard
root.bind("<Configure>", on_configure) # when resize window
root.bind("<Return>", Enter_Key_Press) # When press Enter on keyboard
root.mainloop()