import tkinter
import customtkinter

# Modes: system (default), light, dark
# Themes: blue (default), dark-blue, green
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

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
    
    """Create CTk window like you do with the Tk window"""
    root = customtkinter.CTk()  
    root.geometry("300x470")
    root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

    """Title, size, and transparency"""
    root.title("Simple Python Desktop Calculator")
    root.minsize(300, 470)
    root.attributes('-alpha', 1)
    root.configure(background="light blue")

    """Variables For the Gui"""
    equation = tkinter.StringVar()

    """The layout & Looks of the app"""
    """Row 0 contains the input field"""
    expressionField = customtkinter.CTkEntry(root, textvariable=equation)
    expressionField.grid(row=0, columnspan=5, sticky="nsew")

    """Row 1 contains buttons: 1, 2, 3, & Addition"""
    btn1 = customtkinter.CTkButton(root, text='1', command=lambda: click(1))
    btn1.grid(row=1, column=0, sticky="nsew")

    btn2 = customtkinter.CTkButton(root, text='2', command=lambda: click(2))
    btn2.grid(row=1, column=1, sticky="nsew")

    btn3 = customtkinter.CTkButton(root, text='3', command=lambda: click(3))
    btn3.grid(row=1, column=2, sticky="nsew")

    btnAddition = customtkinter.CTkButton(root, fg_color="#AA0000", text='+', command=lambda: click('+'))
    btnAddition.grid(row=1, column=3, columnspan=2, sticky="nsew")

    """Row 2 contains buttons: 4, 5, 6, & Subtraction"""
    btn4 = customtkinter.CTkButton(root, text='4', command=lambda: click(4))
    btn4.grid(row=2, column=0, sticky="nsew")
    
    btn5 = customtkinter.CTkButton(root, text='5', command=lambda: click(5))
    btn5.grid(row=2, column=1, sticky="nsew")
    
    btn6 = customtkinter.CTkButton(root, text='6', command=lambda: click(6))
    btn6.grid(row=2, column=2, sticky="nsew")

    btnSubtration = customtkinter.CTkButton(root, fg_color="#AA0000", text='-', command=lambda: click('-'))
    btnSubtration.grid(row=2, column=3, columnspan=2, sticky="nsew")

    """Row 3 contains buttons: 7, 8, 9, & Multiplication"""
    btn7 = customtkinter.CTkButton(root, text='7', command=lambda: click(7))
    btn7.grid(row=3, column=0, sticky="nsew")

    btn8 = customtkinter.CTkButton(root, text='8', command=lambda: click(8))
    btn8.grid(row=3, column=1, sticky="nsew")

    btn9 = customtkinter.CTkButton(root, text='9', command=lambda: click(9))
    btn9.grid(row=3, column=2, sticky="nsew")

    btnMultiplication = customtkinter.CTkButton(root, fg_color="#AA0000", text='*', command=lambda: click('*'))
    btnMultiplication.grid(row=3, column=3, columnspan=2, sticky="nsew")

    """Row 4 contains buttons: Decimal, 0, Clear, & Division"""
    btnDecimal = customtkinter.CTkButton(root, fg_color="#00AA00", text='.', command=lambda: click('.'))
    btnDecimal.grid(row=4, column=0, sticky="nsew")

    btn0 = customtkinter.CTkButton(root, text='0', command=lambda: click(0))
    btn0.grid(row=4, column=1, sticky="nsew")

    btnEquals = customtkinter.CTkButton(root, fg_color="#00AA00", text='=', command=equals)
    btnEquals.grid(row=4, column=2, sticky="nsew")

    btnDivision = customtkinter.CTkButton(root, fg_color="#AA0000", text='/', command=lambda: click('/'))
    btnDivision.grid(row=4, column=3, columnspan=2, sticky="nsew")

    """Row 5 contains the clear button"""
    btnClear = customtkinter.CTkButton(root, fg_color="#555555", text='Clear', command=clear)
    btnClear.grid(row=5, column=0, columnspan=5, sticky="nsew")

    """Dynamic Grid Buttons"""
    # row configure
    tkinter.Grid.rowconfigure(root, index=0, weight=2)
    tkinter.Grid.rowconfigure(root, index=1, weight=4)
    tkinter.Grid.rowconfigure(root, index=2, weight=4)
    tkinter.Grid.rowconfigure(root, index=3, weight=4)
    tkinter.Grid.rowconfigure(root, index=4, weight=4)
    tkinter.Grid.rowconfigure(root, index=5, weight=4)

    # column configure
    tkinter.Grid.columnconfigure(root, index=0, weight=1)
    tkinter.Grid.columnconfigure(root, index=1, weight=1)
    tkinter.Grid.columnconfigure(root, index=2, weight=1)
    tkinter.Grid.columnconfigure(root, index=3, weight=1)
    tkinter.Grid.columnconfigure(root, index=4, weight=1)
    tkinter.Grid.columnconfigure(root, index=5, weight=1)

    root.mainloop()
