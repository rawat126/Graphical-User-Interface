from tkinter import *
import sqlite3 as sq
from tkinter import messagebox
import scrolling_area
import random
import re
import webbrowser
import os
# can implement reguler expressions....

def video():
    os.system('yuo.mp4')
    
def home():
    foot=Frame(root,height=1080,width=1000)
    foot.place(x=0,y=0)
    img=PhotoImage(file='ui.gif')
    lb=Label(foot,image=img)
    lb.image=img
    lb.pack(expand=True)
    b1=Button(foot,text=" Explore.....",command=lambda:explore(root,foot),font=('times',17,'italic'),bg='#EAF1F6',fg='#342D2D')
    b1.place(x=45,y=30)
    b2=Button(foot,text="Reder's Login or Sign Up",command=lambda:reder(root,foot),font=('times',17,'italic'),bg='#EAF1F6',fg='#342D2D')
    b2.place(x=45,y=90) 
    b3=Button(foot,text=" Author's Login",font=('times',17,'italic'),command=lambda:member(root,foot),bg='#EAF1F6',fg='#342D2D')
    b3.place(x=45,y=150)
    b4=Button(foot,text='About us',font=('times',17,'italic'),command=lambda:about(root,foot),bg='#A7DBE1',fg='#342D2D')
    b4.place(x=45,y=543)
    b4=Button(foot,text='@Contact',font=('times',17,'italic'),command=lambda:contact(root,foot),bg='#A7DBE1',fg='#342D2D')
    b4.place(x=45,y=605)
    b5=Button(foot,text='Help...?   ',font=('times',17,'italic'),command=lambda:helpp(root,foot),bg='#A7DBE1',fg='#342D2D')
    b5.place(x=45,y=664)
    
def rules(foot,root):
        foot.destroy()
        foot61=Frame(root,width=1080,height=1000)
        foot61.place(x=0,y=0)
        img=PhotoImage(file='poi.png')
        lb=Label(foot61,image=img)
        lb.image=img
        lb.place(x=470,y=30)
        lab=Label(foot61,text='L',font=('times',47,'italic'),fg='brown')
        lab.place(x=5,y=5)
        lab1=Label(foot61,text=''' Listen To the Librarian''',font=('times',17,'italic'),fg='brown')
        lab1.place(x=27,y=65)
        lab2=Label(foot61,text='I',font=('times',47,'italic'),fg='brown')
        lab2.place(x=5,y=85)
        lab3=Label(foot61,text=''' Inquire(ask) if you need help''',font=('times',17,'italic'),fg='brown')
        lab3.place(x=27,y=145)
        lab4=Label(foot61,text='B',font=('times',47,'italic'),fg='brown')
        lab4.place(x=5,y=175)
        lab5=Label(foot61,text=''' Be Respectful of Others''',font=('times',17,'italic'),fg='brown')
        lab5.place(x=27,y=235)
        lab6=Label(foot61,text='R',font=('times',47,'italic'),fg='brown')
        lab6.place(x=5,y=265)
        lab7=Label(foot61,text=''' Read and Talk Quietly''',font=('times',17,'italic'),fg='brown')
        lab7.place(x=27,y=335)
        lab8=Label(foot61,text='A',font=('times',47,'italic'),fg='brown')
        lab8.place(x=5,y=365)
        lab9=Label(foot61,text=''' Always Walk Never Run''',font=('times',17,'italic'),fg='brown')
        lab9.place(x=27,y=425)
        lab10=Label(foot61,text='R',font=('times',47,'italic'),fg='brown')
        lab10.place(x=5,y=455)
        lab11=Label(foot61,text=''' Return Books to their Proper Places''',font=('times',17,'italic'),fg='brown')
        lab11.place(x=27,y=515)
        lab12=Label(foot61,text='Y',font=('times',47,'italic'),fg='brown')
        lab12.place(x=5,y=545)
        lab13=Label(foot61,text=''' Your Manners and Cooperation are Appreciated''',font=('times',17,'italic'),fg='brown')
        lab13.place(x=27,y=605)
        b1=Button(foot61,text='Back',font=('times',17,'italic'),command=lambda:back(foot61,x=5),bg='#F29721',fg='white')
        b1.place(x=880,y=670)
        

def database(foot,e1,e2,e3):
    a=e1.get()
    b=e2.get()
    c=e3.get()
    
    if(a=='' or b=='' or c==''):
        messagebox.showinfo('Title','INCOMPLETE INFORMATION...')
    else:
        con=sq.connect('data.db')
        #con.execute('Create table books (Books INTVAR,Author INTVAR,Catagory INTVAR)')
        con.execute('Insert into books Values (?,?,?)',(a,b,c))
        con.commit()
        messagebox.showinfo('Title','SUCESSFULLY ADDED...')
    
