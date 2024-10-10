from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.lbl0 = Label(window, text="Simple Calculator", font=('Arial', 20))
        self.lbl0.place(x=150, y=10, height=50, width=300)

        self.lbl1 = Label(window, text="Number1: ", font=('Arial', 20))
        self.lbl1.place(x=50, y=60, height=40, width=150)
        self.e1 = Entry(window, bd=2, font=('Arial', 20))
        self.e1.place(x=200, y=60, height=40, width=150)

        self.lbl2 = Label(window, text="Number2:", font=('Arial', 20))
        self.lbl2.place(x=45, y=120, height=40, width=150)
        self.e2 = Entry(window, bd=2, font=('Arial', 20))
        self.e2.place(x=200, y=120, height=40, width=150)

        self.lbl3 = Label(window, text="Result", font=('Arial', 20))
        self.lbl3.place(x=20, y=200, height=50, width=200)

        self.results = Entry(window, font=('Arial', 20))
        self.results.place(x=200, y=200, height=40, width=200)

        self.add_button = Button(window, text="Add", font=('Arial', 10), command=self.add)
        self.add_button.place(x=50, y=300, height=40, width=60)

        self.sub_button = Button(window, text="Sub", font=('Arial', 10), command=self.sub)
        self.sub_button.place(x=120, y=300, height=40, width=60)

        self.multiply_button = Button(window, text="Multiply", font=('Arial', 10), command=self.multiply)
        self.multiply_button.place(x=190, y=300, height=40, width=60)

        self.divide_button = Button(window, text="Divide", font=('Arial', 10), command=self.divide)
        self.divide_button.place(x=260, y=300, height=40, width=60)

        self.clear_button = Button(window, text="Clear", font=('Arial', 10), command=self.clear)
        self.clear_button.place(x=330, y=300, height=40, width=60)

        self.exit_button = Button(window, text="Exit", font=('Arial', 10), command=window.destroy)
        self.exit_button.place(x=200, y=400, height=40, width=80)

    def add(self):
        num1 = float(self.e1.get())
        num2 = float(self.e2.get())
        sum_result = num1 + num2
        self.results.delete(0, END)
        self.results.insert(0, str(sum_result))

    def sub(self):
        num1 = float(self.e1.get())
        num2 = float(self.e2.get())
        sub_result = num1 - num2
        self.results.delete(0, END)
        self.results.insert(0, str(sub_result))

    def multiply(self):
        num1 = float(self.e1.get())
        num2 = float(self.e2.get())
        mult_result = num1 * num2
        self.results.delete(0, END)
        self.results.insert(0, str(mult_result))

    def divide(self):
        num1 = float(self.e1.get())
        num2 = float(self.e2.get())
        if num2 != 0:
            div_result = num1 / num2
            self.results.delete(0, END)
            self.results.insert(0, str(div_result))
        else:
            self.results.delete(0, END)
            self.results.insert(0, "Error") 

    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.results.delete(0, END)

window = Tk()
mywin = MyWindow(window)
window.title("My Calculator")
window.geometry("600x600")
window.mainloop()
