import tkinter as tk
import logging

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.pack()
        self.create_widgets()
        
        logging.basicConfig(filename='calculator.log', level=logging.INFO)
        
    def create_widgets(self):
        self.equation = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.equation)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        
        row = 1
        col = 0
        
        for button in buttons:
            command = lambda x=button: self.click_button(x)
            tk.Button(self, text=button, width=5, height=2, command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
    def click_button(self, key):
        if key == "=":
            try:
                result = str(eval(self.equation.get()))
                self.equation.set(result)
                logging.info(f"{self.equation.get()} = {result}")
            except:
                self.equation.set("Error")
                logging.error(f"{self.equation.get()} caused an error")
        elif key == "C":
            self.equation.set("")
        else:
            self.equation.set(self.equation.get() + key)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(master=root)
    app.mainloop()