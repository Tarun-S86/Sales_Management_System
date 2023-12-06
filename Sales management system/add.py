from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    root.destroy()
    os.system('python option.py')



def verifier():
    a=b=c=d=e=f=0
    if not customer_name.get():
        #t1.insert(END,"<>customer_name is required<>\n")
        a=1
    if not customer_id.get():
        #t1.insert(END,"<>Adhar no is required<>\n")
        b=1
    if not address.get():
        #t1.insert(END,"<>Age is required<>\n")
        c=1
    if not phone.get():
        #t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not product_name.get():
       #t1.insert(END,"<>Covid test result name is required<>\n")
        e=1
    if not units.get():
        #t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        messagebox.showwarning("Warning","Fill the blank spaces.")
        return 1
    else:
        return 0


        

def ad():
    cn=customer_name.get()
    pos = binary_search('product.txt', cn)
    t1=datetime.datetime.now()
    m1=t1.strftime("%Y:%m:%d - %H:%M:%S")
    p=open('product.txt','a')
    pos=p.tell()
    ls=str(pos)+'|'+cn+'|'+customer_id.get()+'|'+address.get()+'|'+phone.get()+'|'+product_name.get()+'|'+units.get()+'|'+m1+"\n"
    p.write(ls)
    p.close()
                    
def ad2():
    ls2=customer_name.get()+'|'+customer_id.get()+'|'+address.get()+'|'+phone.get()+'|'+product_name.get()+'|'+units.get()+"\n"
    p=open('product2.txt','a')
    p.write(ls2)
    p.close()

def add_products():
            ret=verifier()
            if ret==0:
                ad()
                ad2()
                sorting('product2.txt')
                messagebox.showwarning("Success","Added Successfully.")
                                 
def sorting(filename):
    infile = open('product2.txt', 'r')
    words = []
    for line in infile:
        temp = line.split()
        for i in temp:
            words.append(i)
        #words.append('\n')    
    infile.close()
    words.sort()
    outfile = open("result.txt", "w")
    for i in words:
        outfile.writelines(i)
        outfile.writelines('\n')
    outfile.close()


def binary_search(fname, search_key):
	t = []
	fin = open(fname,'r')
	for lx in fin:
		lx = lx.rstrip()
		wx = lx.split('|')
		t.append((wx[0], wx[1]))
	fin.close()
	l = 0
	r = len(t) - 1
	while l <= r:
		mid = (l + r)//2
		if t[mid][0] == search_key:
			return int(t[mid][1])
		elif t[mid][0] <= search_key:
			l = mid + 1
		else:
			r = mid - 1
	return -1




        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("SALES MANAGEMENT SYSTEM")
    root.configure(bg='#a8a8f8')

   
    label=Label(root,text="ADD DETAILS",font="bold",fg="blue",bg='#a8a8f8')
    label.place(x=450,y=50)
    customer_name=StringVar()
    customer_id=StringVar()
    address=StringVar()
    phone=StringVar()
    product_name=StringVar()
    units=StringVar()
    
    label1=Label(root,text="Customer Name:",bg='#a8a8f8')
    label1.place(x=280,y=120)

    label2=Label(root,text="Customer ID:",bg='#a8a8f8')
    label2.place(x=280,y=170)

    label3=Label(root,text="Address:",bg='#a8a8f8')
    label3.place(x=280,y=220)

    label4=Label(root,text="Phone Number:",bg='#a8a8f8')
    label4.place(x=280,y=270)

    label5=Label(root,text="Product Name:",bg='#a8a8f8')
    label5.place(x=280,y=320)

    label6=Label(root,text="Units:",bg='#a8a8f8')
    label6.place(x=280,y=370)

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
   
    b4=Button(root,text="Submit",command=add_products,activebackground="green",bg="#0dba98",width=30)
    b4.place(x=363,y=420)
    b3=Button(root,text="Back",command=clse,bg="#d13f3f",activebackground="red",width=30)
    b3.place(x=630,y=420)
    root.mainloop()

