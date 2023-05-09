from tkinter import*
from tkinter.messagebox import *

root=Tk()
root.title('Online Bus Booking')
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,text='\n\n\n\n\n\n').pack()
Label(root,image=bus).pack()
Label(root,text="Online Bus Booking System",font='Arial 28 bold',bg='light blue',fg='red').pack()
Label(root,text="\n\n\nName: Ankit Kumar",font='Arial 15 bold',fg='blue').pack()
Label(root,text="\nEnr : 211B380",font='Arial 15 bold',fg='blue').pack()
Label(root,text="\nMobile : 9771197769\n\n\n\n",font='Arial 15 bold',fg='blue').pack()
Label(root,text="Submitted to: Dr. Mahesh Kumar",font='Arial 20 bold',bg='light blue',fg='red').pack()
Label(root,text="Project Based Learning",font='Arial 20 bold',fg='red').pack()

showinfo("GREET!","Welcome To Project")