def guide(foot1,root):
    def call(url):
        webbrowser.open_new(url)
    
    foot1.destroy()
    foot51=Frame(root,height=1080,width=1000)
    foot51.pack(expand=True)
    img=PhotoImage(file='lsk.gif')
    lb=Label(foot51,image=img)
    lb.image=img
    img1=PhotoImage(file='rz.gif')
    lb=Label(foot51,image=img1)
    lb.image=img1
    lb.place(x=0,y=70)
    lb1=Label(foot51,text="Here's Our Map.......",font=('times',32,'italic'),fg='brown',borderwidth=0)
    lb1.place(x=300,y=0)
    lb2=Label(foot51,text="We Hope This Will Guide You Correctly.......",font=('times',22,'italic'),fg='brown',borderwidth=0)
    lb2.place(x=20,y=673)
    b1=Button(foot51,text='Back',font=('times',17,'italic'),command=lambda:back(foot51,x=5),bg='#F29721',fg='white')
    b1.place(x=880,y=670)
    b2=Button(foot51,text='LIVE LOCTION...',font=('times',17,'italic'),bg='#F29721',fg='white')
    b2.place(x=799,y=70)
    b2.bind('<Button-1>',lambda e:call('https://www.google.com/maps/place/zeetron+networks+pvt+ltd/@26.8576382,75.793291,17z/data=!3m1!4b1!4m5!3m4!1s0x396dca1fe060d4c1:0xfc8dbfb03fe6fc33!8m2!3d26.8576334!4d75.7954797'))

def search(foot1,root,a):
    con=sq.connect('data.db')
    com=con.execute('Select * from books where Books="%s"'%a)
    our=com.fetchall()
    con.commit()

    if(our==[]):
        lb=Label(foot1,font=('times',21,'italic'),text='        No Such Book Found.......      ',bg='black',fg='lightgray',)
        lb.place(x=300,y=500)

    else:    
        foot1.destroy()
        foot11=Frame(root,height=1080,width=1000)
        foot11.pack(expand=True)
        if(a!='Shiva Trilogy'):  

            im=PhotoImage(file='ytr.gif')
            lab=Label(foot11,image=im)
            lab.image=im
            lab.pack(expand=True)
            la=Label(foot11,text='  We Found Them........ ',font=('times',37,'italic'),fg='#1A1A19',bg='lightgray')
            la.place(x=150,y=1)
        else:
            im=PhotoImage(file='uy.gif')
            lab=Label(foot11,image=im)
            lab.image=im
            lab.pack(expand=True)
            la=Label(foot11,text='   Our BestSellers........   ',font=('times',37,'italic'),fg='#507D7A',bg='lightgray')
            la.place(x=150,y=1)
        scl=scrolling_area.Scrolling_Area(foot11,height=300,width=7500)
        scl.place(x=150,y=67)
        table=scrolling_area.Table(scl.innerframe,
                                   ['BOOK','AUTHOR','CATAGORY'],
                                   column_minwidths=[222,222,222]
                                   )
        
        table.pack(expand=True,fill=X)
        table.on_change_data(scl.update_viewport)
        b2=Button(foot11,text='Back',font=('times',17,'italic'),command=lambda:back(foot11,x=5),bg='#AFB8BA',fg='white')
        b2.place(x=80,y=670)
        com=con.execute('Select * from books where Books="%s"'%a)
        data=[]
        for row in com:
            column=[]
            data.append(column)
            for r in row:
                print(r)
                column.append(r)
        table.set_data(data)
        
def card(foot1,root):                
    def click(e):
        if(e1.get()==''):
            messagebox.showinfo('Title','Plese Enter The Name')
        else:    
            img=PhotoImage(file='rt.gif')
            lb=Label(foot41,image=img)
            lb.image=img
            lb.place(x=320,y=400)
            lb1=Label(foot41,text='''Name : "%s"'''%e1.get(),width=22,font=('times',20),bg='#B08C67',fg='black')
            lb1.place(x=337,y=583)
            random.seed(e1.get())
            num=random.randint(1000,100000)
            #lb2=Label(foot41,text='    Here is Your ID No. :  %d    '%num,height=2,font=('times',18,'bold'),bg='#B5D6EF',fg='black')
            #lb2.place(x=109,y=510)
            lb3=Label(foot41,text='ID NO.  :  %d'%num,height=2,width=14,font=('times',18,'bold'),bg='#B08C67',fg='black')
            lb3.place(x=471,y=510)

    foot1.destroy()
    foot41=Frame(root,height=1080,width=1000)
    foot41.place(x=0,y=0)
    img1=PhotoImage(file='iop.gif')
    lb=Label(foot41,image=img1)
    lb.image=img1
    lb.pack(expand=True)
    l1=Label(foot41,text='Your Name...   ',font=('arial',17),bg='gray',fg='black')
    l1.place(x=50,y=150)
    e1=Entry(foot41,font=('times',17),bd=5,width=40)
    e1.place(x=290,y=153)
    b1=Button(foot41,text='                                          Generate............                                  ',font=('arial',17),bg='lightgray',fg='black')
    b1.place(x=150,y=250)
    b1.bind('<Button-1>',click)
    b2=Button(foot41,text='Back',font=('times',17,'italic'),command=lambda:back(foot41,x=5),bg='#DECAAD',fg='white')
    b2.place(x=880,y=670)    


