from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class CalculateforProject():

    # def stringvarnames(self):
    #     self.calculation_input = StringVar()
    #     self.assign_input = StringVar()

    def clear(self):
        calculation_input.set("")
        assign_input.set("")


    def equal(self):

        AtoZ_atoz = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I'
            , 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'N', 'n', 'M', 'm', 'O', 'o', 'P', 'p', 'Q'
            , 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y'
            , 'y', 'Z', 'z']

        for character in AtoZ_atoz:

            if character == assign_input.get()[0]:
                assign_ans_in_assign_input = int(assign_input.get()[2:])

                for character_in_calculation_input in calculation_input.get():
                    if character_in_calculation_input == assign_input.get()[0]:
                        character = str(assign_ans_in_assign_input)

                        # ans_character_in_calculation_input = eval(str(calculation_input.get()) == )
                        # final_ans = eval(str(calculation_input.get()))
                        # calculation_input.set(eval(final_ans + eval(assign_ans_in_calculation_input)))
                        calculation_input.get()[0] = str(character)
                        calculation_input.set(eval(calculation_input.get()))



        # calculation_input.set(eval(calculation_input.get()))

win = Tk()

win.title("Min's Solution")

frame = Frame(win)
frame.grid()

C = CalculateforProject()

#------------------------------------------------------------------------------------------------

open_image1 = Image.open('C:/Users/ACER/Pictures/Camera Roll/download_18.jpg')
convert_image1 = ImageTk.PhotoImage(open_image1)

background_picture_for_label1 = Label(frame, image=convert_image1)
background_picture_for_label1.place(relx=0, rely=0, relwidth=1, relheight=1)

#----------------------------------------------------------------------------------------------

label_for_inputting_calculation = Label(frame, text="Calculate Here", font=("arial", 12, "normal"), bg='#ffb3ff', fg='black')
label_for_inputting_calculation.grid(row=0, column=0)

label_for_inputting_unkown_number = Label(frame, text="Assign unknown number(s)", font=("arial", 12, "normal"), bg='#ffb3ff', fg='black')
label_for_inputting_unkown_number.grid(row=0, column=2)

#---------------------------------------------------------------------------------------------------------

calculation_input = StringVar()
assign_input = StringVar()

user_input_for_calculation = Entry(frame, bd=5, width=20, font=("arial", 13, "normal"), textvariable=calculation_input)
user_input_for_calculation.grid(row=1, column=0)

user_input_for_assigning = Entry(frame, text="Assign unknown number", bd=5, width=20, font=("arial", 13, "normal"), textvariable=assign_input)
user_input_for_assigning.grid(row=1, column=2)

ans_button = Button(frame, text="Get Answer!", bd=5, width=10, font=("arial", 10, "normal"), bg='#5cd6d6', fg='#000099', command=lambda: C.equal())
ans_button.grid(row=1, column=1)

clear_button = Button(frame, text="C", bd=5, width=20, font=("arial", 10, "normal"), bg='#5cd6d6', fg='#000099', command=lambda: C.clear())
clear_button.grid(row=2, column=0)

#--------------------------------------------------------------------------------------------------

status_bar = Label(frame, text="Min's Solution", anchor='e', font=("arial", 15, "bold"))
status_bar.grid(row=2, column=2)

win.mainloop()