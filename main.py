from tkinter import *
from PIL import Image, ImageTk

root = Tk() # Start Body

root.title('First GUI') # Add title
root.geometry('600x400') # Width x Height | Window default size
root.minsize(400,300) # Width , Height | Window minimum size
root.maxsize(900,500) # Width , Height | Window maximum size

text = Label(
    text='Hello my name is python', # text to show
    bg='black', # background color
    fg='white', # font color
    padx=20,    # padding left and right
    pady=15,    # padding top and bottom
    font=('robot',20, 'bold'), # font style and size and bold
    borderwidth=5, # Border with
    relief="sunken" # Border style
) # create Text
text.pack(
    side=TOP, # fix to | TOP | BOTTOM | LEFT | RIGHT
    fill=X,   # Width auto and | Y for Height | Responsive
    pady=20   # Padding Top and Bottom
) # show Text in body without this text does not display

# Read the Image
image = Image.open("img.png")
# Resize the image using resize() method
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.pack(side=BOTTOM, pady=20) # show Image in body without this Image does not display





#image = PhotoImage(file='img.png')
#image_label = Label(image=image)
#image_label.pack()

root.mainloop() # End Body