def add(foot32,root,enum1,enum2,y):
    print(enum1,enum2)
    def back1(foot,x):    
        if(x==4):
            show_mem(foot,enum1,enum2)
        if(x==6):
            show_red(foot,enum1,enum2)      
    foot32.destroy()
    foot321=Frame(root,height=1080,width=1000)
    foot321.config(bg='#FEF4E4')
    foot321.pack(expand=True)
    if(y==2):
        ig=PhotoImage(file='lsk.gif')
        lb=Label(foot321,image=ig)
        lb.image=ig
        lb.pack(expand=True)
        lb3=Label(foot321,text=''' NOTE : You Can't Issue More than 3 Books.....''',font=('times',22),bg='lightgray',fg='brown')
        lb3.place(x=200,y=470)
    lb1=Label(foot321,text='Book Name...',font=('times',17),bg='#F29721',fg='white')
    lb1.place(x=80,y=90)
    lb2=Label(foot321,text='Author Name...',font=('times',17),bg='#F29721',fg='white')
    lb2.place(x=380,y=90)
    e1=Entry(foot321,font=('arial',17),bd=5)
    e1.place(x=70,y=145)
    e2=Entry(foot321,font=('arial',17),bd=5)
    e2.place(x=370,y=145)
    if(y==1):
        var=StringVar(foot321)
        var.set('None')
        e3=OptionMenu(foot321,var,'None','Literature','Technology','Fiction','Youth','Teens','Kids','Religious','sports','Adventure','Mangement','Civil','Series')
        e3.config(font=('times',13,'bold'),bd=5,width=15,bg='#FEE5C4',fg='white')
        e3.place(x=700,y=141)
        b2=Button(foot321,text='           ADD            ',font=('times',15,'italic'),command=lambda:database(foot321,e1,e2,var),bg='#F29721',fg='white')
        b2.place(x=730,y=220)
        b1=Button(foot321,text='Back',font=('times',17,'italic'),command=lambda:back1(foot321,x=4),bg='#F29721',fg='white')
        b1.place(x=30,y=670)
        lb3=Label(foot321,text='Catagory...',font=('times',17),bg='#F29721',fg='white')
        lb3.place(x=720,y=90)
        b=Button(foot321,text='Logout...',font=('times',17,'italic'),command=lambda:back(foot321,x=3),fg='white',bg='#F29721')
        b.place(x=857,y=3)
    if(y==2):
        b2=Button(foot321,text='           ISSUE           ',font=('times',15,'italic'),command=lambda:database(foot321,e1,e2,e3),bg='#F29721',fg='white')
        b2.place(x=730,y=220)
        b1=Button(foot321,text='Back',font=('times',17,'italic'),command=lambda:back1(foot321,x=6),bg='#F29721',fg='white')
        b1.place(x=30,y=670)
        b=Button(foot321,text='Logout...',font=('times',17,'italic'),command=lambda:back(foot321,x=2),fg='white',bg='#F29721')
        b.place(x=857,y=3)
    
def back(foot,x):
    foot.destroy()
    if(x==1):
        home()
    if(x==2):
        reder(root,foot)
    if(x==3):
        member(root,foot)
    if(x==5):    
        explore(root,foot)
    
        
def show_red(foot,e1,e2,z=0):
    def Logout(e):
        member(root,foot22)
        messagebox.showinfo('Title','Logout Sucess...')
    a=e1
    b=e2

    if(a=='' or b==''):
            messagebox.showinfo('Title','INCOMPLETE INFORMATION...')
    else:
            
        con=sq.connect('data_reder.db')
        cor=con.execute('select name,books,date from books_reder where name = "%s"'%a)
        pas=con.execute('select Password from books_reder where name="%s"' %a)  
        word=str(pas.fetchall()[0][0])
        con.commit()
             
        if(word!=b):
            messagebox.showinfo('Title','INVALID USERNAME OR PASSWORD...')   
        else:    
            if(z==2):
                messagebox.showinfo('Title','LOGIN SUCESS...')
            foot.destroy()
            foot22=Frame(root,height=1080,width=1000,bg='#FEE5C4')
            foot22.place(x=0,y=0)
            img=PhotoImage(file='iop.gif')
            lab=Label(foot22,image=img)
            lab.image=img
            lab.pack(expand=True)
            lab1=Label(foot22,text='YOUR BOOKS.....',font=('times',22,'italic'))
            lab1.place(x=140,y=0)
            scl=scrolling_area.Scrolling_Area(foot22,height=300,width=1500)
            scl.place(x=150,y=50)
            table=scrolling_area.Table(scl.innerframe,
                        ['CANDIDATE NAME','ISSUED BOOKS','DATE OF EXPIRE'],
                         column_minwidths=[222,222,222]
                        )

            #table=scrolling_area.Table(scl.innerframe,
            #           ['NAME','DOB','MOB NO.','CATAGORY','EMAIL','QUALIFICATION','ADDRESS','BOOKS'],
            #           column_minwidths=[152,122,122,222,222,222]
            #         )
            table.pack(expand=True,fill=X)
            table.on_change_data(scl.update_viewport)
            cor=con.execute('select name,books,date from books_reder where name = "%s"'%a)
            b=Button(foot22,text='                     Issue a new Book.....                ',font=('times',17,'italic'),command=lambda:add(foot22,root,e1,e2,y=2),fg='black',bg='lightgray')
            b.place(x=220,y=500)
            data = []
            for row in cor:
                column = []
                data.append(column)
                for r in row:
                    print(r)
                    column.append(r)

            table.set_data(data)
            
            b1=Button(foot22,text='Logout...',font=('times',19,'italic'),command=lambda:back(foot22,x=2),bg='#A7DBE1',fg='black')
            b1.bind('<Button-1>',Logout)
            b1.place(x=30,y=650)
             

