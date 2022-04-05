from tkinter import *

calculator = Tk()
calculator.title("Tri's Calculator")
#function
def button_click7():
    return

#define stuff
output = Entry(calculator, width = 70, borderwidth=5, bg = "gray")
button7 = Button(calculator, text = "7", width = 20, bg = "gray", fg = "black", command = button_click7)
button8 = Button(calculator, text = "8", width = 20, bg = "gray", fg = "black", command = button_click7)
button9 = Button(calculator, text = "9", width = 20,  bg = "gray", fg = "black", command = button_click7)
button4 = Button(calculator, text = "4", width = 20,  bg = "gray", fg = "black", command = button_click7)
button5 = Button(calculator, text = "5", width = 20,  bg = "gray", fg = "black", command = button_click7)
button6 = Button(calculator, text = "6", width = 20,  bg = "gray", fg = "black", command = button_click7)
button1 = Button(calculator, text = "1", width = 20,  bg = "gray", fg = "black", command = button_click7)
button2 = Button(calculator, text = "2", width = 20,  bg = "gray", fg = "black", command = button_click7)
button3 = Button(calculator, text = "3", width = 20,  bg = "gray", fg = "black", command = button_click7)
button0 = Button(calculator, text = "0", width = 20, bg = "gray", fg = "black", command = button_click7)
buttonplus = Button(calculator, text = "+", width = 20,  bg = "gray", fg = "black", command = button_click7)
buttoneq = Button(calculator, text = "=", width = 20,  bg = "gray", fg = "black", command = button_click7)
buttonclear = Button(calculator, text = "Clear", width = 63,  bg = "gray", fg = "black", command = button_click7)
#Put on the screen
output.grid(row = 0, column = 0, columnspan = 3, padx=5 , pady = 5 )
button7.grid(row = 1, column = 0)
button8.grid(row=1, column = 1)
button9.grid(row = 1, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row=2, column = 1)
button6.grid(row = 2, column = 2)

button1.grid(row = 3, column = 0)
button2.grid(row=3, column = 1)
button3.grid(row = 3, column = 2)

buttonplus.grid(row = 4, column = 1)
button0.grid(row = 4, column = 0 )
buttoneq.grid(row = 4, column = 2 )
buttonclear.grid(row =5, column = 0 , columnspan = 3 )
#GUI means there is a loop that keeps going
calculator.mainloop()
