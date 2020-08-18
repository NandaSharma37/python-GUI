from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
captchasol=False
ims=[]
imgs=[]
def verifyfn(event,soln):
        global selectedpos
        global captchasol
        if "".join(selectedpos)==soln:
            captchasol=True
            messagebox.showinfo("Succesfull", "Verified Successfully")
        else:
            captchasol=False
            msg='NOT VERIFIED,TRY AGAIN'
            msgvar=Message(window,text=msg)
            msgvar.config(bg='red')
            msgvar.place(x=0,y=200)
           # messagebox.showerror("Failed", "not Verified ")
def retryfn(event):
        global canvas
        canvas.delete('all')
        start()           
def storepos(event,position):
        global selectedpos
        global rects
        global canvas
        if(selectedpos[position]=='0'):
                selectedpos[position]='1'
                rects[position]=canvas.create_rectangle(100+72*(position%4),100+72*(position//4),170+72*(position%4),170+72*(position//4),outline='blue',width=3)
                canvas.update()
        elif(selectedpos[position]=='1'):
                selectedpos[position]='0'
                canvas.update()
                canvas.delete(rects[position])
def start():
        global ims
        global imgs
        global window
        global canvas
        global selectedpos
        global rects
        f=open('p\\captcha.txt','r')
        #ri=0
        data=f.readlines()
        ri=random.randint(0,len(data)-1)
        ques,res=data[ri].split()
        ims=[]
        imgs=[]
        selectedpos=['0']*16
        rects=['0']*16
        x,y=0,0
        canvas.create_rectangle(100,20,385,95,fill='blue',outline='blue')
        canvas.create_text(240,58,text='Select All Squares With '+ques,fill='white',font=('Lucida Handwriting',12,'bold'))
        for j in range(16):
                ims.append(PhotoImage(file='p\\'+str(ri+1)+str(j+1)+'.png'))
        for j in range(16):
                imgs.append(canvas.create_image(100+72*(j%4),100+72*(j//4),image=ims[j],anchor=NW))
        for i in range(len(imgs)):
                canvas.tag_bind(imgs[i],'<ButtonPress-1>',lambda evt,temp=i:storepos(evt,temp))
        veri=PhotoImage(file='p\\verify.png')
        verify=canvas.create_image(283,420,image=veri,anchor=NW)
        retryim=PhotoImage(file='p\\retry.png')
        retry=canvas.create_image(100,420,image=retryim,anchor=NW)
        canvas.tag_bind(verify,'<ButtonPress-1>',lambda evt,temp=res.rstrip():verifyfn(evt,temp))
        canvas.tag_bind(retry,'<ButtonPress-1>',retryfn)
        window.mainloop()



        
def new():
        def video():
                import os
                os.system("python5.mp4")
        new=Toplevel()
        new.title("python videos")
        new.geometry("1600x1350")
        w1=Label(new,text='Python is a general purpose and high level programming language.\nYou can use Python for developing desktop GUI applications, websites and web applications.\n Also, Python, as a high level programming language, allows you to focus on core functionality of the application by taking care of common programming tasks.')
        w1.place(x=0,y=0)
        Button(new,text='PLAY VIDEO',width=20,bg='brown',fg='white',command=video).place(x=75,y=75)
def new2():
        def video1():
                import os
                os.system("C:\\Users\\Lenovo\\Desktop\\java5.mp4")
         
        new1=Toplevel()
        new1.title("java videos")
        new1.geometry("1600x1350")
        w1=Label(new1,text='The Java programming language requires the presence of a software platform in order for compiled programs to be executed. \n Oracle supplies the Java platform for use with Java. \n The Android SDK is an alternative software platform, used primarily for developing Android applications with its own GUI system.')
        w1.place(x=0,y=0)

        Button(new1,text='PLAY VIDEO',width=20,bg='brown',fg='white',command=video1).place(x=75,y=75)
def new5():
        global loginpage
        root.destroy()
        loginpage()
def new2():
      import webbrowser
      
      
      root=Toplevel()
      root.geometry('1352x800')
      root.title('Application')
      root.config(bg='powderblue')
      #menu=Menu(root)
      #root.config(menu=menu)  
      #filemenu=Menu(menu)
      #menu.add_cascade(label='Back')
      def open():
              webbrowser.open("https://www.w3schools.com/python/")
      canvas=Canvas(root,width = 310,height =163,bg='powderblue')
      canvas.place(x=100,y=40)
      my_image = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\python demo\\2.png')
      canvas.create_image(0,0, anchor=NW,image=my_image)
      label_1=Label(root,text="Python is a general purpose and high level programming language.\nYou can use Python for developing desktop GUI applications, websites \nand web applications. Also, Python, as a high level programming \nlanguage, allows you to focus on core functionality of the \n application by taking care of common programming tasks.",font=("bold",10),bg='powderblue').place(x=30,y=220)
      Button(root,text='learn More',width=20,bg='brown',fg='white',command=open).place(x=160,y=320)
      Button(root,text='SIGN OUT',width=20,bg='brown',fg='white',command=new5).place(x=1200,y=0)
      def open1():
              webbrowser.open("https://www.w3schools.in/java-tutorial/intro/")
      canvas1=Canvas(root,width = 266,height =189,bg='powderblue')
      canvas1.place(x=850,y=360)
      img = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\python demo\\jav.png')
      canvas1.create_image(0,0, anchor=NW,image=img)
      label_2=Label(root,text="The Java programming language requires the presence of a software platform in order for\n compiled programs to be executed. Oracle supplies the Java platform for use with Java. The Android SDK \nis an alternative software platform, used primarily for developing Android applications with its own GUI system.",font=("bold",10),bg='powderblue').place(x=680,y=570)
      Button(root,text='learn More',width=20,bg='brown',fg='white',command=open1).place(x=910,y=630)


      canvas2=Canvas(root,width = 412,height =203)
      canvas2.place(x=750,y=60)
      im = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\python demo\\a.png')
      canvas2.create_image(0,0, anchor=NW,image=im)


      canvas3=Canvas(root,width = 300,height =168)
      canvas3.place(x=100,y=460)
      image = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\python demo\\7.png')
      canvas3.create_image(0,0, anchor=NW,image=image)


      canvas4=Canvas(root,width = 325,height =155)
      canvas4.place(x=430,y=300)
      image4 = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\python demo\\5.png')
      canvas4.create_image(0,0, anchor=NW,image=image4)
      root.mainloop()









                
def loginfn():
    global Username
    global Password
    global captchasol
    if captchasol:
        flag=True
        usr=Username.get()
        pwd=Password.get()
        f=open("users.dat",'r')
        x=f.readlines()
        print(x,len(x))
        f.close()
        for i in range(len(x)):
            uname,passw,emai,y,y,secq,seca=x[i].split('+')
            if usr==uname and pwd==passw:
                 new2()  
                 #messagebox.showinfo("Login SuccessFull", "Login SuccessFull")
                 flag=False
        if flag:
             messagebox.showerror("Error", "Invalid Id or password")
    else:
        messagebox.showerror("Error", "Please Verify  captcha")
def check():
    global var1
    if(var1.get()==1):
        global canvas
        cap()
def submit():
        global canvas
        msge='FIRST VERIFY YOU ARE HUMAN OR NOT'
        msgvar1=Message(canvas,text=msge,width=1000)
        msgvar1.config(bg='Red')
        canvas.create_window(400,400,window=msgvar1)
def RegisterLogic():
    global Username
    global Password
    global CapFlag
    global Email
    global var
    global c
    global var1
    global secvar
    global secnans
    global root
    global user
    
    usr=Username.get()
    pwd=Password.get()
    email=Email.get()
    gender=var.get()
    country=c.get()
    seq=secvar.get()
    seca=secans.get()
    if '@' in email:
        flag=0
        f=open("users.dat",'r')
        users=list(f)
        f.close()
        for i in users:
             if usr in i:
                messagebox.showerror("Validatation Error", "Username Already Exists")
                flag=1
        if flag==0:
                f=open("users.dat",'a')
                f.write(usr+'+'+pwd+'+'+email+'+'+gender+'+'+country+'+'+seq+'+'+seca+'\n')
                f.close()
                messagebox.showinfo("Registration Successful", "Registration success! You Can Now Login")
    else:
        messagebox.showerror("Validatation Error", "Incorrect Email")



def signup():
    global loginpage
    global root
    global Fullname
    global Username
    global Password
    global Email
    global secans
    global var
    global var1
    global c
    global secvar
    

    
    root.destroy()
    root=Tk()
    root.geometry('500x500')
    root.title("Sign Up")
    canvas1=Canvas(root,width=800,height=600)
    canvas1.place(x=0,y=0)
    myimage1=PhotoImage(file='b.gif')
    canvas1.create_image(0,0,anchor=NW,image=myimage1)

    var=IntVar()
    c=StringVar()
    var1=StringVar()
    
    label_0=Label(root,text="Sign Up",font=("bold",20))
    label_0.place(x=90,y=53)


    label_1=Label(root,text="User name",font=("bold",10))
    label_1.place(x=80,y=130)


    Username=Entry(root)
    Username.place(x=240,y=130)

    label_2=Label(root,text="Password",font=("bold",10))
    label_2.place(x=80,y=160)

    Password=Entry(root,show="*")
    Password.place(x=240,y=160)

    label_3=Label(root,text="Email",font=("bold",10))
    label_3.place(x=80,y=190)


    Email=Entry(root)
    Email.place(x=240,y=190)



    label_4=Label(root,text="Gender",font=("bold",10))
    label_4.place(x=80,y=230)
    

    Radiobutton(root,text="Male",padx=5, variable=var,value=1).place(x=235,y=230)
    Radiobutton(root,text="Female",padx=20, variable=var,value=2).place(x=290,y=230)

    label_5=Label(root,text="Country",font=("bold",10))
    label_5.place(x=80,y=280)


    list1=['CANADA','UK','INDIA','NEPAL','ENGLAND','USA']
    list2=['What was Your First Car?','what was your Childhood nickname?','Your Favorite Food?']
    droplist=OptionMenu(root,c,*list1)
    droplist.config(width=15)
    c.set('select your country')
    droplist.place(x=240,y=280)
    secvar=StringVar()
    droplist1=OptionMenu(root,secvar,*list2)
    droplist.config(width=15)
    secvar.set('select your Security Question')
    droplist1.place(x=50,y=330)
    label_4=Label(root,text="Answer",font=("bold",10))
    label_4.place(x=340,y=315)
    secans=Entry(root)
    secans.place(x=340,y=340)
    Button(root,text='Submit',width=20,bg='brown',fg='white',command=RegisterLogic).place(x=180,y=380)
    Button(root,text='login',width=20,bg='brown',fg='white',command=new5).place(x=180,y=430)
    root.mainloop()
def cap():
    global window
    global canvas
    global selectedpos
    global rects
    selectedpos=['0']*16
    rects=['0']*16
    window=Toplevel()
    window.title(' IMAGE CAPTCHA')
    canvas=Canvas(window,width=500,height=500)
    canvas.pack()
    canvas=Canvas(window,width = 2000,height =2000,bg='lightblue')
    canvas.place(x=0,y=0)
    ##myimage=PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\Capture1.png')
    ##canvas.create_image(0,0,anchor=NW,image=myimage
    start()
def glogin():
       global root
       root.destroy()
       loginpage()
def forglog():
    global Username
    global Password
    global email
    global secvar
    global secans
    global root
    usr=Username.get()
    pwd=Password.get()
    emails=email.get()
    if email!="" and usr!="" and pwd!="":
        flag=0
        f=open("users.dat",'r')
        users=list(f)
        f.close()
        for i in range(len(users)):
            uname,passw,emai,x,y,secq,seca=users[i].split('+')
            if usr==uname and emails.upper()==emai.upper() and secq.upper()==secvar.get().upper() and seca.upper().rstrip()==secans.get().upper():
                users[i]=uname+'+'+pwd+'+'+emails+'+'+x+'+'+y+'+'+secq+'+'+seca
                flag=1
        if flag:
             f=open("users.dat",'w')
             for i in users:
                 f.write(i)
             f.close()
             messagebox.showinfo("Successfull", "Password Reset Success ")
        else:
             messagebox.showerror("Error", "Invalid username or Security Question")
    else:
         messagebox.showerror("Error", "Empty Enrties")

def forgotpage():
    global root
    global Username
    global Password
    global email
    global var1
    global secvar
    global secans
    root.destroy()
    root=Tk()
    root.geometry('600x500')
    root.title("Forgot Form")
   
    canvas1=Canvas(root,width=800,height=600)
    canvas1.place(x=0,y=0)
    myimage1=PhotoImage(file='b.gif')
    canvas1.create_image(0,0,anchor=NW,image=myimage1)
    Username=StringVar()
    Password=StringVar()
    email=StringVar()
    #Email=StringVar()
    var=IntVar()
    c=StringVar()
    var1=IntVar()

    label_0=Label(root,text="forgot Form",font=("bold",20))
    label_0.place(x=90,y=53)

    label_1=Label(root,text="User Name",font=("bold",10))
    label_1.place(x=80,y=140)
    entry_1=Entry(root,textvar=Username)
    entry_1.place(x=240,y=140)
    label_2=Label(root,text="Password",font=("bold",10))
    label_2.place(x=68,y=190)
    entry_2=Entry(root,textvar=Password,show='*')
    entry_2.place(x=240,y=190)
    label_2=Label(root,text="Email for verification",font=("bold",10))
    label_2.place(x=68,y=230)
    entry_2=Entry(root,textvar=email)
    entry_2.place(x=240,y=230)
    list2=['What was Your First Car?','what was your Childhood nickname?','Your Favorite Food?']
    secvar=StringVar()
    droplist1=OptionMenu(root,secvar,*list2)
    secvar.set('select your Security Question')
    droplist1.place(x=50,y=285)
    label_4=Label(root,text="Answer",font=("bold",10))
    label_4.place(x=340,y=270)
    secans=Entry(root)
    secans.place(x=340,y=290)

    Button(root,text='reset',width=20,bg='brown',fg='white',command=forglog).place(x=180,y=320)
    Button(root,text='login',width=20,bg='brown',fg='white',command=glogin).place(x=180,y=360)
    root.mainloop()
     
def loginpage():
    global root
    global Username
    global Password
    global var1
    root=Tk()
    root.geometry('1600x1400')
    root.title("Login Form")
    canvas=Canvas(root,width = 2000,height =2000,bg='lightblue')
    canvas.place(x=0,y=0)
    canvas1=Canvas(root,width = 266,height =189,bg='powderblue')
    canvas1.place(x=850,y=30)
    
    img = PhotoImage(file='C:\\Users\\nanda sharma\\Desktop\\python final\\jav.png')
    canvas1.create_image(0,0, anchor=NW,image=img)
    canvas1=Canvas(root,width = 266,height =155,bg='powderblue')
    canvas1.place(x=10,y=450)
    
    img1 = PhotoImage(file='C:\\Users\\nanda sharma\\Desktop\\python final\\5.png')
    canvas1.create_image(0,0, anchor=NW,image=img1)
    canvas1=Canvas(root,width = 500,height =305,bg='powderblue')
    canvas1.place(x=750,y=350)
    
    img2 = PhotoImage(file='C:\\Users\\nanda sharma\\Desktop\\python final\\a.png')
    canvas1.create_image(0,0, anchor=NW,image=img2)
   
    canvas1=Canvas(root,width=600,height=400)
    canvas1.place(x=0,y=0)
    myimage1=PhotoImage(file='b.gif')
    canvas1.create_image(0,0,anchor=NW,image=myimage1)
    Username=StringVar()
    Password=StringVar()
    
    #Email=StringVar()
    var=IntVar()
    c=StringVar()
    var1=IntVar()

    label_0=Label(root,text="Login Form",font=("bold",20))
    label_0.place(x=90,y=53)


    label_1=Label(root,text="User Name",font=("bold",10))
    label_1.place(x=80,y=140)


    entry_1=Entry(root,textvar=Username)
    entry_1.place(x=240,y=140)

    label_2=Label(root,text="Password",font=("bold",10))
    label_2.place(x=80,y=190)

    entry_2=Entry(root,textvar=Password,show='*')
    entry_2.place(x=240,y=190)
    entry_2=Entry(root,textvar=Password,show='*')
    entry_2.place(x=240,y=190)



    
    canvas=Canvas(root,width=220,height=50)
    canvas.place(x=235,y=220)
    myimage=PhotoImage(file='p\\capt.gif')
    canvas.create_image(0,0,anchor=NW,image=myimage)
    cb1=Checkbutton(canvas,text='',variable=var1,command=check)
    canvas.create_window(20,25,window=cb1)
    Button(root,text='Login',width=20,bg='brown',fg='white',command=loginfn).place(x=180,y=280)
    Button(root,text='Sign Up',width=20,bg='brown',fg='white',command=signup).place(x=180,y=320)
    Button(root,text='Forgot Password',width=20,bg='brown',fg='white',command=forgotpage).place(x=180,y=360)
    root.mainloop()
loginpage()
