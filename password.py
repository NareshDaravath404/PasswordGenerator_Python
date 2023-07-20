from tkinter import *
from random import randint

root=Tk()
root.title('Ramdom Password Generator')
root.geometry("500x300")

def new_rand():
    #Clear Previously generated password
    password_entry.delete(0,END)

    pw_length=int(entry.get()) #convert to int because we will get text data 
    real_password=''
    for x in range(pw_length):
        real_password+=chr(randint(33,126))
    password_entry.insert(0,real_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

label_frame=LabelFrame(root,text="How Many Characters?")
label_frame.pack(pady=20)

entry=Entry(label_frame,font=("Halvetica",20))
entry.pack(pady=20,padx=20)

password_entry=Entry(root,text='',font=("Halvetica",20),border=0)
password_entry.pack(pady=20)

my_frame=Frame(root)
my_frame.pack(pady=20)

#Create Buttons
my_button=Button(my_frame,text='Generate Strong Password',command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame,text='Copy to Clip Board',command=clipper)
clip_button.grid(row=0,column=1,padx=10)

root.mainloop()

