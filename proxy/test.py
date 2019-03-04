import socket, sys
from tkinter import *
from threading import *
def GUI():
    window = Tk()
    window.title("welcome to your proxy")
    lbl = Label(window, text="enter your url")
    txt = Entry(window, width=32)
    txt.grid(column=1, row=0)


    def cliked():
        lbl.configure(text="Button was clicked")
        print(txt.get())


    btn = Button(window,text="click Me", command=cliked)
    btn.grid(column=2, row=0)

    window.mainloop()

Thread(group=None,target=GUI,name="GUI").start()

