# Import the tkinter library to create the GUI
from tkinter import *

# Function to handle button clicks
def button_click(number):
    current_text = input_field.get()  # Get the current text from the input field
    input_field.delete(0, END)  # Clear the input field
    if current_text == "Error":
        current_text = ""  # Clear the "Error" message
    input_field.insert(0, current_text + str(number))  # Append the clicked number or operator

# Function to clear the input field
def clear():
    input_field.delete(0, END)  # Clear the input field

# Function to calculate the result
def calculate():
    try:
        expression = input_field.get()  # Get the expression from the input field
        if expression:
            result = str(eval(expression))  # Evaluate the expression
            input_field.delete(0, END)  # Clear the input field
            input_field.insert(0, result)  # Display the result
    except Exception as e:
        input_field.delete(0, END)  # Clear the input field
        input_field.insert(0, "Error")  # Display an error message

# Create the main application window
win = Tk()

# Set the title of the window
win.title('Calculator')

# Set the initial size of the window to 350x450 pixels
win.geometry('350x450')

# Disable the ability to resize the window
win.resizable(0, 0)

# Create an input field for displaying and entering the calculation expression
input_field = Entry(win, font=('arial', 20, 'bold'))

# Pack the input field in the window, fill it horizontally, and add padding
input_field.pack(fill=X, ipadx=8, pady=10, padx=10)

# Create a frame for the calculator buttons
button_frame = Frame(win)

# Pack the button frame in the window
button_frame.pack()

# Define a list of button labels for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Define the grid layout for button placement
grid_layout = [
    (1, 0), (1, 1), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 2), (2, 3),
    (3, 0), (3, 1), (3, 2), (3, 3),
    (4, 0), (4, 1), (4, 2), (4, 3),
    (5, 0), (5, 1)
]

# Create and place buttons in the calculator interface
for i in range(len(buttons)):
    button_text = buttons[i]
    row, col = grid_layout[i]

    if button_text == 'C':
        # Handle the 'C' button separately to call the clear function
        Button(button_frame, text=button_text, font=('arial', 18, 'bold'), width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        # For other buttons, use the lambda function
        Button(button_frame, text=button_text, font=('arial', 18, 'bold'), width=5, height=2,
               command=lambda text=button_text: button_click(text) if text != '=' else calculate()).grid(row=row, column=col)

# Start the main event loop to run the calculator application
win.mainloop()
