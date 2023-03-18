from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


def signin():
    username=user.get()
    password=code.get()



    if username=='Alirza Shabazov' and password=='20232007':
        screen=Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.configure(bg="white")

        Label(screen,text="Prayektime Xos Gelmissiniz😊",bg='white',font=('Calibri(Body)',40,'bold') ).pack(expand=True)


    elif username != 'Alirza Shabazov' and password != '20232007':
        messagebox.showerror('Invalid','Invalid username and password')

    elif password != '20232007':
        messagebox.showerror('Invalid', 'Invalid password')
    
    elif username != "Alirza Shabazov":
      messagebox.showerror('Invalid', 'Invalid username ')


    
       




    screen.mainloop()
 



#icon
image_icon = PhotoImage(file='image/login.png')
root.iconphoto(False, image_icon)




img = PhotoImage(file='image/login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in', fg='#57a1f8',bg='white',
              font=('Microsoft YaHei UI Light', 23, 'bold'))
                

heading.place(x=100,y=5)
############## _____________________________________
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')





user = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")                                                                
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

############_____________________________________


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>',on_enter)
code.bind("<FocusOut>",on_leave)



Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

########################################################
Button(frame, width=39, pady=7, text='Sign in ', bg='#57a1f8',
       fg="white", border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))

label.place(x=75,y=270)

sign_up=Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',
fg='#57a1f8',)
sign_up.place(x=215,y=270)














root.mainloop()








