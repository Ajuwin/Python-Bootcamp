# importing library
from tkinter import *
from tkinter import filedialog
import tkinter
from PIL import Image
import os

window = Tk()
#Declaring Window Title
window.title("Image Converter")
#Declaring Window size
window.geometry('600x200')

label0 = Label(window,text = "IMAGE CONVERTER", width=25,font=('Cooper Std Black',20,"bold")).place(x=50, y=20)
label1 = Label(window,text= "Folder Path", font=('Courier New',12,"bold")).place(x=15, y=80)
label2 = Label(window,text= "Status", font=('Courier New',12,"bold")).place(x=15, y=130)

dir = tkinter.StringVar()
folder = Entry(window,textvariable=dir,font=('Courier New',11)).place(x=140, y=80, width=325, height=20)

status = tkinter.StringVar()
process = Entry(window,textvariable=status,font=('Courier New',11)).place(x=140, y=130, width=325, height=20)

def get_path():
    global directory
    directory = filedialog.askdirectory(initialdir="C:\\Users\\DELL\\Downloads", title="Select A Folder")
    dir.set(directory)
    status.set("click on convert to start")

def convert_to_png():
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                img = Image.open(directory+"/"+filename, 'r')
                img.save(directory+"/"+filename[:-4]+'.png')
        status.set("Completed")
    except:
        status.set("Error converting files")
    
Button(window, text="Browse", font=('Courier New',11, "bold"), command=get_path).place(x=480, y=75, width=100, height=23)
Button(window, text="Convert", font=('Courier New',11, "bold"), command=convert_to_png).place(x=480, y=125, width=100, height=23)

window.mainloop()
