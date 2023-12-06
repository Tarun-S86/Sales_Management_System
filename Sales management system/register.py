import binascii
import hashlib
from tkinter import *
import tkinter.font
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    root.destroy()
    os.system('python index.py')
def log():
	root.destroy()
	os.system('python login.py')

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')



def verifier():
    a=b=c=d=0
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
    
    if a==1 or b==1 or c==1 or d==1: #or e==1 or f==1:
        messagebox.showwarning("Warning","Fill the blank spaces.")
        return 1
    else:
        return 0


def ad():
	f = open('admin.txt', 'a')
	pos = f.tell()
	buf = customer_name.get() + '|' + hash_password(phone.get()) + '|' + '#' +'\n'
	f.write(buf)
	f.write('\n')
	f.close()
	tkinter.messagebox.showinfo("Register", "Registration successful!")
        
                        
def add_products():
            ret=verifier()
            if ret==0:
                ad()
                log()
                messagebox.showwarning("Success","Added Successfully.")
                                 


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
    root.title("")
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='C:\\Users\\iamta\\Desktop\\SMS\\Sales-mgmt-system\\images\\bgc.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='#812ca8')

   
    label=Label(root,text="Enter your details",font="bold",fg="Blue")
    label.place(x=420,y=90)
    customer_name=StringVar()
    customer_id=StringVar()
    address=StringVar()
    phone=StringVar()
    product_name=StringVar()
    units=StringVar()
    
    label1=Label(root,text="Username:",bg='light blue')
    label1.place(x=250,y=120)

    label2=Label(root,text="Phone number:",bg='light blue')
    label2.place(x=250,y=170)

    label3=Label(root,text="Email:",bg='light blue')
    label3.place(x=250,y=220)

    label4=Label(root,text="Password:",bg='light blue')
    label4.place(x=250,y=270)

    

    e1=Entry(root,textvariable=customer_name,width=40)
    e1.place(x=420,y=120)

    e2=Entry(root,textvariable=customer_id,width=40)
    e2.place(x=420,y=170)

    e3=Entry(root,textvariable=address,width=40)
    e3.place(x=420,y=220)

    e4=Entry(root,textvariable=phone,width=40)
    e4.place(x=420,y=270)
    
    
   
    b4=Button(root,text="Submit",command=add_products,activebackground="blue",bg="#6292c4",width=30)
    b4.place(x=363,y=420)

    

    b3=Button(root,text="Back",command=clse,bg="#6292c4",activebackground="red",width=30)
    b3.place(x=650,y=420)
    root.mainloop()

