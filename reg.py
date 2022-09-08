from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#clear
def reset():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    course.set(0)
    pcourse.set(0)
    nat.set(0)
    cbu.set(0)
    gender.set(0)




sk=Tk()
fr=Frame(sk)
sk.maxsize(500,400)
sk.configure(bg="pink")

#submit
def Submit():
    name=s_name.get()
    fat=f_name.get()
    con=cont.get()
    emai=email.get()
    add=pa.get()
    cour=course.get()
    pcour=pcourse.get()
    nt=nat.get()
    chb=cbu.get()
    gend=gender.get()

    if name=="":
        messagebox.showerror("Error","please enter your name")
    elif fat=="":
        messagebox.showerror("Error","please enter father's name")
    elif con=="":
        messagebox.showerror("Error","please enter contact number")
    elif emai=="":
        messagebox.showerror("Error","please enter a valid email")
    elif add=="":
        messagebox.showerror("Error","please enter your address")
    elif cour=="":
        messagebox.showerror("Error","please select your course")
    elif pcour=="":
        messagebox.showerror("Error","please select your choice")
    elif chb=="":
        messagebox.showerror("Error","please click on checkbox icon")
    elif gend== "":
        messagebox.showerror("Error", "please select your gender")


    elif nt=="":
        messagebox.showerror("Error","please select your nationality")

    else:
        Label(sk,text="Registration successfull",font="14",bg="pink",fg="green").place(x=160,y=340)
    with open(name+".txt","w")as f:
        f.write(name+"\n")
        f.write(fat+"\n")
        f.write(con+"\n")
        f.write(emai+"\n")
        f.write(gend+"\n")
        f.write(add+"\n")
        f.write(cour+"\n")
        f.write(pcour+"\n")
        f.write(nt+"\n")











s_name=StringVar()
f_name=StringVar()
cont=StringVar()
email=StringVar()
pa=StringVar()
course=StringVar()
pcourse=StringVar()
nat=StringVar()
cbu=StringVar()
gender=StringVar()
sk.title("Student Registration Form")
l=Label(sk,text="Registration Form",bg="pink",fg="black",font=("helvetica",24))
l.place(x=2,y=0)
l1=Label(sk,text="Student Name:",bg="pink",fg="black")
l1.place(x=5,y=45)
e1=Entry(sk,textvariable=s_name)
e1.place(x=100,y=45)
l2=Label(sk,text="Father's name:",bg="pink",fg="black")
l2.place(x=5,y=70)
e2=Entry(sk,textvariable=f_name)
e2.place(x=100,y=70)
l3=Label(sk,text="Contact:",bg="pink",fg="black")
l3.place(x=5,y=100)
e3=Entry(sk,textvariable=cont)
e3.place(x=60,y=100)
l4=Label(sk,text="Gender:",bg="pink",fg="black")
l4.place(x=5,y=130)
rb=Radiobutton(sk,text="Male",fg="black",bg="pink",value=1,variable=gender)
rb.place(x=60,y=130)
rb1=Radiobutton(sk,text="Female",fg="black",bg="pink",value=0,variable=gender)
rb1.place(x=150,y=130)
l5=Label(sk,text="Email:",bg="pink",fg="black")
l5.place(x=5,y=160)
e4=Entry(sk,textvariable=email)
e4.place(x=60,y=160)
l6=Label(sk,text="Permanent Address:",bg="pink",fg="black")
l6.place(x=5,y=190)
e5=Entry(sk,width=20,textvariable=pa,font=("arrial",12))
e5.place(x=120,y=190)
l7=Label(sk,text="UG Course:",bg="pink",fg="black")
l7.place(x=5,y=220)
var=StringVar()
com=ttk.Combobox(sk,width=27,textvariable=course)
com.place(x=100,y=220)
com['value']=('BCA','BBA','B.COM')
l8=Label(sk,text="Regular/Reappear:",bg="pink",fg="black")
l8.place(x=5,y=250)
com1=ttk.Combobox(sk,width=27,textvariable=pcourse)
com1.place(x=120,y=250)
com1['value']=('Reglar','Reappear')
l9=Label(sk,text="Nationality:",bg="pink",fg="black")
l9.place(x=5,y=280)
com2=ttk.Combobox(sk,width=27,textvariable=nat)
com2['value']=('INDIA','NEPAL','BANGLADESH','SRILANKA','PAKISTAN','BHUTAN','UAE','AFGANISTAN','USA')
com2.place(x=80,y=280)
cb=Checkbutton(sk,text="I Accepted Terms&Condition",bg="pink",fg="black",variable=cbu)
cb.place(x=5,y=310)
b1=Button(sk,text="Submit",bg="green",fg="black",command=Submit)
b1.place(x=20,y=340)
b2=Button(sk,text="reset",bg="red",fg="black",width=8,command=reset)
b2.place(x=80,y=340)



sk.mainloop()
