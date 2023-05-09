from tkinter import*
root=Tk()
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus = PhotoImage(file='Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12)
Label(root,text="Online Bus Booking System",font='Arial 28 bold',bg='sky blue',fg='red').grid(row=1,column=0,columnspan=12)
Label(root,text="Add Bus Details",font='Arial 20 bold',bg='gainsboro',fg='green4').grid(row=2,column=0,pady=20,columnspan=12)
Label(root,text="Bus ID",font='Arial 12 bold',fg='black').grid(row=3,column=1,pady=50)
Entry(root,font="Arial 12").grid(row=3,column=2)

bus_type=StringVar()
bus_type.set("Select Bus Type")
opt=["2x2","AC 2x2","3x2","AC 3x2"]
d_menu=OptionMenu(root,bus_type,*opt).grid(row=3,column=3)


Label(root,text="Capacity",font='Arial 12 bold',fg='black').grid(row=3,column=4)
Entry(root,font="Arial 12").grid(row=3,column=5)
Label(root,text="Fare Rs",font='Arial 12 bold',fg='black').grid(row=3,column=6)
Entry(root,font="Arial 12").grid(row=3,column=7)
Label(root,text="Operator ID",font='Arial 12 bold',fg='black').grid(row=3,column=8)
Entry(root,font="Arial 12").grid(row=3,column=9)
Label(root,text="Route ID",font='Arial 12 bold',fg='black').grid(row=3,column=10)
Entry(root,font="Arial 12").grid(row=3,column=11)

Button(root,text="Add Bus",font='Arial 12 bold',bg='green2',fg='black').grid(row=5,column=4,pady=20,columnspan=4)
Button(root,text="Edit Bus",font='Arial 12 bold',bg='green2',fg='black').grid(row=5,column=5,pady=20,columnspan=4)
home = PhotoImage(file='home.png')
Button(root,image=home).grid(row=5,column=6,columnspan=3)
root.mainloop()
