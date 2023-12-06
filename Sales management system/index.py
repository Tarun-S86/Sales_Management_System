from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    sys.exit() 

def pos():
    root.destroy()
    os.system('python login.py')
    
def ros():
    root.destroy()
    os.system('python register.py')   

        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("SALES MANAGEMENT SYSTEM")
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='C:\\Users\\iamta\\Desktop\\final\\Sales management system\\images\\indexbg.png')
    root.create_image(0,0,anchor = NW, image = image)
    
    root.configure(bg='magenta')

   
    b1=Button(root,text="LOGIN",command=pos,activebackground="blue",bg="#a061d8",width=30)
    b1.place(x=330,y=50)
    b2=Button(root,text="REGISTER",command=ros,activebackground="blue",bg="#a061d8",width=30)
    b2.place(x=330,y=95)
    
    root.mainloop()


