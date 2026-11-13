"""Tkinter calculator with sequential arithmetic and recoverable errors."""
import math
import tkinter as tk

class Calculator:
    def __init__(self):
        self.clear()

    def clear(self):
        self.text, self.left, self.operator, self.fresh = '0', None, None, True

    def show(self, value):
        if not math.isfinite(value):
            raise ValueError('Non-finite result')
        self.text = format(value, '.12g')

    def calculate(self):
        a, b = self.left, float(self.text)
        if self.operator == '+': self.show(a + b)
        elif self.operator == '-': self.show(a - b)
        elif self.operator == '×': self.show(a * b)
        elif self.operator == '÷': self.show(a / b)
        self.operator = None

    def press(self, key):
        try:
            if key == 'AC': self.clear()
            elif key.isdigit() or key == '.':
                if self.fresh or self.text == 'Error':
                    self.text, self.fresh = '0', False
                if key == '.':
                    if '.' not in self.text: self.text += '.'
                else: self.text = key if self.text == '0' else self.text + key
            elif self.text != 'Error':
                if key in ('+', '-', '×', '÷'):
                    if self.operator and not self.fresh: self.calculate()
                    self.left, self.operator, self.fresh = float(self.text), key, True
                elif key == '=':
                    if self.operator and not self.fresh: self.calculate()
                    self.fresh = True
                elif key == '+/-': self.show(-float(self.text))
                elif key == '%': self.show(float(self.text) / 100)
                elif key == '√':
                    self.show(math.sqrt(float(self.text)))
                    self.fresh = True
        except (ValueError, ZeroDivisionError, OverflowError):
            self.clear()
            self.text = 'Error'
        return self.text

def main():
    calculator = Calculator()
    window = tk.Tk()
    window.title('Calculator')
    window.resizable(False, False)
    display = tk.StringVar(value='0')
    tk.Label(window, textvariable=display, font=('Arial',36), bg='#1C1C1C',
             fg='white', anchor='e', width=14).grid(row=0,column=0,columnspan=4,sticky='ew')
    rows = [['AC','+/-','%','÷'],['7','8','9','×'],['4','5','6','-'],['1','2','3','+'],['0','.','√','=']]
    for row, keys in enumerate(rows,start=1):
        for column,key in enumerate(keys):
            utility = key in ('AC','+/-','%','√')
            color = '#FF9500' if key in ('+','-','×','÷','=') else '#D4D4D2' if utility else '#505050'
            tk.Button(window,text=key,font=('Arial',24),width=4,height=2,bg=color,
                      fg='black' if utility else 'white',
                      command=lambda value=key:display.set(calculator.press(value))).grid(row=row,column=column)
    window.mainloop()

if __name__ == '__main__':
    main()