def show_mem(foot2,e1,e2,z=0):
    def Logout(e):
        member(root,foot32)
        messagebox.showinfo('Title','Logout Sucess...')
    a=e1
    b=e2

    if(a=='' or b==''):
            messagebox.showinfo('Title','INCOMPLETE INFORMATION...')
    else:
            
        con=sq.connect('data_aut.db')
        cor=con.execute('select name,books,catagory from books_aut where name = "%s"'%a)
        pas=con.execute('select Password from books_aut where name="%s"' %a)
        word=str(pas.fetchall()[1][0])
        print(pas.fetchall())
        con.commit()
                
        if(word!=b):
            messagebox.showinfo('Title','INVALID USERNAME OR PASSWORD...')       
        else:
            if(z==1):
                messagebox.showinfo('Title','LOGIN SUCESS...')
            foot2.destroy()
            foot32=Frame(root,height=1080,width=1000)
            foot32.place(x=0,y=0)
            im=PhotoImage(file='ytr.gif')
            lab=Label(foot32,image=im)
            lab.image=im
            lab.pack(expand=True)
            scl=scrolling_area.Scrolling_Area(foot32,height=420,width=800)
            scl.place(x=120,y=5)
            table=scrolling_area.Table(scl.innerframe,
                        ['NAME','BOOKS','CATAGORY'],
                         column_minwidths=[222,222,222]
                        )

            #table=scrolling_area.Table(scl.innerframe,
            #           ['NAME','DOB','MOB NO.','CATAGORY','EMAIL','QUALIFICATION','ADDRESS','BOOKS'],
            #           column_minwidths=[152,122,122,222,222,222]
            #         )
            table.pack(expand=True,fill=X)
            table.on_change_data(scl.update_viewport)
            data = []
            for row in cor:
                column = []
                data.append(column)
                for r in row:
                    print(r)
                    column.append(r)

            table.set_data(data)
            b=Button(foot32,text='                          Add a new Book.....                    ',font=('times',17,'italic'),command=lambda:add(foot32,root,e1,e2,y=1),fg='black',bg='lightgray')
            b.place(x=200,y=500)
            b1=Button(foot32,text='Logout...',font=('times',19,'italic'),command=lambda:back(foot32,x=3),bg='#A7DBE1',fg='black')
            b1.bind('<Button-1>',Logout)
            b1.place(x=30,y=650)
                

def submit_aut(foot31,e1,e2,e3,e4,e5,e6,e7,e8,e9):
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    f=e6.get()
    g=e7.get()
    h=e8.get()
    i=e9.get()
    
    if(a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h=='' or i==''):
        messagebox.showinfo('Title','INCOMPLETE INFORMATION...')
    else:
        messagebox.showinfo('Title','SUCESSFULLY DONE...')
        conn=sq.connect('data_aut.db')
        #conn.execute('Create Table books_aut (Name TEXT,Password INTVAR,DOB INTVAR,Mob_no INTVAR,Catagory INTVAR,Email INTVAR,Qualification INTVAR,Address INTVAR,books TEXT)')        
        conn.execute('Insert into books_aut Values(?,?,?,?,?,?,?,?,?)',(a,b,c,d,e,f,g,h,i))
        conn.commit()
         

def submit_reder(foot21,e1,e2,e3,e4,e5,e6,e7,e8):
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    f=e6.get()
    g=e7.get()
    h=e8.get()
    
    if(a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h==''):
        messagebox.showinfo('Title','INCOMPLETE INFORMATION...')
    else:
        messagebox.showinfo('Title','SUCESSFULLY DONE...')
        conn=sq.connect('data_reder.db')
        #conn.execute('Create Table books_reder (Name TEXT,Password INTVAR,Books INTVAR,Date INTVAR,DOB INTVAR,Mob_no INTVAR,Email INTVAR,Address INTVAR)')        
        conn.execute('Insert into books_reder Values(?,?,?,?,?,?,?,?)',(a,b,c,d,e,f,g,h))
        conn.commit()
        
