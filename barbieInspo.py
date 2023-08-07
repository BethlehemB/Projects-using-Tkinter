from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Barbies Coffee Shop")
root.resizable(False,False)

def Reset():
    entry_CakePop.delete(0, END)
    entry_Cupcake.delete(0,END)
    entry_Cookies.delete(0, END)
    entry_Tea.delete(0, END)
    entry_Coffee.delete(0,END)
    entry_Mocha.delete(0, END)
    entry_Cappuccino.delete(0,END)

def Total():
    try:a1 = int(CakePop.get())
    except: a1 = 0 

    try: a2 = int(Cupcake.get())
    except: a2 = 0

    try: a3 = int(Cookies.get())
    except: a3 = 0

    try: a4 = int(Tea.get())
    except: a4 = 0

    try: a5 = int(Coffee.get())
    except: a5 = 0

    try: a6 = int(Mocha.get())
    except: a6 = 0

    try: a7 = int(Cappuccino.get())
    except: a7 = 0

    #define cost of each item
    c1 = 1*a1
    c2 = 2.50*a2
    c3 = 3*a3
    c4= 2*a4
    c5= 1.50*a5
    c6= 3*a6
    c7 =3*a7

    lbl_total = Label(f2, font =('aria', 20,'bold'), text = "Total", width=16, fg = "lightpink", bg = "black")
    lbl_total.place(x=0, y=50)

    entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd =6, width=15, bg= "grey")
    entry_total.place(x=20, y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "$", str('%.2f' % totalcost)
    Total_bill.set(string_bill)



Label(text = "Barbies Coffee Shop", bg = "lightpink", fg="white", font=("calibri",33), width="300", height="2").pack()

#Menu Card
f = Frame(root, bg ="lightpink",highlightbackground="black",highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)

Label(f, text="MENU", font=("Gabriola",40,"bold"), fg="black", bg = "lightpink").place(x=60, y=0)


Label(f, font=("Lucida Calligraphy", 15, "bold"), text="CakePop.......$1.00/each", fg= "black", bg= "lightpink").place(x=10,y=200)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Cupcake.....$2.50/each", fg= "black", bg= "lightpink").place(x=10,y=80)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Cookies.........$3.00/5", fg= "black", bg= "lightpink").place(x=10,y=110)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Tea........$2.00/cup", fg= "black", bg= "lightpink").place(x=10,y=140)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Coffee......$1.50/cup", fg= "black", bg= "lightpink").place(x=10,y=170)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Mocha..........$3.00/cup", fg= "black", bg= "lightpink").place(x=10,y=230)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Cappuccino.....$3.00/cup", fg= "black", bg= "lightpink").place(x=10,y=260)


#bill
f2 = Frame(root, bg= "lightpink", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill = Label(f2, text = "Bill", font =("calibri",20),bg="lightpink")
Bill.place(x=120,y=10)
#ENTRY WORK
f1=Frame(root,bd=4,height=370,width=300,relief=RAISED)
f1.pack()

CakePop = StringVar()
Cupcake= StringVar()
Cookies = StringVar()
Tea = StringVar()
Coffee = StringVar()
Mocha = StringVar()
Cappuccino = StringVar()
Total_bill = StringVar()


# label
lbl_CakePop = Label(f1, font =("aria",20,'bold'), text = "CakePop", width=10, fg = "lightpink")
lbl_Cupcake = Label(f1, font =("aria",20,'bold'), text = "Cupcake", width=10, fg = "lightpink")
lbl_Cookies = Label(f1, font =("aria",20,'bold'), text = "Cookies", width=10, fg = "lightpink")
lbl_Tea = Label(f1, font =("aria",20,'bold'), text = "Tea", width=10, fg = "lightpink")
lbl_Coffee = Label(f1, font =("aria",20,'bold'), text = "Coffee", width=10, fg = "lightpink")
lbl_Mocha = Label(f1, font =("aria",20,'bold'), text = "Mocha", width=10, fg = "lightpink")
lbl_Cappuccino = Label(f1, font =("aria",20,'bold'), text = "Cappuccino", width=10, fg = "lightpink")

lbl_CakePop.grid(row =1, column=0)
lbl_Cupcake.grid(row =2, column=0)
lbl_Cookies.grid(row =3, column=0)
lbl_Tea.grid(row =4, column=0)
lbl_Coffee.grid(row =5, column=0)
lbl_Mocha.grid(row =6, column=0)
lbl_Cappuccino.grid(row = 7, column=0)

#entry
entry_CakePop = Entry(f1, font = ("aria", 20, 'bold'), textvariable=CakePop, bd =6, width=8,bg="grey")
entry_Cupcake = Entry(f1, font = ("aria", 20, 'bold'), textvariable=Cupcake, bd =6, width=8,bg="grey")
entry_Cookies = Entry(f1, font = ("aria", 20, 'bold'), textvariable=Cookies, bd =6, width=8,bg="grey")
entry_Tea = Entry(f1, font = ("aria", 20, 'bold'), textvariable=Tea, bd =6, width=8,bg="grey")
entry_Coffee = Entry(f1, font = ("aria", 20, 'bold'), textvariable=Coffee, bd =6, width=8,bg="grey")
entry_Mocha = Entry(f1, font = ("aria", 20, 'bold'), textvariable=Mocha, bd =6, width=8,bg="grey")
entry_Cappuccino = Entry(f1, font = ("aria", 20, 'bold'), textvariable=Cappuccino, bd =6, width=8,bg="grey")


entry_CakePop.grid(row =1, column=1)
entry_Cupcake.grid(row =2, column=1)
entry_Cookies.grid(row =3, column=1)
entry_Tea.grid(row =4, column=1)
entry_Coffee.grid(row =5, column=1)
entry_Mocha.grid(row =6, column=1)
entry_Cappuccino.grid(row =7, column=1)


#buttons

btn_reset = Button(f1, bd=5, fg="black", bg="grey", font =("ariel",16,'bold'), width=10, text= "Reset", command= Reset)
btn_reset.grid(row=8, column=0)



btn_total = Button(f1, bd=5, fg= "black", bg="lightpink", font = ("ariel", 16, 'bold'), width=10, text = "Total", command = Total)
btn_total.grid(row=8, column=1)

root.mainloop()
