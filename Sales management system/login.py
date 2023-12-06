from tkinter import *
import os,index,datetime,sys
from register import *
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    sys.exit() 

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
def pos():
    ret=verifier()
    if ret==0:
        h=open("admin.txt",'r')
        
        for line in h:
            temp = line.split('|')
            if temp[0]==customer_name.get() and verify_password(temp[1],phone.get()):
                
                # make_pass(phone)   if we give hash password it works
                # check_pass(phone,hash)
                messagebox.showwarning("success","Authorization Success.")
                root.destroy()
                rec()
                os.system('python option.py')
                break
        else:
            messagebox.showwarning("Warning","Employee id or password is incorrect.")
    else:
        messagebox.showwarning("Warning","Type Employee id and password.")
def verifier():
    a=b=0
    if not customer_name.get():
        a=1
    if not phone.get():
        b=1
    if a==1 or b==1 :
        return 1
    else:
        return 0  
        
def rec():
    o=datetime.datetime.now()
    k=o.strftime("%Y:%m:%d | %H:%M:%S")
    rc=customer_name.get()+" | "+k
    g=open("record.txt",'a')
    g.write(rc)
    g.write('\n')
    g.close()

                  




        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("SALES MANAGEMENT SYSTEM")
    root.configure(bg='#a8a8f8')

    customer_name=StringVar()
    phone=StringVar()
    label=Label(root,text="LOGIN",font="bold",fg="blue",bg='#a8a8f8')
    label.place(x=450,y=50)
    label1=Label(root,text="Username :",bg='#a8a8f8')
    label1.place(x=360,y=120)

    label2=Label(root,text="Password :",bg='#a8a8f8')
    label2.place(x=360,y=150)


    e1=Entry(root,textvariable=customer_name)
    e1.place(x=460,y=120)

    e2=Entry(root,show='*',textvariable=phone)
    e2.place(x=460,y=150)
   
    b4=Button(root,text="Submit",command=pos,activebackground="green",bg="#0dba98",width=30)
    b4.place(x=363,y=200)
    b3=Button(root,text="Close",command=clse,bg="#d13f3f",activebackground="red",width=30)
    b3.place(x=363,y=240)
    root.mainloop()

