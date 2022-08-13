from tkinter import *
from script import *  # this file contains port_scanner()


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(text="Enter the targets Ip Address",
                          fg='red', font=("Helvetica", 16))
        self.lbl1.place(x=52, y=120)
        self.txtfld1 = Entry(text="This is Entry Widget", bd=5)
        self.txtfld1.place(x=50, y=150)
        self.btn1 = Button(win, text="Run Nmap Scan",
                           fg='blue', command=self.scan)
        self.btn1.place(x=80, y=190)

    def scan(self):
        address = str(self.txtfld1.get())
        print(address)
        print(port_scanner(address))


window = Tk()
mywin = MyWindow(window)
window.title('Nmap')
window.geometry("300x300")
# Code


window.mainloop()
