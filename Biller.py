from tkinter import *
global text

#FUNCTIONS 
def value():
	text.set('hai')
 	
#variables
root=Tk()
text=StringVar()

#frameS
frame=Frame(root,bg='#9fa009',bd=30,relief=RIDGE)
frame.pack()

frame1=Frame(frame,bg='#9fa009',bd=30,relief=RIDGE)
frame1.pack()

#heading
Label(frame1,bg='#9fa009',fg='white',text='...Heading...',font=("arial",17,"bold")).pack(padx=20,pady=20)

#Entry
word=Entry(frame1,bg='black',fg='white',font=('arial',23,'bold'),textvariable=text).pack(padx=20,pady=20,)

#submit
submit=Button(frame1,bd=4,text='SUBMIT',font=("arial",17,"bold"),fg="white",bg='black',justify=CENTER,command=value).pack()

root.mainloop()