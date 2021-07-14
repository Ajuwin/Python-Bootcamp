from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

window = Tk()
window.title("File Renaming Tool")
window.geometry('630x220')

label0 = Label(window,text= "File path", font=('Courier New',12,"bold")).place(x=40, y=40)
label1 = Label(window,text= "New filename", font=('Courier New',12,"bold")).place(x=40, y=80)

file = StringVar()
entry0 = Entry(window,textvariable=file,font=('Courier New',11))
entry0.place(x=190, y=40, width=290, height=25)

entry = StringVar()
entry1 = Entry(window, textvariable=entry)
entry1.font=('Courier New',11)
entry1.place(x=190, y=80, width=290, height=25)

def get_file_path():
    global file, filepath
    filepath = filedialog.askopenfilename(initialdir="/home/ajuwin_s/Downloads", title="Select A File", filetypes=(("All files", "*.*"),))
    file.set(filepath)

def renaming_file():
    try:
        renaming = entry.get()
        destination = filepath.replace(os.path.basename(filepath), renaming)
        os.rename(filepath, destination)
        
    except:
        file.set("Cannot find the file.")
    
    else:
        messagebox.showinfo("showinfo", "File Renamed Successfully!")
        file.set("")
        entry.set("")

def close_window():
    window.destroy()

file_name = Button(window, text="Browse", font=('Courier New',11, "bold"), command=get_file_path)
file_name.place(x=500, y=40, height=25)
rename_button = Button(window, text="Rename", font=('Courier New',11, "bold"), command=renaming_file)
rename_button.place(x=500, y=80, height=25)
close_button = Button(window, text="Close", font=('Courier New',11, "bold"), command=close_window)
close_button.place(x=500, y=130, height=25, width=80)

window.mainloop()


