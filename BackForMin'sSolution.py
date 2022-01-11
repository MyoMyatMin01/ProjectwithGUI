from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class CalculateforProject():

    def click_button(self, input_numbers):
        global number
        number = number + str(input_numbers)
        calculation_input.set(number)


    def clear(self):
        global number
        number = ""
        calculation_input.set("")

    def get_ans(self):
        ans = eval(calculation_input.get())
        calculation_input.set(ans)


win = Tk()

win.title("Min's Solution")

frame = Frame(win)
frame.grid()

number = ""

C = CalculateforProject()

#------------------------------------------------------------------------------------------------

open_image1 = Image.open('C:/Users/ACER/Pictures/Camera Roll/repixel_for_download_22.jpg')
convert_image1 = ImageTk.PhotoImage(open_image1)

background_picture_for_label1 = Label(frame, image=convert_image1)
background_picture_for_label1.place(relx=0, rely=0, relwidth=1, relheight=1)

#----------------------------------------------------------------------------------------------

# label_for_inputting_calculation = Label(frame, text="Calculate Here", font=("arial", 12, "normal"), bg='#ffb3ff', fg='black')
# label_for_inputting_calculation.grid(row=0, column=1)

#---------------------------------------------------------------------------------------------------------

# combo_for_unknown_number = ttk.Combobox(frame, width=20, font=("arial", 15, "normal"))
# combo_for_unknown_number["values"] = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I'
#             , 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'N', 'n', 'M', 'm', 'O', 'o', 'P', 'p', 'Q'
#             , 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y'
#             , 'y', 'Z', 'z')
# combo_for_unknown_number.grid(row=1, column=2)

#---------------------------------------------------------------------------------------------------------

calculation_input = StringVar()
assign_input = StringVar()

user_input_for_calculation = Entry(frame, bd=25, width=20, font=("arial", 18, "normal"), textvariable=calculation_input, bg="black", fg='yellow', justify="right")
user_input_for_calculation.grid(row=1, column=1)

ans_button = Button(frame, text="Get Answer!", bd=5, width=15, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.get_ans())
ans_button.grid(row=1, column=0)

#-------------------------------------------------------------------------------------------------

clear_button = Button(frame, text="C", bd=5, width=20, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.clear())
clear_button.grid(row=1, column=2)

#--------------------------------------------------------------------------------------------------

status_bar = Label(frame, text="Min's Solution", anchor='e', font=("arial", 15, "normal"), bg='black', fg='yellow')
status_bar.grid(row=7, column=2)

#---------------------------------------------------------------------------------------------------

button_for_1 = Button(frame, text="1", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(1))
button_for_1.grid(row=2, column=0)

button_for_2 = Button(frame, text="2", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(2))
button_for_2.grid(row=2, column=1)

button_for_3 = Button(frame, text="3", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(3))
button_for_3.grid(row=2, column=2)

button_for_4 = Button(frame, text="4", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(4))
button_for_4.grid(row=3, column=0)

button_for_5 = Button(frame, text="5", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(5))
button_for_5.grid(row=3, column=1)

button_for_6 = Button(frame, text="6", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(6))
button_for_6.grid(row=3, column=2)

button_for_7 = Button(frame, text="7", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(7))
button_for_7.grid(row=4, column=0)

button_for_8 = Button(frame, text="8", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(8))
button_for_8.grid(row=4, column=1)

button_for_9 = Button(frame, text="9", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(9))
button_for_9.grid(row=4, column=2)

button_for_0 = Button(frame, text="0", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button(0))
button_for_0.grid(row=5, column=0)

#---------------------------------------------------------------------------------------------

button_for_divided = Button(frame, text="/", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button('/'))
button_for_divided.grid(row=5, column=1)

button_for_multiply = Button(frame, text="*", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button('*'))
button_for_multiply.grid(row=5, column=2)

button_for_minus = Button(frame, text="-", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button('-'))
button_for_minus.grid(row=6, column=0)

button_for_plus = Button(frame, text="+", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button('+'))
button_for_plus.grid(row=6, column=1)

button_for_percent = Button(frame, text="%", bd=5, width=10, font=("arial", 10, "normal"), bg='black', fg='yellow', command=lambda: C.click_button('%'))
button_for_percent.grid(row=6, column=2)


win.mainloop()