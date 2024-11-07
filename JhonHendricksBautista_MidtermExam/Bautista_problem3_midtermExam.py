from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Midterm in OOP")
        self.geometry("450x250")
        self.initUI()

    def initUI(self):
        self.label1 = Label(self, text="Enter your fullname: ", font = ('Arial', 8,), fg = 'red')
        self.label1.place(x = 20, y = 60, height = 50, width = 100)
        
        self.entry1 = Entry(self, bd = 3, font = ('Arial', 15))
        self.entry1.place(x = 220, y = 75, height = 30, width = 210)
        

        self.button = Button(self, text="Click to display your Fullname", font = ('Arial', 8), fg = 'red', command = self.display_info)
        self.button.place(x = 20, y = 115, height = 20, width = 150)
        
        self.output = Entry(self, bd = 3, font = ('Arial', 15), state='readonly', bg = 'white')
        self.output.place(x=220, y=110, height = 30, width = 210 )
        
    def display_info(self):

        name = str(self.entry1.get())
        
        self.output.config(state='normal')
        self.output.delete(0, END)
        self.output.insert(0, name)
        self.output.config(state='readonly')         

if __name__ == '__main__':
    app = App()
    app.mainloop()