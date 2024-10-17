import tkinter as tk
from registration import Registration

if __name__ == "__main__":
    window = tk.Tk()
    mywin = Registration(window)
    window.mainloop()