import tkinter as tk

# create a window window
window = tk.Tk()
 
# set the background colour of window
window.configure(background="light green")

# set the title of window window
window.title("Calculator")
 
# set the configuration of window window
window.geometry("500x225")
window.resizable(0, 0)


expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        expression = expression.replace('x', '*')
        total = str(eval(expression))
        equation.set(total)
        expression = ""
 
    except:
        equation.set(" ERROR ")
        expression = ""
 

def clear():
    global expression
    expression = ""
    equation.set("")

def pop():
    global expression
    expression = expression[:-1]
    equation.set(expression)


equation = tk.StringVar()
 
expression_field = tk.Entry(window, textvariable=equation, font=('calibre', 20, 'bold'))
 
expression_field.grid(columnspan=5, ipadx=60)
 
button1 = tk.Button(window, text=' 1 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)
 
button2 = tk.Button(window, text=' 2 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
 
button3 = tk.Button(window, text=' 3 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
 
button4 = tk.Button(window, text=' 4 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
 
button5 = tk.Button(window, text=' 5 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
 
button6 = tk.Button(window, text=' 6 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
 
button7 = tk.Button(window, text=' 7 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
 
button8 = tk.Button(window, text=' 8 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
 
button9 = tk.Button(window, text=' 9 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
 
button0 = tk.Button(window, text=' 0 ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=1)
 
plus = tk.Button(window, text=' + ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                command=lambda: press("+"), height=1, width=7)
plus.grid(row=5, column=3)
 
minus = tk.Button(window, text=' - ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                command=lambda: press("-"), height=1, width=7)
minus.grid(row=6, column=0)
 
multiply = tk.Button(window, text=' x ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press("x"), height=1, width=7)
multiply.grid(row=6, column=1)
 
divide = tk.Button(window, text=' / ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press("/"), height=1, width=7)
divide.grid(row=6, column=2)
 
equal = tk.Button(window, text=' = ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                command=equalpress, height=1, width=7)
equal.grid(row=6, column=3)
 
clear = tk.Button(window, text='Clear', fg='black', bg='red',font=('calibre', 14, 'bold'),
                command=clear, height=1, width=7)
clear.grid(row=3, column=3)
 
Decimal= tk.Button(window, text='.', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=4, column=3)

delete = tk.Button(window, text='Del', fg='black', bg='red',font=('calibre', 14, 'bold'),
                    command=lambda: pop(), height=1, width=7)
delete.grid(row=2, column=3)

open_bracket = tk.Button(window, text=' ( ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                command=lambda: press('('), height=1, width=7)
open_bracket.grid(row=5, column=0)

close_bracket = tk.Button(window, text=' ) ', fg='black', bg='red',font=('calibre', 14, 'bold'),
                command=lambda: press(')'), height=1, width=7)
close_bracket.grid(row=5, column=2)

# start the window
window.mainloop()
