
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
                numB = float(B) 
                if operator == "+":
                    label["text"] = remove0(numA + numB)
                elif operator == "-":
                    label["text"] = remove0(numA - numB)
                elif operator == "×":
                    label["text"] = remove0(numA * numB)
                elif operator =="÷":
                    label["text"] = remove0(numA / numB)
                
                clear_all()
        
            
        elif value in "+-×÷":
            if operator is None :
                A = label["text"] 
                label["text"] = "0"
                B = "0"
            operator = value
    
    elif value in upper_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
            
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove0(result)
            
        elif value == "%": 
            result = float(label["text"]) / 100
            label["text"] = remove0(result)
            label["text"] = f"{result}%"
        
        elif value == "√":
            try:
                num = float(label["text"])
                if num < 0:
                    label["text"] = "Error"
                else:
                    label["text"] = f"{num ** 0.5:.3f}"
            except ValueError:
                label["text"] = "Error"
    
            
        
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
                
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
                
            else :
                label["text"] += value 
frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height /2)  - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()