from tkinter import *
from tkinter import messagebox
import base64
from cryptography.fernet import Fernet
import os

key=Fernet.generate_key()
cipher=Fernet(key)

def Decrypt():
    password=code.get()

    if password=="1234":
        
        screen2=Toplevel(screen)
        screen2.geometry("400x200")
        screen2.title("Encryption")
        screen2.configure(bg="#ed3833") 

        message=text1.get(1.0,END)
        #decode_message=message.encode("ascii")
        #base64_bytes=base64.b64decode(decode_message)
        #decrypt=base64_bytes.decode("ascii")
        decrypt=cipher.decrypt(message).decode('utf-8')
         

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="arial",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("encryption","input errors")

    elif password!="1234":
        messagebox.shoewerror("encryption","Invalid Password")



def Encrypt():
    password=code.get()  

    if password=="1234":


        screen1=Toplevel(screen)
        screen1.geometry("400x200")
        screen1.title("Encryption")
        screen1.configure(bg="#ed3833") 

        message=text1.get(1.0,END)
        #encode_message=message.encode("ascii")
        #base64_bytes=base64.b64encode(encode_message)
        #encrypt=base64_bytes.decode("ascii") 
        encrypt=cipher.encrypt(message.encode('utf-8'))

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="arial",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","input errors")

    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")




def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("400x470")

    #icon
    image_icon=PhotoImage(file=r"C:\Users\rishi\OneDrive\Desktop\crypto2.png")
    screen.iconphoto(False,image_icon)
    screen.title("Secure Txt")

    def reset():
        code.set("")
        text1.delete(1.0,END)
        

    Label(text="Enter text for encryption and decryption",fg="black",font=("helvetica",13)).place(x=10,y=10)
    text1=Text(font="calibry",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=350,height=80)

    Label(text="Enter the key" ,fg="black",font=("helvectia",13)).place(x=10,y=170) 
    
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",20),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width="23",fg="white",bg="red",command=Encrypt).place(x=10,y=250)
    Button(text="DECRYPT",fg="white",bg="green",height="2",width="23",command=Decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,fg="white",bg="#1089ff",command=reset).place(x=10,y=300)


    screen.mainloop()

main_screen( )    
