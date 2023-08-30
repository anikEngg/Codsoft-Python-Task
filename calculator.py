from tkinter import *

# Constants
THEME_COLOR = "#FFF6DC"
FONT_NAME = "Courier"


# Function to handle button press for expression values
def press(x):
    input_entry.insert(END, str(x))


def clear():
    input_entry.delete(0, END)


def evaluate():
    try:
        input_expression = input_entry.get()
        output = eval(input_expression)
        input_entry.delete(0, END)
        input_entry.insert(0, f"{output:.2f}")
    except (SyntaxError, ZeroDivisionError):
        input_entry.delete(0, END)
        input_entry.insert(0, "BAD EXPRESSION")


# Function to handle "Enter" key press event
def evaluate_on_enter(event):
    evaluate()


window = Tk()

# Entry field for input
input_entry = Entry(font=(FONT_NAME, 25))
input_entry.focus_set()
input_entry.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

# Buttons for numbers
b0 = Button(text="0", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(0))
b0.grid(row=4, column=0, pady=15)

b1 = Button(text="1", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(1))
b1.grid(row=3, column=0, pady=15)

b2 = Button(text="2", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(2))
b2.grid(row=3, column=1, pady=15)

b3 = Button(text="3", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(3))
b3.grid(row=3, column=2, pady=15)

b4 = Button(text="4", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(4))
b4.grid(row=2, column=0, pady=15)

b5 = Button(text="5", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(5))
b5.grid(row=2, column=1, pady=15)

b6 = Button(text="6", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(6))
b6.grid(row=2, column=2, pady=15)

b7 = Button(text="7", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(7))
b7.grid(row=1, column=0, pady=15)

b8 = Button(text="8", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(8))
b8.grid(row=1, column=1, pady=15)

b9 = Button(text="9", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(9))
b9.grid(row=1, column=2, pady=15)

# Buttons for different functions
clear_btn = Button(text="CLEAR", height=1, width=18, font=(FONT_NAME, 25), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=15)

divide = Button(text="/", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("/"))
divide.grid(row=1, column=3)

multiply = Button(text="*", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("*"))
multiply.grid(row=2, column=3)

addition = Button(text="+", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("+"))
addition.grid(row=3, column=3)

subtract = Button(text="-", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("-"))
subtract.grid(row=4, column=3)

equal = Button(text="=", height=1, width=2, font=(FONT_NAME, 25), command=evaluate)
equal.grid(row=4, column=2)

point = Button(text=".", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("."))
point.grid(row=4, column=1)

# Event listener for "Enter" key to evaluate expression in input field
window.bind("<Return>", evaluate_on_enter)

# Window configuration
window.title("Calculator")
window.config(padx=20, pady=20, bg=THEME_COLOR)
window.geometry("+575+125")
window.minsize(width=325, height=500)
window.resizable(False, False)
window.mainloop()
