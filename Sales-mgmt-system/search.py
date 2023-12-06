from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')

def ver():
    a=0
    if not customer_name.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
        a=1
    return a


# def delete_products():
#     if not op.get():
#         messagebox.showwarning("Warning","Fill the blank spaces.")
#     else:
#         dele.pos(op.get())
        
#         messagebox.showwarning("Succes","Deleted Successfully.")

def ser():
    t=ver()
    if (t==0):
        f=open("products.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(customer_name.get())!=-1:
                t1.insert(END,"\n"+i+"\n")      

                    





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("SALES MANAGEMENT SYSTEM")
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='C:\\Users\\iamta\\Desktop\\SMS\\Sales-mgmt-system\\images\\bgc.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='white')

   
    label=Label(root,text="SEARCH",font="bold",fg="Blue")
    label.place(x=450,y=20)

    customer_name=StringVar()


    label2=Label(root,text="Name:", bg='light blue')
    label2.place(x=300,y=90)





    e2=Entry(root,textvariable=customer_name,width=40)
    e2.place(x=420,y=90)

   
    b4=Button(root,text="Search",command=ser,activebackground="blue",bg="light blue",width=30)
    b4.place(x=350,y=190)
    t1=Text(root,width=90,height=10)
    t1.place(x=0,y=280)
    b3=Button(root,text="Back",command=clse,bg="light blue",activebackground="blue",width=30)
    b3.place(x=350,y=230)
    root.mainloop()

