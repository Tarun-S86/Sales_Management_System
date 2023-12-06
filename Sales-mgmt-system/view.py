from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox

def pos():
    root.destroy()
    os.system('python login.py')
    
def clse():
    root.destroy()
    os.system('python option.py')



        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("SALES MANAGEMENT SYSTEM")
    root.configure(bg='white')
    label=Label(root,text="SALES DETAILS",font="bold",fg="Red")
    label.place(x=363,y=50)
    customer_name=[]
    customer_id=[]
    address=[]
    Decease=[]
    units=[]
    ph=[]
    Date=[]
    norecord = 0
    f1 = open('products.txt', 'r')
    for line in f1:
        norecord += 1
        line = line.rstrip('\n')
        word = line.split('|')
        customer_name.append(word[0])
        customer_id.append(word[1])
        address.append(word[2])
        ph.append(word[3])
        Decease.append(word[4])
        units.append(word[5])
        Date.append(word[6])
    f1.close()
    borrow_list=Listbox(root,height=50,width=20)
    borrow_list1=Listbox(root,height=50,width=20)
    borrow_list2=Listbox(root,height=50,width=20)
    borrow_list3=Listbox(root,height=50,width=20)
    borrow_list4=Listbox(root,height=50,width=20)
    borrow_list5=Listbox(root,height=50,width=20)
    borrow_list6=Listbox(root,height=50,width=20)
    for num in range(0,norecord):
        borrow_list.insert(0,customer_name[num])
        borrow_list1.insert(0,customer_id[num])
        borrow_list2.insert(0,address[num])
        borrow_list3.insert(0,ph[num])
        borrow_list4.insert(0,Decease[num])
        borrow_list5.insert(0,units[num])
        borrow_list6.insert(0,Date[num])
    borrow_list.configure(background="light grey")
    borrow_list1.configure(background="light blue")
    borrow_list2.configure(background="light grey")
    borrow_list3.configure(background="light blue")
    borrow_list4.configure(background="light grey")
    borrow_list5.configure(background="light blue")
    borrow_list6.configure(background="light grey")

    borrow_label=Label(root,text="Customer Name")
    borrow_label2=Label(root,text="Customer ID")
    borrow_label3=Label(root,text="Address")
    borrow_label4=Label(root,text="Phone Number")
    borrow_label5=Label(root,text="Product Name")
    borrow_label6=Label(root,text="Units")
    borrow_label7=Label(root,text="Date")
	
    borrow_label.grid(row=3,column=0)
    borrow_label2.grid(row=3,column=1)
    borrow_label3.grid(row=3,column=4)
    borrow_label4.grid(row=3,column=7)
    borrow_label5.grid(row=3,column=8)
    borrow_label6.grid(row=3,column=10)
    borrow_label7.grid(row=3,column=12)

    borrow_list.grid(row=4,column=0)
    borrow_list1.grid(row=4,column=1)
    borrow_list2.grid(row=4,column=4)
    borrow_list3.grid(row=4,column=7)
    borrow_list4.grid(row=4,column=8)
    borrow_list5.grid(row=4,column=10)
    borrow_list6.grid(row=4,column=12)

    b3=Button(root,text="Back",command=clse,bg="light blue",activebackground="blue",width=118)
    b3.place(x=0,y=422)
    root.mainloop()

