import tkinter

button_value = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]   
]

row_count = len(button_value)
column_count = len(button_value[0])

upper_symbols = ["AC", "+/-", "%", "√"]
right_symbols = ["÷", "×", "-", "+", "="]

light_gray_color = "#D4D4D2"
black_color = "#1C1C1C"
dark_gray_color = "#505050"
orange_color = "#FF9500"
white = "white"

window = tkinter.Tk()
window.title("calculator")
window.resizable(False,False)

frame = tkinter.Frame(window)

label = tkinter.Label(frame, text= "0", font= ("Arial", 45), background= black_color, foreground= white,
                    anchor= "e", width= column_count)

label.grid(row=0, column=0, columnspan=column_count,  sticky= "we")

for row in range(row_count):
    for column in range(column_count):
        value = button_value[row][column]
        button = tkinter.Button(frame, text= value, font= ("Arial", 30),width= column_count-1, height= 1,
                                command= lambda value =  value: button_clicked(value))
        
        if value in upper_symbols:
            button.config(foreground= black_color, background= light_gray_color)
        
        elif value in right_symbols:
            button.config(foreground= white, background= orange_color)
        
        else :
            button.config(foreground= white , background= dark_gray_color)
            
        button.grid(row = row + 1, column= column)

A = "0"
operator = None
B = None

def clear_all():
    global A, operator, B 
    A = "0"
    operator = None
    B = None

def remove0(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value) :
    global right_symbols, upper_symbols, label, A, B, operator
    
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None :
                B = label["text"]
                numA = float(A)
                try:
                    numB = float(B)
                except ValueError:
                    label["text"] = "Error"
                    clear_all()
                    return

                if operator == "+":
                    label["text"] = remove0(numA + numB)
                elif operator == "-":
                    label["text"] = remove0(numA - numB)
                elif operator == "×":
                    label["text"] = remove0(numA
