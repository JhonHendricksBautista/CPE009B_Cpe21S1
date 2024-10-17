from tkinter import *
from tkinter import messagebox
class Registration:
    def __init__(self, window):
        self.window = window
        self.window.title("REGISTRATION")
        self.window.geometry("600x600")




        self.lbl0 = Label(window, text="Account Resigation System", font=('Arial', 20))
        self.lbl0.place(x=50, y=20, height=20, width=400)

        self.lbl1 = Label(window, text="First Name", font=('Arial', 15))
        self.lbl1.place(x=35, y=60, height=40, width=150)
        self.e1 = Entry(window, bd=2, font=('Arial', 20))
        self.e1.place(x=200, y=60, height=40, width=300)

        self.lbl2 = Label(window, text="Last Name", font=('Arial', 15))
        self.lbl2.place(x=35, y=120, height=40, width=150)
        self.e2 = Entry(window, bd=2, font=('Arial', 20))
        self.e2.place(x=200, y=120, height=40, width=300)

        self.lbl3 = Label(window, text="Username", font=('Arial', 15))
        self.lbl3.place(x=35, y=180, height=50, width=150)
        self.e3 = Entry(window, bd=2, font=('Arial', 20))
        self.e3.place(x=200, y=180, height=40, width=300)

        self.lbl4 = Label(window, text="Email Address", font=('Arial', 15))
        self.lbl4.place(x=35, y=240, height=50, width=150)
        self.e4 = Entry(window, bd=2, font=('Arial', 20))
        self.e4.place(x=200, y=240, height=40, width=300)

        self.lbl5 = Label(window, text="Password", font=('Arial', 15))
        self.lbl5.place(x=35, y=300, height=50, width=150)
        self.e5 = Entry(window, bd=2, font=('Arial', 20), show= '*')
        self.e5.place(x=200, y=300, height=40, width=300)

        self.lbl6 = Label(window, text="Contact Number", font=('Arial', 15))
        self.lbl6.place(x=35, y=360, height=50, width=150)
        self.e6 = Entry(window, bd=2, font=('Arial', 20))
        self.e6.place(x=200, y=360, height=40, width=300)

        self.submit_button = Button(window, text="Submit", font=('Arial', 15), command = self.submit)
        self.submit_button.place(x=60, y=450, height=50, width=80)

        self.clear_button = Button(window, text="Clear", font=('Arial', 15), command = self.clear)
        self.clear_button.place(x=160, y=450, height=50, width=80)

    def submit(self):
        firstName = self.e1.get()
        lastName = self.e2.get()
        username = self.e3.get()
        password = self.e4.get()
        email_address = self.e5.get()
        contact_number = self.e6.get()



        if firstName and lastName and username and password and email_address and contact_number:
            messagebox.showinfo("Success","Registration Completed Succesfully")

        else:
            messagebox.showinfo("Error", "Invalid Entry")


    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)


        messagebox.showinfo("Clear", "Data is cleared")

