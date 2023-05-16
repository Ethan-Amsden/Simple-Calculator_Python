# importing tkinter and ttk
import tkinter as tk
from tkinter import * 
from tkinter import ttk

expression = ""

def click(num):
    
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equals():

    global expression

    try:

        total = str(eval(expression))
        equation.set(total)
        expression = total

    except:

        equation.set(" error ")
        expression = ""

def clear():
    
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    
    """Start up the app"""
    root = Tk()
    root.geometry("300x470")
    root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

    """Title, size, and transparency"""
    root.title("Simple Python Desktop Calculator")
    root.minsize(300, 470)
    root.attributes('-alpha', 1)
    root.configure(background="light blue")

    """Variables For the Gui"""
    equation = StringVar()

    """The layout & Looks of the app"""
    """Row 0 contains the input field"""
    expressionField = Entry(root, textvariable=equation)
    expressionField.grid(row=0, columnspan=5, sticky="nsew")

    """Row 1 contains buttons: 1, 2, 3, & Addition"""
    btn1 = Button(root, background='black', foreground='white',  text='1', command=lambda: click(1))
    btn1.grid(row=1, column=0, sticky="nsew")

    btn2 = Button(root, background='black', foreground='white',  text='2', command=lambda: click(2))
    btn2.grid(row=1, column=1, sticky="nsew")

    btn3 = Button(root, background='black', foreground='white',  text='3', command=lambda: click(3))
    btn3.grid(row=1, column=2, sticky="nsew")

    btnAddition = Button(root, background='black', foreground='white',  text='+', command=lambda: click('+'))
    btnAddition.grid(row=1, column=3, columnspan=2, sticky="nsew")

    """Row 2 contains buttons: 4, 5, 6, & Subtraction"""
    btn4 = Button(root, background='black', foreground='white',  text='4', command=lambda: click(4))
    btn4.grid(row=2, column=0, sticky="nsew")
    
    btn5 = Button(root, background='black', foreground='white',  text='5', command=lambda: click(5))
    btn5.grid(row=2, column=1, sticky="nsew")
    
    btn6 = Button(root, background='black', foreground='white',  text='6', command=lambda: click(6))
    btn6.grid(row=2, column=2, sticky="nsew")

    btnSubtration = Button(root, background='black', foreground='white',  text='-', command=lambda: click('-'))
    btnSubtration.grid(row=2, column=3, columnspan=2, sticky="nsew")

    """Row 3 contains buttons: 7, 8, 9, & Multiplication"""
    btn7 = Button(root, background='black', foreground='white',  text='7', command=lambda: click(7))
    btn7.grid(row=3, column=0, sticky="nsew")

    btn8 = Button(root, background='black', foreground='white',  text='8', command=lambda: click(8))
    btn8.grid(row=3, column=1, sticky="nsew")

    btn9 = Button(root, background='black', foreground='white',  text='9', command=lambda: click(9))
    btn9.grid(row=3, column=2, sticky="nsew")

    btnMultiplication = Button(root, background='black', foreground='white',  text='*', command=lambda: click('*'))
    btnMultiplication.grid(row=3, column=3, columnspan=2, sticky="nsew")

    """Row 4 contains buttons: Decimal, 0, Clear, & Division"""
    btnDecimal = Button(root, background='black', foreground='white',  text='.', command=lambda: click('.'))
    btnDecimal.grid(row=4, column=0, sticky="nsew")

    btn0 = Button(root, background='black', foreground='white',  text='0', command=lambda: click(0))
    btn0.grid(row=4, column=1, sticky="nsew")

    btnEquals = Button(root, background='black', foreground='white',  text='=', command=equals)
    btnEquals.grid(row=4, column=2, sticky="nsew")

    btnDivision = Button(root, background='black', foreground='white',  text='/', command=lambda: click('/'))
    btnDivision.grid(row=4, column=3, columnspan=2, sticky="nsew")

    """Row 5 contains the clear button"""
    btnClear = Button(root, background='black', foreground='white',  text='Clear', command=clear)
    btnClear.grid(row=5, column=0, columnspan=5, sticky="nsew")

    """Dynamic Grid Buttons"""
    # row configure
    Grid.rowconfigure(root, index=0, weight=2)
    Grid.rowconfigure(root, index=1, weight=4)
    Grid.rowconfigure(root, index=2, weight=4)
    Grid.rowconfigure(root, index=3, weight=4)
    Grid.rowconfigure(root, index=4, weight=4)
    Grid.rowconfigure(root, index=5, weight=4)

    # column configure
    Grid.columnconfigure(root, index=0, weight=1)
    Grid.columnconfigure(root, index=1, weight=1)
    Grid.columnconfigure(root, index=2, weight=1)
    Grid.columnconfigure(root, index=3, weight=1)
    Grid.columnconfigure(root, index=4, weight=1)
    Grid.columnconfigure(root, index=5, weight=1)

    root.mainloop()
    
