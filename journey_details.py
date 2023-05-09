from tkinter import*
from tkinter.messagebox import*
root=Tk()

h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus = PhotoImage(file='Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=3,columnspan=12)
Label(root,text="Online Bus Booking System",font='Arial 28 bold',bg='sky blue',fg='red').grid(row=2,column=3,pady=20,columnspan=12)
Label(root,text='Enter Journey Details',bg='gainsboro',fg='green4',font='Arial 20 bold').grid(row=3,column=3,columnspan=12,pady=20)

to_place=''
Label(root,text='To',fg='black',font='Arial 12 bold').grid(row=4,column=3,padx=30)
to_place=Entry(root,font='Arial 12 bold',fg='black')
to_place.grid(row=4,column=4,padx=50)

from_place=''
Label(root,text='From',fg='black',font='Arial 12 bold').grid(row=4,column=5,padx=30)
from_place=Entry(root,font='Arial 12 bold',fg='black')
from_place.grid(row=4,column=6,padx=50)

j_date=''
Label(root,text='Journey date',fg='black',font='Arial 12 bold').grid(row=4,column=7,padx=30)
j_date=Entry(root,font='Arial 12 bold',fg='black')
j_date.grid(row=4,column=8,padx=50)

def check():
    if to_place.get()=='':
        showerror('value missing',"enter to place")
    if from_place.get()=='':
        showerror('value missing',"enter from place")
    if j_date.get()=='':
        showerror("value missing","enter journey date")
        
Button(root,text='Show Bus',command=check,bg='green',fg='black',font='Arial 12 bold').grid(row=4,column=9,padx=30)
home=PhotoImage(file='home.png')
Button(root,image=home).grid(row=4,column=10)



root.mainloop()
