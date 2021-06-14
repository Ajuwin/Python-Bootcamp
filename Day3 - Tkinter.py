#importing library
from tkinter import *
from tkinter import ttk

#var = IntVar()
window = Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('500x500')

#below four fields are declared
label0 = Label(window,text = "REGISTRATION FORM", width=25,font=('Cooper Std Black',20,"bold")).place(x=2, y=20)
Firstname = Label(window ,text = "First Name", width=15,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=20, y=80)
LastName = Label(window ,text = "Last Name", width=15,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=19, y=115)
Gender = Label(window, text= "Gender", width=15,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=4, y=150)
Country = Label(window, text="Country", width=15,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=8, y=185)
State = Label(window ,text = "State", width=14,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=2, y=220)
Programing_Language = Label(window ,text = "Programing Language", width=20,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=39, y=255)
Email = Label(window ,text = "Email Id", width=15,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=8, y=350)
Mobile = Label(window ,text = "Contact Number", width=15,font=('Bahnschrift Light SemiCondensed',15,"bold")).place(x=41, y=385)


Firstname1 = Entry(window,font=('Times New Roman',15)).place(x=270, y=80, width=155, height=22)
Lastname1 = Entry(window,font=('Times New Roman',15)).place(x=270, y=115, width=155, height=22)

vari1=IntVar()
Radiobutton(window,text="Male",width=2,padx= 25,variable=vari1,value=1,font=('Times New Roman',13,"bold")).place(x=250, y=150)
Radiobutton(window,text="Female",width=3,padx= 25,variable=vari1,value=2,font=('Times New Roman',13,"bold")).place(x=330,y=150)

vari2 = IntVar()
Radiobutton(window,text="India",width=3,padx= 25,variable=vari2,value=1,font=('Times New Roman',13,"bold")).place(x=245,y=185)

var1=StringVar()
list1 = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chattisgarh','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttrakhand','West Bengal']
droplist=OptionMenu(window,var1,*list1)
var1.set('select your state')
droplist.config(font=('Times New Roman',10,"bold")) 
droplist.place(x=268, y=215, width=155)

Cvar = IntVar()
Jvar = IntVar()
Jsvar = IntVar()
Pyvar = IntVar()
C = Checkbutton(window, text="C", variable=Cvar,onvalue = 1, offvalue = 0, font=('Times New Roman',13,"bold")).place(x=265, y=262, width=50, height=20)
Jvar = Checkbutton(window, text="Java", variable=Jvar,onvalue = 1, offvalue = 0, font=('Times New Roman',13,"bold")).place(x=272, y=283, width=55, height=20)
Jsvar = Checkbutton(window, text="Java Script", variable=Jsvar,onvalue = 1, offvalue = 0, font=('Times New Roman',13,"bold")).place(x=270, y=302, width=110, height=20)
Pyvar = Checkbutton(window, text="Python", variable=Pyvar,onvalue = 1, offvalue = 0, font=('Times New Roman',13,"bold")).place(x=233, y=324, width=155, height=20)


Email1 = Entry(window,font=('Times New Roman',15)).place(x=270, y=350, width=155, height=22)

num = StringVar()
Mobile1 = Entry(window, textvariable=num)
num.set("+91 ")
Mobile1.config(font=('Times New Roman',15, "bold"))
Mobile1.place(x=270, y=385, width=155, height=22)

# Submit button
btn = ttk.Button(window ,text="Submit").place(x=300, y=425, width=100, height=40)


window.mainloop()


