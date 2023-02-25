import tkinter
import threading
from tkinter import messagebox
from os import system

window = tkinter.Tk()
window.title("Don't close")
window.geometry("300x300")

def close_window():
    makeThread()
    
def openWindow():
    system("python3 main.py")
    
def makeThread():
    t = threading.Thread(target=openWindow)
    t.start()
    
def on_closing():
    if messagebox.askokcancel("Try and quit", "You wanna try?"):
        makeThread()
    else:
        window.destroy()

button = tkinter.Button(window, text="Close", command=close_window)
button.pack()

button2 = tkinter.Button(window, text="Open", command=makeThread)
button2.pack()


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()