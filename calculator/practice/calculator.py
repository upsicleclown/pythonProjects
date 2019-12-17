from tkinter import *
import math

root = Tk()
root.title("karatsuba")

x = 0
y = 0
op = "add"


e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)


def number_click(n):
    global y 

    y = e.get()  + str(n)
    e.delete(0, END)
    e.insert(0, y)

def calc():
    global x
    global y

    if op == "add":
        x += y
    elif op == "mult":
        x*=y 
    elif op == "sub":
        x -= y
    elif op == "div":
        x/=y
    else:
        print("invalid")

def changeOp(newOp):
    global y
    global op 

    y = int(y)
    calc()
    op = newOp

    e.delete(0, END)

def eq_click():
    global y
    global x
    global op

    y = int(y)
    calc()

    y = 0
    op = "add"
    
    e.delete(0, END)
    e.insert(0, x)


def clear_click():
    global x 
    global y 
    global op 

    y = 0
    x = 0
    op = "add"

    e.delete(0, END)



buttons = []
for i in range(10):
    #anumber_click = partial(number_click, i)
    buttons.append(Button(root, text = i, height= 5, width = 10, command= lambda x = i: number_click(x)))
    buttons[i].grid(column  = (i % 3), padx = 5, pady = 5, row = 1 + math.floor(i/3))

addButt = Button(root, text = "+", height= 5, width = 10, command = lambda x = "add": changeOp(x), padx = 5)
subButt = Button(root, text = "-", height= 5, width = 10, command = lambda x = "sub": changeOp(x), padx = 5)
multButt = Button(root, text = "x", height= 5, width = 10, command = lambda x = "mult": changeOp(x), padx = 5)
divButt = Button(root, text = "/", height= 5, width = 10, command = lambda x = "div": changeOp(x), padx = 5)
eqButt = Button(root, text = "=", height= 5, width = 10, command = eq_click, padx = 5)
clearButt = Button(root, text = "C", height= 5, width = 10, command = clear_click, padx = 5)

addButt.grid(column = 3, row = 1)
subButt.grid(column = 3, row = 2)
multButt.grid(column = 3, row = 3)
divButt.grid(column = 3, row = 4)
eqButt.grid(column = 1, row = 4)
clearButt.grid(column = 2, row = 4)


root.mainloop()