def explore(root,foot):
    def enter(e):
        if(b):
            e1=Entry(foot1,font=('times',19),bd=5)
            e1.place(x=630,y=70)
            ig=PhotoImage(file='gh.gif')
            lab=Label(foot1,image=ig)
            lab.image=ig
            lab.place(x=592,y=72)
            bu=Button(foot1,text='SEARCH',command=lambda:search(foot1,root,e1.get()),height=2,font=('times',10),bg='lightgray')
            bu.place(x=878,y=72)
    
    foot.destroy()
    foot1=Frame(root,height=1080,width=1000)      
    foot1.place(x=0,y=0)
    img1=PhotoImage(file='21.gif')
    lb1=Label(foot1,image=img1)
    lb1.image=img1
    lb1.pack(expand=True)
    b=Button(foot1,text='Search a Book......',font=('times',17,'italic'),bg='#E0FBD2',fg='black' )
    b.bind('<Button-1>',enter)
    b.place(x=100,y=60)
    b1=Button(foot1,text='Back',font=('times',17,'italic'),command=lambda:back(foot1,x=1),bg='#A7DBE1',fg='black')
    b1.place(x=30,y=650)
    b2=Button(foot1,text="What's New...",font=('times',17,'italic'),fg='black',bg='#E0FBD2')
    b2.place(x=100,y=120)
    b3=Button(foot1,text="Best Seller...",font=('times',17,'italic'),command=lambda:search(foot1,root,a='Shiva Trilogy'),fg='black',bg='#E0FBD2')
    b3.place(x=100,y=180)
    b4=Button(foot1,text="Library Rules",font=('times',17,'italic'),command=lambda:rules(foot1,root),fg='black',bg='#E0FBD2')
    b4.place(x=100,y=240)
    b5=Button(foot1,text='Library Card',font=('times',17,'italic'),command=lambda:card(foot1,root),fg='black',bg='#E0FBD2')
    b5.place(x=100,y=300)
    b6=Button(foot1,text='Guide you',font=('times',17,'italic'),command=lambda:guide(foot1,root),fg='black',bg='#E0FBD2')
    b6.place(x=100,y=360)
    
    
    #back1

def reder(root,foot):
    foot.destroy()
    foot2=Frame(root,height=1080,width=1000)
    foot2.place(x=0,y=0)
    img1=PhotoImage(file='typ.gif')
    lb1=Label(foot2,image=img1)
    lb1.image=img1
    lb1.pack(expand=True)
    b1=Button(foot2,text='Back',font=('times',17,'italic'),command=lambda:back(foot2,x=1),bg='black',fg='white')
    b1.place(x=30,y=650)
    lb2=Label(foot2,text='Username',font=('times',20,),bg='black',fg='white')
    lb2.place(x=40,y=110)
    lb3=Label(foot2,text='Password ',font=('times',20,),bg='black',fg='white')
    lb3.place(x=40,y=167)
    e1=Entry(foot2,font=('Arial',18),bd=5)
    e1.place(x=200,y=110)
    e2=Entry(foot2,font=('Arial',18),bd=5)
    e2.place(x=200,y=165)
    e2.config(show='*')
    b3=Button(foot2,text='Forgot Password',font=('times',10,'underline'),bg='black',fg='white')
    b3.place(x=70,y=219)
    b4=Button(foot2,text='Login',font=('times',12),bg='black',command=lambda:show_red(foot2,e1.get(),e2.get(),z=2),fg='white')
    b4.place(x=445,y=219)
    b5=Button(foot2,text='             Sign Up by Creating Account =>>             ',font=('times',17,'bold'),bg='black',command=lambda:new(foot2,root),fg='white')
    b5.place(x=135,y=359)
    
    #back2
        
