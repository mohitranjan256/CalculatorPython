from tkinter import *
boot=Tk()

boot.title("Calculator")
boot.minsize(455,415)
boot.maxsize(455,415)
boot.configure(bg="black")

operator=""

def click(num):
    global operator
    if(num=="AC"):
        operator=""
        txt_int.set(operator)
        return operator
    elif(num=="C"):
        lenght=len(e.get())
        e.delete(lenght-1,'end')
        if(len(e.get())==0):
            operator=""
    elif(num=="="):
        Reso=str(eval(operator))
        txt_int.set(Reso)
        operator=""

    else:       
        operator=str(operator) + str(num)
        txt_int.set(operator)
        


txt_int=StringVar()

    

#-----------------------------------------------------

e=Entry(boot,font=('arial',20,'bold'),bg="light yellow",bd=5,textvariable=txt_int)
e.place(x=10,y=5,width=430)

#------------------------------------------------------
b7=Button(boot,text="7", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(7))
b7.place(x=10,y=70,width=70)

b8=Button(boot,text="8", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(8))
b8.place(x=100,y=70,width=70)


b9=Button(boot,text="9", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(9))
b9.place(x=190,y=70,width=70)


b_AC=Button(boot,text="AC", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click("AC"))
b_AC.place(x=280,y=70,width=70)


b_C=Button(boot,text="C", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click("C"))
b_C.place(x=370,y=70,width=70)


#-----------------------------------------------------------

b4=Button(boot,text="4", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(4))
b4.place(x=10,y=150,width=70)

b5=Button(boot,text="5", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(5))
b5.place(x=100,y=150,width=70)


b6=Button(boot,text="6", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(6))
b6.place(x=190,y=150,width=70)

b_MUL=Button(boot,text="X", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click('*'))
b_MUL.place(x=280,y=150,width=70)


b_DIV=Button(boot,text="÷", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click('/'))
b_DIV.place(x=370,y=150,width=70)


#---------------------------------------------------------------


b3=Button(boot,text="3", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(3))
b3.place(x=10,y=230,width=70)

b2=Button(boot,text="2", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(2))
b2.place(x=100,y=230,width=70)


b1=Button(boot,text="1", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(1))
b1.place(x=190,y=230,width=70)


b_ADD=Button(boot,text="+", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click('+'))
b_ADD.place(x=280,y=230,width=70)


b_SUB=Button(boot,text="-", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click('-'))
b_SUB.place(x=370,y=230,width=70)


#-------------------------------------------------------------------


b0=Button(boot,text="0", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click(0))
b0.place(x=10,y=310,width=70)

b00=Button(boot,text="00", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click('00'))
b00.place(x=100,y=310,width=70)


b_point=Button(boot,text=".", font=('arial',20,'bold'),fg="white" ,bg="black",bd=5,command=lambda:click('.'))
b_point.place(x=190,y=310,width=70)


b_percent=Button(boot,text="%", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click('%'))
b_percent.place(x=280,y=310,width=70)


b_equals=Button(boot,text="=", font=('arial',20,'bold'), bg="blue",bd=5,command=lambda:click("="))
b_equals.place(x=370,y=310,width=70)


#----------------------------------------------------------------------

l1=Label(boot,text="____Made By Mohit__Ranjan___", font=('arial',20,'bold'))
l1.place(x=10,y=380)



boot.mainloop()
