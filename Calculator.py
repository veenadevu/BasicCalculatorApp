# Simple Calculator
# Python 3.9
# Topics: tkinder, grid geometry manager, evel, try/except, lambda

import tkinter

root = tkinter.Tk()
root.title("Calculator")

expression = ""
#Create functions
def add(value):
    global expression
    expression += value
    myLabel_result.config(text=expression)

def clear():
    global expression
    expression = ""
    myLabel_result.config(text=expression)

def calc():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    myLabel_result.config(text=result)

#Create GUI for layout
myLabel_result = tkinter.Label(root, text ="")
myLabel_result.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(root, text="1", width=3, command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", width=3, command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3", width=3, command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_addition = tkinter.Button(root, text="+", width=3, bg="orange", fg="darkgreen", font=("Impact",10), command=lambda: add("+"))
button_addition.grid(row=1, column=3)

button_4 = tkinter.Button(root, text="4", width=3, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", width=3, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", width=3, command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_sub = tkinter.Button(root, text="-", width=3, bg="orange", fg="darkgreen", font=("Impact",10), command=lambda: add("-"))
button_sub.grid(row=2, column=3)

button_7 = tkinter.Button(root, text="7", width=3, command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="8", width=3, command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="9", width=3, command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_mult = tkinter.Button(root, text="*", width=3, bg="orange", fg="darkgreen", font=("Impact",10), command=lambda: add("*"))
button_mult.grid(row=3, column=3)

button_0 = tkinter.Button(root, text="0", width=3, command=lambda: add("0"))
button_0.grid(row=4, column=0)

button_clear = tkinter.Button(root, text="C", width=3, bg="lightgrey", fg="red", activebackground="white", font=("Impact",10), command=lambda: clear())
button_clear.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".", width=3, bg="orange", fg="darkgreen", font=("Impact",10), command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_division = tkinter.Button(root, text="/", width=3, bg="orange", fg="darkgreen", font=("Impact",10), command=lambda: add("/"))
button_division.grid(row=4, column=3)

button_equals = tkinter.Button(root, text="=", width=16, bg="white", fg="black", command=lambda: calc())
button_equals.grid(row=5, column=0, columnspan=4)


root.mainloop()