def new(foot2,root):
    #regular expressions
    def name(e):
        if(e1.get()!=''):
            p1=re.search('[A-Z,a-z]{1,50}',e1.get())
            if not p1:
                messagebox.showinfo('title','Invalid format...')
    def password(e):
        if(e2.get()!=''):
            p2=re.search('[A-Z,a-z]{1,8}[\d]{1,5}',e2.get())
            if not p2:
                messagebox.showinfo('title','Invalid format...')
    def date(e):
        if(e4.get()!=''):
            p3=re.search('[\d]{1,2}\/[\d]{1,12}\/[\d]{4}',e4.get())
            if not p3:
                messagebox.showinfo('title','Invalid format...')
    def dob(e):
        if(e5.get()!=''):
            p6=re.search('[\d]{1,2}\/[\d]{1,12}\/[\d]{4}',e5.get())
            if not p6:
                messagebox.showinfo('title','Invalid format...')        
    def on(e):
        if(e7.get()!=''):
            p4=re.search('[A-Z,a-z]{1,50}[\d]{1,20}@[A-Z,a-z]{1,15}\.[A-Z,a-z]{1,10}',e7.get())
            if not p4:
                messagebox.showinfo('title','Invalid format...')
    def mob(e):
        if(e6.get()!=''):
            p5=re.search('[\d]{1,10}',e6.get())
            if not p5:
                messagebox.showinfo('title','Invalid format...') 

    foot2.destroy()
    foot21=Frame(root,height=1080,width=1000)
    foot21.place(x=0,y=0)
    img=PhotoImage(file='poi.gif')
    lb=Label(foot21,image=img)
    lb.image=img
    lb.pack(expand=True)
    lb1=Label(foot21,text='CREATE ACCOUNT.....',font=('arial',37),fg='black')
    lb1.place(x=30,y=30)
    lb2=Label(foot21,text='Name',font=('arial',15),fg='black')
    lb2.place(x=30,y=120)
    lb3=Label(foot21,text='Password',font=('arial',15),fg='black')
    lb3.place(x=30,y=170)
    lb7=Label(foot21,text='Books',font=('arial',15),fg='black')
    lb7.place(x=30,y=220)
    lb8=Label(foot21,text='Date',font=('arial',15),fg='black')
    lb8.place(x=30,y=270)
    lb9=Label(foot21,text='DOB',font=('arial',15),fg='black')
    lb9.place(x=30,y=320)
    lb6=Label(foot21,text='Mob No.',font=('arial',15),fg='black')
    lb6.place(x=30,y=370)
    lb4=Label(foot21,text='Email',font=('arial',15),fg='black')
    lb4.place(x=30,y=420)
    lb5=Label(foot21,text='Address',font=('arial',15),fg='black')
    lb5.place(x=30,y=470)
    #lb6=Label(foot21,text='Gender',font=('arial',15),fg='black')
    #lb6.place(x=30,y=373)
    e1=Entry(foot21,font=('arial',15),bd=5)
    e1.place(x=200,y=123)
    e1.bind('<Leave>',name)
    e2=Entry(foot21,font=('arial',15),bd=5)
    e2.place(x=200,y=169)
    e2.bind('<Leave>',password)
    e3=Entry(foot21,font=('arial',15),bd=5)
    e3.place(x=200,y=220)
    e3.bind('<Leave>',name)
    e4=Entry(foot21,font=('arial',15),bd=5)
    e4.place(x=200,y=270)
    e4.bind('<Leave>',date)
    e5=Entry(foot21,font=('arial',15),bd=5)
    e5.place(x=200,y=320)
    e5.bind('<Leave>',dob)
    e6=Entry(foot21,font=('arial',15),bd=5)
    e6.place(x=200,y=370)
    e6.bind('<Leave>',mob)
    e7=Entry(foot21,font=('arial',15),bd=5)
    e7.place(x=200,y=420)
    e7.bind('<Leave>',on)
    e8=Entry(foot21,font=('arial',15),bd=5)
    e8.place(x=200,y=470)
    #e6=Radiobutton(foot21,text='Male',font=('arial',17),variable)
    #e6.place(x=210,y=370)
    #e7=Radiobutton(foot21,text='Female',font=('arial',17))
    #e7.place(x=310,y=371)
    b1=Button(foot21,text='Sign Up',font=('arial',17),command=lambda:submit_reder(foot21,e1,e2,e3,e4,e5,e6,e7,e8))
    b1.place(x=450,y=470)
    #b1.bind('<Button-1>',on)
    #b1.bind('<Button-1>',mob)
    b2=Button(foot21,text='Back',font=('arial',17),command=lambda:back(foot21,x=2))
    b2.place(x=80,y=670)
    
    

