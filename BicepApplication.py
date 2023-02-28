from tkinter import *
from LeftCurlApp import LeftCurl
from RightCurlApp import RightCurl
from BarbellCurlApp import BarbellCurl

class AppWindow:
    def __init__(self,root):
        self.window = root
        self.window.title("Welcome to trAIner application")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="cyan")

        self.frame3 = Frame(self.window, bg="white")
        self.frame3.place(x=140,y=100,width=1000,height=550)

        self.video_button = Button(self.frame3,text="Left Bicep Exercise",command=self.LeftBicep_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=100,width=500)
        self.video_button = Button(self.frame3,text="Right Bicep Exercise",command=self.RightBicep_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=250,width=500)
        self.video_button = Button(self.frame3,text="Barbell Curl Exercise",command=self.BarbellCurl_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=400,width=500)


    def LeftBicep_func(self):
        self.window.destroy()

        root=Tk()
        obj=LeftCurl(root)
        root.mainloop()
    
    def RightBicep_func(self):
        self.window.destroy()

        root=Tk()
        obj=RightCurl(root)
        root.mainloop()
    
    def BarbellCurl_func(self):
        self.window.destroy()
        root=Tk()
        obj=BarbellCurl(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = AppWindow(root)
    root.mainloop()