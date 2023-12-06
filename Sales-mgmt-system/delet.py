from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')



def delete_products():
    if not customer_id.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
    else:
        dele.pos(customer_id.get())
        
        messagebox.showwarning("Success","Deleted Successfully.")

        

                    





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("SALES MANAGEMENT SYSTEM")
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='C:\\Users\\iamta\\Desktop\\SMS\\Sales-mgmt-system\\images\\bgc.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='#812ca8')

   
    label=Label(root,text="DELETE",font="bold",fg="Blue")
    label.place(x=420,y=90)

    customer_id=StringVar()


    label2=Label(root,text="Customer ID:",fg='black',bg='light blue')
    label2.place(x=250,y=170)





    e2=Entry(root,textvariable=customer_id,width=40)
    e2.place(x=420,y=170)

   
    b4=Button(root,text="Delete",command=delete_products,activebackground="blue",bg="light blue",width=30)
    b4.place(x=363,y=240)
    b3=Button(root,text="Back",command=clse,bg="light blue",activebackground="blue",width=30)
    b3.place(x=363,y=290)
    root.mainloop()

