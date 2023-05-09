from tkinter import*
root=Tk()
root.title('Second Page')
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,text='\n\n\n\n').grid(row=0,column=0)
Label(root,image=bus).grid(row=1,column=1,columnspan=12,padx=w//3.2)
Label(root,text="Online Bus Booking System",font='Arial 28 bold',bg='light blue',fg='red').grid(row=2,column=2,columnspan=9,padx=w//3.2)
Label(root,text='\n\n\n\n\n\n').grid(row=3,column=4)
Button(root,text='Seat Booking',font='Arial 12 bold',bg='Light green',fg='black').grid(row=4,column=4)
Label(root,text='\n\n\n\n\n\n').grid(row=3,column=6)
Button(root,text='Check Booked Seat',font='Arial 12 bold',bg='green3',fg='black').grid(row=4,column=6)
Label(root,text='\n\n\n\n\n\n').grid(row=3,column=8)
Button(root,text='Add Bus Details',font='Arial 12 bold',bg='green',fg='black').grid(row=4,column=8)
Label(root,text='\n').grid(row=5,column=8)
Label(root,text='For Admin Only',font='Arial 12 bold',fg='red').grid(row=6,column=8)


