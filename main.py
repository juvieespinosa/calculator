from tkinter import *

FONT = ("Courier", 25, "bold")



# ---------------------------- WINDOW SETUP ------------------------------- #

window = Tk()
window.title("Jhuv's Simple Calculator")
window.minsize(width=190, height=200)
window.config(bg="light pink", padx=10, pady=10)



expression = ""
input_text = StringVar()
# ---------------------------- BUTTON CLICK FUNCTIONS ------------------------------- #
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# ----------------------------BUTTON CLEAR FUNCTIONS ------------------------------- #
def button_clear():
    global expression
    expression = ""
    input_text.set("")


# ---------------------------- BUTTON EQUAL FUNCTIONS ------------------------------- #
def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""



# ---------------------------- GUI SETUP ------------------------------- #

# Entry
entry_input = Entry(bg="white", fg="red", highlightthickness=0, font=FONT, textvariable=input_text, justify="right", width=34)
entry_input.grid(column=0, row=0, columnspan=6)

# Number Buttons
zero_button = Button(text="0", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(0))
zero_button.grid(column=1, row=4)

one_button = Button(text="1", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(1))
one_button.grid(column=0, row=3)

two_button = Button(text="2", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(2))
two_button.grid(column=1, row=3)

three_button = Button(text="3", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(3))
three_button.grid(column=2, row=3)

four_button = Button(text="4", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(4))
four_button.grid(column=0, row=2)

five_button = Button(text="5", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(5))
five_button.grid(column=1, row=2)

six_button = Button(text="6", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(6))
six_button.grid(column=2, row=2)

seven_button = Button(text="7", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(7))
seven_button.grid(column=0, row=1)

eight_button = Button(text="8", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(8))
eight_button.grid(column=1, row=1)

nine_button = Button(text="9", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click(9))
nine_button.grid(column=2, row=1)

dot_button = Button(text=".", font=FONT, fg="red", width=5, height=3, highlightthickness=0, command=lambda: button_click("."))
dot_button.grid(column=2, row=4)

clear_button = Button(text="C", font=FONT, fg="green", width=5, height=3, highlightthickness=0, command=button_clear)
clear_button.grid(column=0, row=4)

# Arithmetic Buttons
plus_button = Button(text="+", font=FONT, fg="green", width=5, height=3, highlightthickness=0,
                     command=lambda: button_click("+"))
plus_button.grid(column=3, row=4)

minus_button = Button(text="-", font=FONT, fg="green", width=5, height=3, highlightthickness=0,
                      command=lambda: button_click("-"))
minus_button.grid(column=3, row=3)

multiply_button = Button(text="*", font=FONT, fg="green", width=5, height=3, highlightthickness=0,
                         command=lambda: button_click("*"))
multiply_button.grid(column=3, row=2)

divide_button = Button(text="/", font=FONT, fg="green", width=5, height=3, highlightthickness=0,
                       command=lambda: button_click("/"))
divide_button.grid(column=3, row=1)

equal_button = Button(text="=", font=FONT, fg="green", width=5, height=13, highlightthickness=0,
                      command=button_equal)
equal_button.grid(column=4, row=1, rowspan=4)



window.mainloop()