def new1(foot3,root):
    def name(e):
        if(e1.get()!=''):
            p1=re.search('[A-Z,a-z]{1,50}',e1.get())
            if not p1:
                messagebox.showinfo('title','Invalid format...')
    def password(e):
        if(e2.get()!=''):
            p2=re.search('[A-Z,a-z]{1,8}[\d]{1,5}',e2.get())
            if not p2:
                messagebox.showinfo('title','Invalid format...')
    def date(e):
        if(e4.get()!=''):
            p3=re.search('[\d]{1,2}\/[\d]{1,12}\/[\d]{4}',e4.get())
            if not p3:
                messagebox.showinfo('title','Invalid format...')
    def dob(e):
        if(e3.get()!=''):
            p6=re.search('[\d]{1,2}\/[\d]{1,12}\/[\d]{4}',e3.get())
            if not p6:
                messagebox.showinfo('title','Invalid format...')        
    def on(e):
        if(e6.get()!=''):
            p4=re.search('[A-Z,a-z]{1,50}[\d]{1,20}@[A-Z,a-z]{1,15}\.[A-Z,a-z]{1,10}',e6.get())
            if not p4:
                messagebox.showinfo('title','Invalid format...')
    def mob(e):
        if(e5.get()!=''):
            p5=re.search('[\d]{1,10}',e5.get())
            if not p5:
                messagebox.showinfo('title','Invalid format...')
    foot3.destroy()
    foot31=Frame(root,height=1080,width=1000)
    foot31.place(x=0,y=0)
    img=PhotoImage(file='poi.gif')
    lb=Label(foot31,image=img)
    lb.image=img
    lb.pack(expand=True)
    lb1=Label(foot31,text='CREATE ACCOUNT.....',font=('times',37),fg='black')
    lb1.place(x=30,y=30)
    lb2=Label(foot31,text='Name',font=('arial',15),fg='black')
    lb2.place(x=30,y=120)
    lb3=Label(foot31,text='Password',font=('arial',15),fg='black')
    lb3.place(x=30,y=170)
    lb6=Label(foot31,text='DOB',font=('arial',15),fg='black')
    lb6.place(x=30,y=220)
    lb6=Label(foot31,text='Catagory',font=('arial',15),fg='black')
    lb6.place(x=30,y=270)
    lb4=Label(foot31,text='Mob No.',font=('arial',15),fg='black')
    lb4.place(x=30,y=320)
    lb7=Label(foot31,text='Email',font=('arial',15),fg='black')
    lb7.place(x=30,y=373)
    lb8=Label(foot31,text='Books',font=('arial',15),fg='black')
    lb8.place(x=30,y=423)
    lb5=Label(foot31,text='Qualification',font=('arial',15),fg='black')
    lb5.place(x=30,y=473)
    #lb6=Label(foot31,text='Gender',font=('arial',15),fg='black')
    #lb6.place(x=30,y=433)
    lb6=Label(foot31,text='Address',font=('arial',15),fg='black')
    lb6.place(x=30,y=530)
    e1=Entry(foot31,font=('arial',15),bd=5)
    e1.bind('<Leave>',name)
    e1.place(x=200,y=123)
    e2=Entry(foot31,font=('arial',15),bd=5)
    e2.bind('<Leave>',password)
    e2.place(x=200,y=169)
    e3=Entry(foot31,font=('arial',15),bd=5)
    e3.bind('<Leave>',dob)
    e3.place(x=200,y=220)
    e4=Entry(foot31,font=('arial',15),bd=5)
    e4.bind('<Leave>',name)
    e4.place(x=200,y=270)
    e5=Entry(foot31,font=('arial',15),bd=5)
    e5.bind('<Leave>',mob)
    e5.place(x=200,y=320)
    #e6=Radiobutton(foot31,text='Male',font=('arial',17),variable)
    #e6.place(x=210,y=370)
    #e7=Radiobutton(foot31,text='Female',font=('arial',17))
    #e7.place(x=310,y=371)
    e6=Entry(foot31,font=('arial',15),bd=5)
    e6.bind('<Leave>',on)
    e6.place(x=200,y=370)
    e7=Entry(foot31,font=('arial',15),bd=5)
    e7.bind('<Leave>',name)
    e7.place(
        x=200,y=420)
    e8=Entry(foot31,font=('arial',15),bd=5)
    e8.place(x=200,y=470)
    e9=Entry(foot31,font=('arial',15),bd=5)
    e9.place(x=200,y=530)
    b1=Button(foot31,text='Sign Up',font=('arial',17),command=lambda:submit_aut(foot31,e1,e2,e3,e4,e5,e6,e7,e8,e9))
    b1.place(x=450,y=530)
    b2=Button(foot31,text='Back',font=('arial',17),command=lambda:back(foot31,x=3))
    b2.place(x=80,y=670)
    
    
    
def member(root,foot):
    foot.destroy()
    foot3=Frame(root,height=1080,width=1000)
    foot3.place(x=0,y=0)
    img1=PhotoImage(file='book.gif')
    lb1=Label(foot3,image=img1)
    lb1.image=img1
    lb1.pack(expand=True)
    b1=Button(foot3,text='Back',font=('times',17,'italic'),command=lambda:back(foot3,x=1),bg='#A7DBE1',fg='black')
    b1.place(x=30,y=650)
    lb2=Label(foot3,text='Username',font=('times',20),bg='lightgray',fg='black')
    lb2.place(x=80,y=80)
    lb3=Label(foot3,text='Password ',font=('times',20),bg='lightgray',fg='black')
    lb3.place(x=80,y=140)
    e1=Entry(foot3,font=('times',19),bd=5)
    e1.place(x=250,y=83)
    e2=Entry(foot3,font=('times',19),bd=5)
    e2.config(show='*')
    e2.place(x=250,y=143)
    b2=Button(foot3,text='Forgot Password',font=('times',10,'underline'),bg='lightgray',fg='black')
    b2.place(x=110,y=189)
    b3=Button(foot3,text='Log in...',command=lambda:show_mem(foot3,e1.get(),e2.get(),z=2),font=('times',15),bg='lightgray',fg='black')
    b3.place(x=515,y=142)
    b4=Button(foot3,text='            Create Account, Become a Member a member today         ',command=lambda:new1(foot3,root),font=('times',15),bg='lightgray',fg='black')
    b4.place(x=100,y=515)
    

