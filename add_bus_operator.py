from tkinter import*
root=Tk()
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus = PhotoImage(file='Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12)
Label(root,text="Online Bus Booking System",font='Arial 28 bold',bg='sky blue',fg='red').grid(row=1,column=0,columnspan=12)
Label(root,text="Add Bus Operator Details",font='Arial 20 bold',bg='gainsboro',fg='green4').grid(row=2,column=0,pady=20,columnspan=12)
Label(root,text="Operator ID",font='Arial 12 bold',fg='black').grid(row=3,column=0,pady=50)
Entry(root,font="Arial 12").grid(row=3,column=1)
Label(root,text="Name",font='Arial 12 bold',fg='black').grid(row=3,column=2)
Entry(root,font="Arial 12").grid(row=3,column=3)
Label(root,text="Address",font='Arial 12 bold',fg='black').grid(row=3,column=4)
Entry(root,font="Arial 12").grid(row=3,column=5)
Label(root,text="Phone",font='Arial 12 bold',fg='black').grid(row=3,column=6)
Entry(root,font="Arial 12").grid(row=3,column=7)
Label(root,text="Email",font='Arial 12 bold',fg='black').grid(row=3,column=8)
Entry(root,font="Arial 12").grid(row=3,column=9)
Button(root,text="Add",font='Arial 12 bold',bg='green2',fg='black').grid(row=3,column=10,padx=10)
Button(root,text="Edit",font='Arial 12 bold',bg='green2',fg='black').grid(row=3,column=11,padx=10)

home = PhotoImage(file='home.png')
Button(root,image=home).grid(row=7,column=11)
root.mainloop()