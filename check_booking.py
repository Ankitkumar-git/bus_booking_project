from tkinter import*
from tkinter.messagebox import*

root=Tk()
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus = PhotoImage(file='Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=12,padx=80)
Label(root,text="Online Bus Booking System",font='Arial 28 bold',bg='sky blue',fg='red').grid(row=2,column=0,columnspan=12,pady=20)
Label(root,text="Check Your Booking",font='Arial 22 bold',bg='gainsboro',fg='green4').grid(row=3,column=0,pady=20,columnspan=12,padx=600)
mobile=''
Label(root,text="Enter your mobile no.",font='Arial 12 bold',fg='black').grid(row=4,column=5)
mobile=Entry(root,font='Arial 12 bold')
mobile.grid(row=4,column=6)

l=[0,1,2,3,4,5,6,7,8,9]

def check_mobile():
    if len(mobile.get())==10:
        if mobile.get().isdigit():
                showerror("value error","mobile number should only contain digits")
    :
        showerror("value error","enter valid number")
        
Button(root,text='Check Booking',font='Arial 12',command=check_mobile).grid(row=4,column=7)


            
        




root.mainloop()

