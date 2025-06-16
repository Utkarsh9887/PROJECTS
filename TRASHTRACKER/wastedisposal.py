from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from organic import Organicclass
from recyclable import recyclableclass
from non_recyclable import non_recyclableclass
from e_waste import ewasteclass
from industrial_waste import industrialclass
from hazardous import hazardousclass

class wastedisposalclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500")
        self.root.title("WASTE DISPOSAL")
        self.root.config(bg="white")
        self.root.focus_force()
        border=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        border.place(x=50,y=50,width=1020,height=400)
        btn_Supplier=Button(border,text="Organic Waste     ",command=self.organic,font=("times new roman",20,"bold"),bg="Light Blue",bd=3).place(x=75,y=70,height=100)
        btn_Supplier=Button(border,text="Recyclable Waste",command=self.recyclable,font=("times new roman",20,"bold"),bg="Light Blue",bd=3).place(x=350,y=70,height=100)
        btn_Supplier=Button(border,text="Non-Recyclable Waste",command=self.non_recyclable,font=("times new roman",20,"bold"),bg="Light Blue",bd=3).place(x=630,y=70,height=100)
        btn_Supplier=Button(border,text="Hazardous Waste",font=("times new roman",20,"bold"),command=self.hazardous,bg="Light Blue",bd=3).place(x=75,y=200,height=100) 
        btn_Supplier=Button(border,text="E-Waste         ",command=self.e_waste,font=("times new roman",20,"bold"),bg="Light Blue",bd=3).place(x=350,y=200,height=100)
        btn_Supplier=Button(border,text="Industrial Waste",command=self.industrialwaste,font=("times new roman",20,"bold"),bg="Light Blue",bd=3).place(x=630,y=200,height=100)
    def organic(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Organicclass(self.new_win)
    def recyclable(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=recyclableclass(self.new_win)
    def non_recyclable(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=non_recyclableclass(self.new_win)
    def hazardous(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=hazardousclass(self.new_win)    
    def e_waste(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ewasteclass(self.new_win) 
    def industrialwaste(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=industrialclass(self.new_win)         
                     
            
if __name__ == "__main__":
    root = Tk()
    obj = wastedisposalclass(root)
    root.mainloop()