def about(root,foot):
    foot.destroy()
    foot4=Frame(root,height=1080,width=1000)
    foot4.place(x=0,y=0)
    img=PhotoImage(file='lib.gif')
    lb1=Label(foot4,image=img)
    lb1.image=img
    lb1.pack(expand=True)
    b1=Button(foot4,text='Back',font=('times',17,'italic'),command=lambda:back(foot4,x=1),bg='#A7DBE1',fg='black')
    b1.place(x=30,y=650)
    lb2=Label(foot4,text='''A library is organized for use and maintained by a public 
                            body,an institution, a corporation, or a private individual.
                            Public and institutional collections and services may be  
                            intended for use by people who choose not to—or cannot afford
                            to—purchase an extensive collection themselves, who need material 
                            no individual can reasonably be expected to have, or who require
                            professional assistance with their research. In addition to providing
                            materials, libraries also provide the services of librarians who are 
                            experts at finding and organizing information and at interpreting
                            information needs. Libraries often provide quiet areas for studying,
                            and they also often offer common areas to facilitate group study and
                            collaboration. Libraries often provide public facilities for access 
                            to their electronic resources and the Internet.''',font=('times',15,'italic'),fg='black',bg='white',borderwidth=0)
    lb2.place(x=0,y=1)
    
    
def contact(root,foot):
    foot.destroy()
    foot5=Frame(root,height=1080,width=1000)
    foot5.place(x=0,y=0)
    img=PhotoImage(file='tui.gif')
    lab=Label(foot5,image=img)
    lab.image=img
    lab.pack(expand=True)
    lab1=Label(foot5,text='''Mob No. : 9999-xxxxxxx

Contact No. : 0129-xxxxxxx

                                                 OR
                                                
     Mail Us @ : xyzlibrary@gmail.com''',font=('Arial',17),)
    lab1.place(x=500,y=150)
    b1=Button(foot5,text='Back',font=('times',17,'italic'),command=lambda:back(foot5,x=1),bg='#A7DBE1',fg='black')
    b1.place(x=30,y=650)
    

def helpp(root,foot):    
    foot.destroy()
    foot6=Frame(root,height=1080,width=1000)
    foot6.place(x=0,y=0)
    img=PhotoImage(file='pi.gif')
    lab=Label(foot6,image=img)
    lab.image=img
    lab.pack(expand=True)
    b1=Button(foot6,text='Back',font=('times',17,'italic'),command=lambda:back(foot6,x=1),bg='#A7DBE1',fg='black')
    b1.place(x=30,y=650)
    lab=Label(foot6,text='STEP 1 :',font=('times',47,'italic'),fg='brown')
    lab.place(x=5,y=5)
    lab1=Label(foot6,text=''' If You was an authorized Reder You can go to Reder's Login''',font=('times',17,'italic'),fg='brown')
    lab1.place(x=57,y=65)
    lab2=Label(foot6,text='STEP 2 :',font=('times',47,'italic'),fg='brown')
    lab2.place(x=5,y=120)
    lab3=Label(foot6,text=''' If You was registered Author You can access Author's Login''',font=('times',17,'italic'),fg='brown')
    lab3.place(x=57,y=185)
    lab4=Label(foot6,text='STEP 3 :',font=('times',47,'italic'),fg='brown')
    lab4.place(x=5,y=230)
    lab5=Label(foot6,text=''' If You are New to our Library You can Use Explore...''',font=('times',17,'italic'),fg='brown')
    lab5.place(x=57,y=290)
    lab6=Label(foot6,text='STEP 4 :',font=('times',47,'italic'),fg='brown')
    lab6.place(x=5,y=335)
    lab7=Label(foot6,text=''' You can also Use our Map for Correct way it will also ping you to live loction...''',font=('times',17,'italic'),fg='brown')
    lab7.place(x=57,y=395)
    lab8=Label(foot6,text='STEP 5 :',font=('times',47,'italic'),fg='brown')
    lab8.place(x=5,y=445)
    lab9=Label(foot6,text=''' Yoy can Also use our Video Featue for better Understanding...''',font=('times',17,'italic'),fg='brown')
    lab9.place(x=57,y=505)
    lab11=Label(foot6,text=''' Enjoy The Library is all Your's......''',font=('times',27,'italic'),fg='brown')
    lab11.place(x=477,y=575)
    b1=Button(foot6,text='Play Video...',font=('times',17,'italic'),command=lambda:video(),bg='#A7DBE1')
    b1.config(width=20)
    b1.place(x=705,y=30)

    
    
    
root=Tk()
root.geometry('985x900')
root.title('LIBRARY MANAGEMENT')
#function calling....
home()
