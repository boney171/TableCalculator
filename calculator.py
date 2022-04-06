from tkinter import *

"""Practice user interface with tkinter in python"""

#Structure of tkinter


calculator = Tk()  #call tkinter, required
calculator.title("Tri's Calculator")  # title of the program
#function

#this function take care of numbers being input into the entry
def button_click(number):
    """When the user enter numbers, everytime they enter a new number, this function clear out the entry box, get user input and add into the back of the previous number 3-> 35 -> 350
     User enter 3 then 5 then 0 """
    number1 =  0 
    number1 = output.get() + number
    output.delete(0, END)
    output.insert(0, number1)

#this function take care of the operations buttons being input: + - * /
#store whatever in the entry box into the first global variable
#store which operation button were chosen
#clear out the entry box
def button_operation(operation):
    global firstNum
    global math
    math = operation
    firstNum = output.get()
    output.delete(0, END)

def button_eq():
    secondNum = output.get()
    output.delete(0, END)
    
    if math == "+":
         output.insert(0, int(firstNum)+int(secondNum))
    elif math == "-":
         output.insert(0, int(firstNum)-int(secondNum))
    elif math == "*":
         output.insert(0, float(firstNum)*float(secondNum))
    elif math == "/":
         output.insert(0, float(firstNum)/float(secondNum))

def button_clear():
    output.delete(0, END)

#define stuff

output = Entry(calculator, width = 70, borderwidth=5, bg = "#E4EDEA")
button7 = Button(calculator, text = "7", width = 20, bg = "#BFC7C4", fg = "black", command = lambda : button_click("7"))
button8 = Button(calculator, text = "8", width = 20, bg = "#BFC7C4", fg = "black", command = lambda : button_click("8"))
button9 = Button(calculator, text = "9", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_click("9"))
button4 = Button(calculator, text = "4", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_click("4"))
button5 = Button(calculator, text = "5", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_click("5"))
button6 = Button(calculator, text = "6", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_click("6"))
button1 = Button(calculator, text = "1", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_click("1"))
button2 = Button(calculator, text = "2", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_click("2"))
button3 = Button(calculator, text = "3", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_click("3"))
button0 = Button(calculator, text = "0", width = 20, bg = "#BFC7C4", fg = "black", command = lambda : button_click("0"))
buttonplus = Button(calculator, text = "+", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_operation("+"))
buttonminus = Button(calculator, text = "-", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_operation("-"))
buttonmultiply = Button(calculator, text = "*", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_operation("*"))
buttondivide = Button(calculator, text = "/", width = 20,  bg = "#BFC7C4", fg = "black", command = lambda : button_operation("/"))
buttoneq = Button(calculator, text = "=", width = 20,  bg = "#BFC7C4", fg = "black", command =  button_eq)
buttonclear = Button(calculator, text = "Clear", width = 63,  bg = "#BFC7C4", fg = "black", command =  button_clear)

#Put on the screen
output.grid(row = 0, column = 0, columnspan = 3, padx=10 , pady = 10 )
button7.grid(row = 1, column = 0, padx=1 , pady = 1)
button8.grid(row=1, column = 1, padx=1 , pady = 1)
button9.grid(row = 1, column = 2, padx=1 , pady = 1)

button4.grid(row = 2, column = 0, padx=1 , pady = 1)
button5.grid(row=2, column = 1, padx=1 , pady = 1)
button6.grid(row = 2, column = 2, padx=1 , pady = 1)

button1.grid(row = 3, column = 0, padx=1 , pady = 1)
button2.grid(row=3, column = 1, padx=1 , pady = 1)
button3.grid(row = 3, column = 2, padx=1, pady = 1)

buttonplus.grid(row = 4, column = 1, padx=1 , pady = 1)
button0.grid(row = 4, column = 0, padx=1 , pady =1 )
buttonminus.grid(row = 4, column = 2, padx=1 , pady = 1 )
buttoneq.grid(row = 5, column = 2, padx=1 , pady = 1 )
buttonmultiply.grid(row = 5, column = 0, padx=1 , pady = 1 )
buttondivide.grid(row = 5, column = 1, padx=1 , pady = 1 )
buttonclear.grid(row =6, column = 0 , columnspan = 3, padx=1 , pady = 1 )

#GUI means there is a loop that keeps going
calculator.mainloop()
