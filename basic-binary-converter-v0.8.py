
#!/usr/bin/python3

##########################################################
# basic-binary-converter-v0.8.py - September 2024 - SRR  #
# For converting between binary and decimal numbers      #
##########################################################

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#--| GUI |--#

# main window
window = ttk.Window(themename = "sandstone")
window.title("Basic Binary Converter - 0.8")
window.resizable(False, False)

# main window size
window_width = 345
window_height = 500

# getting screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# finding center of screen
screen_center_x = int(screen_width / 2 - window_width / 2)
screen_center_y = int(screen_height / 2 - window_height / 2)

# placing window in center of screen
window.geometry(f'{window_width}x{window_height}+{screen_center_x}+{screen_center_y}')

# grouping of conversion widgets in frame
conversion_grouping = ttk.LabelFrame(window, text = "Conversion:")
conversion_grouping.place(x = 55, y = 50)

# tkinter string variable for holding radiobutton choice
conversion_choice = tk.StringVar(conversion_grouping, " ")

# radiobuttons for conversion choice
r1 = ttk.Radiobutton(conversion_grouping, text = "Binary to Decimal", value = '1')
r1.pack(fill = 'x', padx = 25, pady = 20)
r2 = ttk.Radiobutton(conversion_grouping, text = "Decimal to Binary", value = '0')
r2.pack(fill = 'x', padx = 25, pady = 20)

# label for input widget
entry_field_label = ttk.Label(conversion_grouping, text = "Enter digits for conversion:")
entry_field_label.pack(fill = 'x', padx = 25)

# tkinter string variable for holding user input
user_input = tk.StringVar()

# entry widget for user input
entry_field = ttk.Entry(conversion_grouping, textvariable = user_input, justify = CENTER)
entry_field.pack(fill = 'x', padx = 25, pady = 12)
entry_field.configure(state = "disabled")

# frame widget for output label
output_label = ttk.LabelFrame(window, text = "Instructions:")
output_label.place(x = 55, y = 290)

# label for conversion output to user
output_label = ttk.Label(output_label, text = "First choose conversion\nthen input corresponding\ndigits in the text box", width = 24)
output_label.config(anchor = CENTER)
output_label.pack(fill = 'x', padx = 17, pady = 20)

# button for conversion of input
convert = ttk.Button(window, text = "Convert", bootstyle="dark")
convert.place(x = 57, y = 420, width = 90, height = 40)
convert.configure(state = "disabled")

# button for closing application
close = ttk.Button(window, text = "Close", bootstyle="secondary", command = window.destroy)
close.place(x = 210, y = 420, width = 90, height = 40)

# TODO: alter configuration when no radiobutton is choosen or wrong input
#output_label.config(text = "oooopppps", bootstyle = "danger")


window.mainloop()

#-| Sample code for conversion function |-#
# # Binary to decimal conversion
# binary_number = input("Input a binary number: ")
# decimal_number = 0
#
# for digit in binary_number:
#     # Left shift in binary means x 2
#     decimal_number = decimal_number * 2 + int(digit)
#
# print("Your decimal number is: " + str(decimal_number))
#
# # Decimal to binary conversion
# decimal_number = int(input("Input a decimal number: "))
# binary_number = ""
#
# while decimal_number > 0:
#     # A left shift in binary means / 2
#     binary_number = str(decimal_number % 2) + binary_number
#     decimal_number = decimal_number // 2
# print("Your binary number is: " + binary_number)
