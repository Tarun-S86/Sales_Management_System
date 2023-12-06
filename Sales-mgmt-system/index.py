from tkinter import *
import curses
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
#from curses import KEY_SOPTIONS, window
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
    image = PhotoImage(file='C:\\Users\\iamta\\Desktop\\SMS\\Sales-mgmt-system\\images\\indexbg.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='#812ca8')
    



   
    b1=Button(root,text="Click to Start",command=pos,activebackground="blue",bg="#812ca8",width=30)
    b1.place(x=330,y=100)
    b2=Button(root,text="REGISTER HERE",command=ros,activebackground="pink",bg="#68BBE3",width=30)
    b2.place(x=363,y=160)
    
    root.mainloop()


