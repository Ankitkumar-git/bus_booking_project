from tkinter import*
root=Tk()
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus = PhotoImage(file='Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12)
Label(root,text="Online Bus Booking System",font='Arial 28 bold',bg='sky blue',fg='red').grid(row=1,column=0,columnspan=12)
Label(root,text="Add Bus Route Details",font='Arial 20 bold',bg='gainsboro',fg='green4').grid(row=2,column=0,pady=20,columnspan=12)

Label(root,text="Route ID",font='Arial 12 bold',fg='black').grid(row=3,column=0,pady=50)
Entry(root,font="Arial 12").grid(row=3,column=1,padx=50)
Label(root,text="Station Name",font='Arial 12 bold',fg='black').grid(row=3,column=2)
Entry(root,font="Arial 12").grid(row=3,column=3,padx=50)
Label(root,text="Station ID",font='Arial 12 bold',fg='black').grid(row=3,column=4)
Entry(root,font="Arial 12").grid(row=3,column=5,padx=50)
Button(root,text="Add Route",font='Arial 12 bold',bg='green2',fg='black').grid(row=3,column=7,pady=20,padx=10)
Button(root,text="Delete Route",font='Arial 12 bold',bg='green2',fg='black').grid(row=3,column=9,pady=20,padx=10)
home = PhotoImage(file='home.png')
Button(root,image=home).grid(row=4,column=9)


root.mainloop()

