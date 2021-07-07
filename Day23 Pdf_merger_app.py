# importing library
from tkinter import *
from tkinter import filedialog
import tkinter
import PyPDF2

window = Tk()
#Declaring Window Title
window.title("Pdf Merger App")
#Declaring Window size
window.geometry('600x220')

label0 = Label(window,text = "PDF MERGER", width=25,font=('Cooper Std Black',20,"bold")).place(x=50, y=20)
label1 = Label(window,text= "Pdf 1", font=('Courier New',12,"bold")).place(x=40, y=80)
label2 = Label(window,text= "Pdf 2", font=('Courier New',12,"bold")).place(x=40, y=120)
label3 = Label(window,text= "Status", font=('Courier New',12,"bold")).place(x=40, y=160)

file1 = tkinter.StringVar()
file2 = tkinter.StringVar()
ent1 = Entry(window,textvariable=file1,font=('Courier New',11)).place(x=140, y=80, width=325, height=20)
ent2 = Entry(window,textvariable=file2,font=('Courier New',11)).place(x=140, y=120, width=325, height=20)

status = tkinter.StringVar()
process = Entry(window,textvariable=status,font=('Courier New',11)).place(x=140, y=160, width=325, height=20)

def get_pdf1():
    global file1
    path1 = filedialog.askopenfilename(initialdir="C:\\Users\\DELL\\Downloads", title="Select A File", filetypes=(("pdf files", "*.pdf"),))
    file1.set(path1)

def get_pdf2():
    global file2
    path2 = filedialog.askopenfilename(initialdir="C:\\Users\\DELL\\Downloads", title="Select A File", filetypes=(("pdf files", "*.pdf"),))
    file2.set(path2)
    status.set("Click on Merge to start")

def convert_pdf():
    temp = PyPDF2.PdfFileReader(open(file1,'rb'))
    water = PyPDF2.PdfFileReader(open(file2,'rb'))

    output = PyPDF2.PdfFileWriter()

    for i in range(temp.getNumPages()):
        page = temp.getPage(i)
        page.mergePage(water.getPage(0))
        output.addPage(page)

        with open('C:\\Users\\Dell\\Downloads\\watermarked_output.pdf','wb') as file:
            output.write(file)
    status.set("Done")


Button(window, text="Browse", font=('Courier New',11, "bold"), command=get_pdf1).place(x=480, y=80, width=100, height=23)
Button(window, text="Browse", font=('Courier New',11, "bold"), command=get_pdf2).place(x=480, y=120, width=100, height=23)
Button(window, text="Merge", font=('Courier New',11, "bold"), command=convert_pdf).place(x=480, y=160, width=100, height=23)

window.mainloop()
