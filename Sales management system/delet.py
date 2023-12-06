from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')



def delete_product():
    if not customer_id.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
    else:
        dele.pos(customer_id.get())
        dele.pos1(customer_id.get())
        dele.pos2(customer_id.get())
        messagebox.showwarning("Success","Deleted Successfully.")

        

                    





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("SALES MANAGEMENT SYSTEM")
    root.configure(bg='#a8a8f8')

   
    label=Label(root,text="DELETE",font="bold",fg="blue",bg='#a8a8f8')
    label.place(x=450,y=50)

    customer_id=StringVar()


    label2=Label(root,text="Customer ID:",bg='#a8a8f8')
    label2.place(x=300,y=170)





    e2=Entry(root,textvariable=customer_id,width=40)
    e2.place(x=420,y=170)

   
    b4=Button(root,text="Delete",command=delete_product,activebackground="red",bg="#d13f3f",width=30)
    b4.place(x=363,y=240)
    b3=Button(root,text="Back",command=clse,bg="#a061d8",activebackground="blue",width=30)
    b3.place(x=363,y=300)
    root.mainloop()

