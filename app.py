from tkinter import *

import math

root = Tk()

# Give the app window a name
root.title("Calculator")

# set text box
e = Entry(root, width=60, borderwidth=10)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# create button functions
def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def buttonCls():
    e.delete(0, END)


def buttonAdd():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)


def buttonSub():
    first_num = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_num)
    e.delete(0, END)


def buttonDiv():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)


def buttonMulti():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)


def button_sin():
    f_num = int(e.get())
    e.insert(0, math.sin(f_num))


def button_cos():
    f_num = int(e.get())
    e.insert(0, math.cos(f_num))


def button_tan():
    f_num = int(e.get())
    e.insert(0, math.tan(f_num))


def button_sqrt():
    f_num = int(e.get())
    e.insert(0, math.sqrt(f_num))


def buttonEquals():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "substraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num // int(second_number))
    else:
        pass


# create buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: buttonAdd())
button_sub = Button(root, text="-", padx=40, pady=20, command=lambda: buttonSub())
button_div = Button(root, text="-", padx=40, pady=20, command=lambda: buttonDiv())
button_multi = Button(root, text="*", padx=40, pady=20, command=lambda: buttonMulti())
button_cls = Button(root, text="cls", padx=40, pady=20, command=lambda: buttonCls())
button_equals = Button(root, text="=", padx=40, pady=20, command=lambda: buttonEquals())
button_sine = Button(root, text="sin", padx=40, pady=20, command=lambda: button_sin())
button_cosine = Button(root, text="cos", padx=40, pady=20, command=lambda: button_cos())
button_tangent = Button(
    root, text="tan", padx=40, pady=20, command=lambda: button_tan()
)
button_square_root = Button(
    root, text="sqrt", padx=40, pady=20, command=lambda: button_sqrt()
)

# put the buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_cls.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_div.grid(row=3, column=3)
button_multi.grid(row=4, column=3)
button_sine.grid(row=1, column=4)
button_cosine.grid(row=2, column=4)
button_tangent.grid(row=3, column=4)
button_square_root.grid(row=4, column=4)

# close the connection
root.mainloop()
