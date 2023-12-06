from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')



def verifier():
    a=b=c=d=e=f=0
    if not customer_name.get():
        #t1.insert(END,"<>Name is required<>\n")
        a=1
    if not customer_id.get():
        #t1.insert(END,"<>Customer ID is required<>\n")
        b=1
    if not address.get():
        #t1.insert(END,"<>Address is required<>\n")
        c=1
    if not phone.get():
        #t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not product_name.get():
       #t1.insert(END,"<>Product name is required<>\n")
        e=1
    if not units.get():
        #t1.insert(END,"<>Units is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        messagebox.showwarning("Warning","Fill the blank spaces.")
        return 1
    else:
        return 0


        

def ad():
    t1=datetime.datetime.now()
    m1=t1.strftime("%Y:%m:%d - %H:%M:%S")
    ls=customer_name.get()+'|'+customer_id.get()+'|'+address.get()+'|'+phone.get()+'|'+product_name.get()+'|'+units.get()+'|'+m1+"\n"
    
    p=open('products.txt','a')
    p.write(ls)
    p.close()
                    


def add_products():
            ret=verifier()
            if ret==0:
                ad()
                messagebox.showwarning("Succes","Added Successfully.")
                                 

def update_products():
    ret=verifier()
    if ret==0:
        dele.pos(customer_id.get())
        
        ad()
        messagebox.showwarning("Succes","Updated successfully")


        
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

   
    label=Label(root,text="UPDATE SALES INFO",font="bold",fg="Blue")
    label.place(x=420,y=90)
    customer_name=StringVar()
    customer_id=StringVar()
    address=StringVar()
    phone=StringVar()
    product_name=StringVar()
    units=StringVar()
    
    label1=Label(root,text="Customer Name:",fg='black',bg='light blue')
    label1.place(x=250,y=120)

    label2=Label(root,text="Customer ID:",fg='black',bg='light blue')
    label2.place(x=250,y=170)

    label3=Label(root,text="Address",fg='black',bg='light blue',)
    label3.place(x=250,y=270)

    label4=Label(root,text="Phone Number:",fg='black',bg='light blue')
    label4.place(x=250,y=220)

    label5=Label(root,text="Product Name:",fg='black',bg='light blue')
    label5.place(x=250,y=320)

    label6=Label(root,text="Units:",fg='black',bg='light blue')
    label6.place(x=250,y=370)

    e1=Entry(root,textvariable=customer_name,width=40)
    e1.place(x=420,y=120)

    e2=Entry(root,textvariable=customer_id,width=40)
    e2.place(x=420,y=170)

    e3=Entry(root,textvariable=address,width=40)
    e3.place(x=420,y=220)

    e4=Entry(root,textvariable=phone,width=40)
    e4.place(x=420,y=270)
    
    e5=Entry(root,textvariable=product_name,width=40)
    e5.place(x=420,y=320)

    e6=Entry(root,textvariable=units,width=40)
    e6.place(x=420,y=370)
   
    b4=Button(root,text="Submit",command=update_products,activebackground="blue",bg="light blue",width=30)
    b4.place(x=363,y=420)
    b3=Button(root,text="Back",command=clse,bg="light blue",activebackground="blue",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

