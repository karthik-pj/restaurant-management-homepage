#RESTAURANT MANAGEMENT HOME PAGE
#===========================================================================================
from tkinter import *
from tkinter import ttk
import mysql.connector as mc
import tkinter.messagebox as tm
#from PIL import ImageTk, Image # PIL - python photo image library
from tkhtmlview import * #import html project
win=Tk()
win.geometry('1000x600')
win.config(bg='#ffead5')
win.title('🕸 RESATURANT 🕸')

#======================================== FRAME ============================================
f1=Frame(win,width=1365,height=50,bg='#6f6f6f',relief=GROOVE,borderwidth=5)
f1.place(x=0,y=0)

#===================================== LABEL CREATION ======================================
l1=Label(f1,text='Phone.No: 9597948459',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
l1.place(x=0,y=5)
l2=Label(win,text='FOOD MATES 🥰',font=('Algerian',50,'bold'),fg='black',bg='#ffead5')
l2.place(x=1,y=50)
l3=Label(win,text='WELCOME YOU ALL!!!',font=('Berlin Sans FB',35,'bold'),bg='#ffead5')
l3.pack(fill=X,pady=300)

#===========================================================================================

h1=HTMLLabel(win,html='<a href="https://www.instagram.com/_karthik.20_pj/"> Instagram </a>')
h1.config(bg='#ffead5')
h1.place(x=100,y=550,width=100,height=30)
h2=HTMLLabel(win,html='<a href="https://www.youtube.com/@karthikefx6652"> Youtube </a>')
h2.config(bg='#ffead5')
h2.place(x=630,y=550,width=80,height=30)
h3=HTMLLabel(win,html='<a href="https://twitter.com/karthik_0502/"> Twitter </a>')
h3.config(bg='#ffead5')
h3.place(x=1200,y=550,width=70,height=30)

#======================================== FRAME ============================================
f2=Frame(win,width=1365,height=110,bg='#6f6f6f',relief=GROOVE,borderwidth=5)
f2.place(x=0,y=590)

#===========================================================================================
l4=Label(win,text='Address',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
l4.place(x=100,y=600)
l5=Label(win,text='T Nagar, Chennai-600017',font=('Times New Roman',15),bg='#6f6f6f',fg='white')
l5.place(x=25,y=630)
l6=Label(win,text='☏ Order food: 9751748459',font=('Times New Roman',15),bg='#6f6f6f',fg='white')
l6.pack()
l6.place(x=600,y=625)
l7=Label(win,text='🕤 Timing',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
l7.place(x=1200,y=600)
l8=Label(win,text='Monday - Saturday',font=('Times New Roman',15),bg='#6f6f6f',fg='white')
l8.place(x=1170,y=625)
l9=Label(win,text='7:00AM - 10:300 PM',font=('Times New Roman',15),bg='#6f6f6f',fg='white')
l9.place(x=1150,y=650)


#====================================== CHILD WINDOW FOR MENU ===============================
def newwindow():
    new_win=Toplevel(win)
    new_win.geometry('700x400')
    new_win.config(bg='#ffead5')
    lb1=Label(new_win,text='--- Menu ---',font=('Times New Roman',30,'bold'),bg='#ffead5')
    lb1.pack()
#--------------------------------------------------------------------------------------------
    f2=Frame(new_win,width=1365,height=38,bg='#6f6f6f',borderwidth=5)
    f2.place(x=0,y=50)
    f3=Frame(new_win,width=1365,height=38,bg='#6f6f6f',borderwidth=5)
    f3.place(x=0,y=144)
    f4=Frame(new_win,width=1365,height=38,bg='#6f6f6f',borderwidth=5)
    f4.place(x=0,y=310)
    f5=Frame(new_win,width=1365,height=38,bg='#6f6f6f',borderwidth=5)
    f5.place(x=0,y=430)
#--------------------------------------------------------------------------------------------
    lb1=Label(new_win,text='MEALS',font=('Times New Roman',20,'bold'),bg='#6f6f6f',fg='white')
    lb1.pack()
    
    lb2=Label(new_win,text='1.VEG - 150 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb2.pack()
    lb3=Label(new_win,text='2.NON-VEG - 150 RS',font=('Times New Roman',15),bg='#ffead5')
    lb3.pack()
    
    lb4=Label(new_win,text='RICE VARIETTES',font=('Times New Roman',20,'bold'),bg='#6f6f6f',fg='white')
    lb4.pack()
    lb5=Label(new_win,text='VEG',font=('Times New Roman',15,'bold'),bg='#ffead5')
    lb5.place(x=200,y=190)
    lb10=Label(new_win,text='NON-VEG',font=('Times New Roman',15,'bold'),bg='#ffead5')
    lb10.place(x=900,y=190)
    
    lb6=Label(new_win,text='1.VEG  BRIYANI - 100 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb6.place(x=150,y=220)
    lb7=Label(new_win,text='2.VEG FRIED RICE - 120 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb7.place(x=150,y=240)
    lb8=Label(new_win,text='3.MUSROOM BRIYANI - 120 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb8.place(x=150,y=260)
    lb9=Label(new_win,text='4.BRINGE - 100 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb9.place(x=150,y=280)
    
    lb11=Label(new_win,text='1.CHICKEN BRIYANI - 150 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb11.place(x=850,y=220)
    lb12=Label(new_win,text='2.MUTTON BRIYANI - 200 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb12.place(x=850,y=240)
    lb13=Label(new_win,text='3.EGG BRIYANI - 120 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb13.place(x=850,y=260)
    lb14=Label(new_win,text='4.CHICKEN FRIED RICE - 100 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb14.place(x=850,y=280)
    
    lb15=Label(new_win,text='SIDE DISHES',font=('Times New Roman',20,'bold'),bg='#6f6f6f',fg='white')
    lb15.place(x=590,y=310)
    lb16=Label(new_win,text='1.GOPI 65 - 75 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb16.place(x=150,y=360)
    lb17=Label(new_win,text='2.MUSROOM - 75 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb17.place(x=150,y=380)
    lb18=Label(new_win,text='3.PANEER 65 - 75 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb18.place(x=150,y=400)

    lb16=Label(new_win,text='1.CHICKEN 65 - 100 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb16.place(x=850,y=360)
    lb17=Label(new_win,text='2.CHICKEN GRILL (FULL) - 250 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb17.place(x=850,y=380)
    lb18=Label(new_win,text='3.CHICKEN THANDOORI(FULL) - 250 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb18.place(x=850,y=400)

    lb19=Label(new_win,text='BEVERAGES',font=('Times New Roman',20,'bold'),bg='#6f6f6f',fg='white')
    lb19.place(x=150,y=430)
    lb20=Label(new_win,text='DESSERTS',font=('Times New Roman',20,'bold'),bg='#6f6f6f',fg='white')
    lb20.place(x=850,y=430)

    lb21=Label(new_win,text='1.LIME JUICE - 50 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb21.place(x=150,y=480)
    lb22=Label(new_win,text='2.LASSI SALT/SUGAR - 50 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb22.place(x=150,y=500)
    lb23=Label(new_win,text='3.FRESH FRUITE JUICE - 75 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb23.place(x=150,y=520)
    lb24=Label(new_win,text='4.SODA - 25 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb24.place(x=150,y=540)

    lb21=Label(new_win,text='1.RED VALVET CAKE - 75 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb21.place(x=850,y=480)
    lb22=Label(new_win,text='2.FRUIT SALAD - 100 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb22.place(x=850,y=500)
    lb23=Label(new_win,text='3.ICE REAM (ALL VARIETTES) - 100 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb23.place(x=850,y=520)
    lb24=Label(new_win,text='4.FALLODA - 100 Rs',font=('Times New Roman',15),bg='#ffead5')
    lb24.place(x=850,y=540)

    exit1=Button(new_win,text='Exit',command=lambda:new_win.destroy(),font=('Times New Roman',15),bg='red',fg='white')
    exit1.place(x=650,y=600)
    
menu=Button(win,text='Menu',command=newwindow,font=('Times New Roman',15),bg='#6f6f6f',fg='white')
menu.place(x=1065,y=55)
#============================================================================================

def newwindow1():
    new_win1=Toplevel(win)
    new_win1.geometry('700x400')
    new_win1.configure(bg='#ffead5')
#----------------------------------------------------------------------------------------------------
    f12=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f12.place(x=0,y=0)
#----------------------------------------------------------------------------------------------------

    Lb1=Label(new_win1,text='DETAILS',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb1.place(x=620,y=0)
    Lb2=Label(new_win1,text='Upscale indoor/outdoor hotel offering Indian and Continental dishes, plus live blues music.',font=('Times New Roman',15),bg='#ffead5')
    Lb2.place(x=250,y=40)
#----------------------------------------------------------------------------------------------------
    f13=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f13.place(x=0,y=90)
#----------------------------------------------------------------------------------------------------

    Lb3=Label(new_win1,text='SREVICE OPTIONS',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb3.place(x=580,y=90)
    Lb4=Label(new_win1,text='🚴‍ Delivery',font=('Times New Roman',15),bg='#ffead5')
    Lb4.place(x=200,y=120)
    Lb5=Label(new_win1,text='⛱ Outdoor seating',font=('Times New Roman',15),bg='#ffead5')
    Lb5.place(x=400,y=120)
    Lb6=Label(new_win1,text='🏃‍ Take away',font=('Times New Roman',15),bg='#ffead5')
    Lb6.place(x=600,y=120)
    Lb7=Label(new_win1,text='🍜 Dine-in',font=('Times New Roman',15),bg='#ffead5')
    Lb7.place(x=800,y=120)
#----------------------------------------------------------------------------------------------------
    f4=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f4.place(x=0,y=150)
#----------------------------------------------------------------------------------------------------
    Lb8=Label(new_win1,text='ACCESSIBLITY',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb8.place(x=590,y=150)
    
    Lb9=Label(new_win1,text='👨‍🦼 Wheelcahir-accessbility toilet',font=('Times New Roman',15),bg='#ffead5')
    Lb9.place(x=200,y=180)
    Lb10=Label(new_win1,text='👨‍🦼 Wheelcahir-accessbility chair',font=('Times New Roman',15),bg='#ffead5')
    Lb10.place(x=600,y=180)
#----------------------------------------------------------------------------------------------------
    f5=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f5.place(x=0,y=210)
#----------------------------------------------------------------------------------------------------
    Lb11=Label(new_win1,text='OFFERING',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb11.place(x=600,y=210)

    Lb12=Label(new_win1,text='☕︎ Coffee',font=('Times New Roman',15),bg='#ffead5')
    Lb12.place(x=200,y=240)
    Lb13=Label(new_win1,text='🍸 Cocktails',font=('Times New Roman',15),bg='#ffead5')
    Lb13.place(x=600,y=240)
#----------------------------------------------------------------------------------------------------
    f6=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f6.place(x=0,y=270)
#----------------------------------------------------------------------------------------------------
    Lb14=Label(new_win1,text='DINING OPTIONS',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb14.place(x=580,y=270)
    
    Lb15=Label(new_win1,text='🍛 Lunch',font=('Times New Roman',15),bg='#ffead5')
    Lb15.place(x=200,y=300)
    Lb16=Label(new_win1,text='🍝 Dinner',font=('Times New Roman',15),bg='#ffead5')
    Lb16.place(x=400,y=300)
    Lb17=Label(new_win1,text='🍹 Beverages',font=('Times New Roman',15),bg='#ffead5')
    Lb17.place(x=600,y=300)
    Lb18=Label(new_win1,text='🍨 Dessert',font=('Times New Roman',15),bg='#ffead5')
    Lb18.place(x=800,y=300)
#----------------------------------------------------------------------------------------------------
    f7=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f7.place(x=0,y=330)
#----------------------------------------------------------------------------------------------------
    Lb19=Label(new_win1,text='AMINITIES',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb19.place(x=600,y=330)

    Lb19=Label(new_win1,text='🌐 Wifi',font=('Times New Roman',15),bg='#ffead5')
    Lb19.place(x=200,y=360)
    Lb20=Label(new_win1,text='👶 Good for kids',font=('Times New Roman',15),bg='#ffead5')
    Lb20.place(x=400,y=360)
    Lb21=Label(new_win1,text='🚽 Toilet',font=('Times New Roman',15),bg='#ffead5')
    Lb21.place(x=600,y=360)
    Lb22=Label(new_win1,text='♬ Music',font=('Times New Roman',15),bg='#ffead5')
    Lb22.place(x=800,y=360)
    
#----------------------------------------------------------------------------------------------------
    f8=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f8.place(x=0,y=390)
#----------------------------------------------------------------------------------------------------
    Lb23=Label(new_win1,text='ATMOSPHERE',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb23.place(x=590,y=390)

    Lb24=Label(new_win1,text='🏘 Casual',font=('Times New Roman',15),bg='#ffead5')
    Lb24.place(x=200,y=420)
    Lb25=Label(new_win1,text='🌆 Cosy',font=('Times New Roman',15),bg='#ffead5')
    Lb25.place(x=400,y=420)
    Lb26=Label(new_win1,text='♥ Romentic',font=('Times New Roman',15),bg='#ffead5')
    Lb26.place(x=600,y=420)

#----------------------------------------------------------------------------------------------------
    f9=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f9.place(x=0,y=450)
#----------------------------------------------------------------------------------------------------
    Lb27=Label(new_win1,text='CROWD',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb27.place(x=620,y=450)

    Lb28=Label(new_win1,text='👬🏿👫🏿 Family friendly',font=('Times New Roman',15),bg='#ffead5')
    Lb28.place(x=200,y=480)
    Lb29=Label(new_win1,text='👬🏿👫🏿 Groups',font=('Times New Roman',15),bg='#ffead5')
    Lb29.place(x=600,y=480)

#----------------------------------------------------------------------------------------------------
    f10=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f10.place(x=0,y=510)
#----------------------------------------------------------------------------------------------------
    Lb30=Label(new_win1,text='PLANNING',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb30.place(x=605,y=510)

    Lb31=Label(new_win1,text='✓ Accept reservations',font=('Times New Roman',15),bg='#ffead5')
    Lb31.place(x=200,y=540)

#----------------------------------------------------------------------------------------------------
    f11=Frame(new_win1,width=1365,height=30,bg='#6f6f6f')
    f11.place(x=0,y=580)
#----------------------------------------------------------------------------------------------------
    Lb32=Label(new_win1,text='PAYMENTS',font=('Times New Roman',15,'bold'),bg='#6f6f6f',fg='white')
    Lb32.place(x=605,y=580)

    Lb33=Label(new_win1,text='✓ Debit card',font=('Times New Roman',15),bg='#ffead5')
    Lb33.place(x=200,y=610)
    Lb34=Label(new_win1,text='✓ Credit Card',font=('Times New Roman',15),bg='#ffead5')
    Lb34.place(x=400,y=610)
    Lb35=Label(new_win1,text='✓ Google pay',font=('Times New Roman',15),bg='#ffead5')
    Lb35.place(x=600,y=610)
    Lb36=Label(new_win1,text='✓ American Express,Master card,VISA',font=('Times New Roman',15),bg='#ffead5')
    Lb36.place(x=800,y=610)

    
about=Button(win,text='About',command=newwindow1,font=('Times New Roman',15),bg='#6f6f6f',fg='white')
about.place(x=1140,y=55)
#=====================================================================================================

def gallery():
    new_win1=Toplevel(win)
    new_win1.geometry('700x400')
    new_win1.title('Restaurant images')
    new_win1.config(bg='#ffead5')
    p1 = HTMLLabel(new_win1,html='<img src="C:\\Users\\LENOVO\\OneDrive\\Pictures\\dine in.jpg"width=400 height=200>')
    p1.config(bg='#ffead5')
    p1.place(x=100,y=100,width=400,height=200)
    p2 = HTMLLabel(new_win1,html='<img src="C:\\Users\\LENOVO\\OneDrive\\Pictures\\blog-banner-9-845x321.jpg"width=400 height=200>')
    p2.config(bg='#ffead5')
    p2.place(x=900,y=100,width=400,height=200)
    p3 = HTMLLabel(new_win1,html='<img src="C:\\Users\\LENOVO\\OneDrive\\Pictures\\exp-dinner.jpg"width=400 height=200>')
    p3.config(bg='#ffead5')
    p3.place(x=100,y=400,width=400,height=200)
    p4 = HTMLLabel(new_win1,html='<img src="C:\\Users\\LENOVO\\OneDrive\\Pictures\\thumb_presc.jpg"width=400 height=200>')
    p4.config(bg='#ffead5')
    p4.place(x=900,y=400,width=400,height=200)
#-------------------------------------------------------------------------------------------------
    fm1=Frame(new_win1,width=1365,height=38,bg='#6f6f6f',borderwidth=5)
    fm1.place(x=0,y=0)
    
#-------------------------------------------------------------------------------------------------
    LB1=Label(new_win1,text='GALLERY',font=('Times New Roman',20,'bold'),bg='#6f6f6f',fg='white')
    LB1.pack()
    LB2=Label(new_win1,text='Dine-in',font=('Times New Roman',15),bg='#ffead5')
    LB2.place(x=250,y=310)
    LB3=Label(new_win1,text='Outdoor seating',font=('Times New Roman',15),bg='#ffead5')
    LB3.place(x=1050,y=310)
    LB4=Label(new_win1,text='Candle dinner',font=('Times New Roman',15),bg='#ffead5')
    LB4.place(x=250,y=610)
    LB5=Label(new_win1,text='Children park',font=('Times New Roman',15),bg='#ffead5')
    LB5.place(x=1050,y=610)

    
menu=Button(win,text='Gallery',command=gallery,font=('Times New Roman',15),bg='#6f6f6f',fg='white')
menu.place(x=1215,y=55)

#==================================================================================================

def offer():
    k=Toplevel(win)
    k.geometry('700x400')
    k.config(bg='#ffead5')
#--------------------------------------------------------------------------------------------------
    fm2=Frame(k,width=1365,height=38,bg='#6f6f6f',borderwidth=5)
    fm2.place(x=0,y=0)
#--------------------------------------------------------------------------------------------------
    LB1=Label(k,text='COMBO OFFER',font=('Times New Roman',20,'bold'),bg='#6f6f6f',fg='white')
    LB1.pack()
    LB2=Label(k,text='1. Bucket mutton Briyani + Full Chicken grill + 8 Eggs + Chicken 65 + Desset + 4 drinks= 2500 Rs',font=('Times New Roman',15),bg='#ffead5')
    LB2.place(x=300,y=100)
    LB3=Label(k,text='2. Bucket Chicken Briyani + Full Chicken grill + 8 Eggs + Chicken 65 + Desset + 4 drinks= 2500 Rs',font=('Times New Roman',15),bg='#ffead5')
    LB3.place(x=300,y=150)
    LB4=Label(k,text='3. Bucket Mutton Briyani + Half Chicken grill + 4 Eggs + Chicken 65 + Desset + 4 drinks=1700 Rs',font=('Times New Roman',15),bg='#ffead5')
    LB4.place(x=300,y=200)
    LB5=Label(k,text='4. Bucket Chicken Briyani + Half Chicken grill + 4 Eggs + Chicken 65 + Desset + 4 drinks=1700 Rs',font=('Times New Roman',15),bg='#ffead5')
    LB5.place(x=300,y=250)
    LB6=Label(k,text='5. Veg Briyani (8 Mems)+ Gopi 65 + Mushroom 65 + Desset + 4 drinks=2000 Rs',font=('Times New Roman',15),bg='#ffead5')
    LB6.place(x=300,y=300)
    LB7=Label(k,text='6. Veg Briyani (4 Mems)+ Gopi 65 + Mushroom 65 + Desset + 4 drinks=1500 Rs',font=('Times New Roman',15),bg='#ffead5')
    LB7.place(x=300,y=350)
    
    
menu=Button(win,text='Offer',command=offer,font=('Times New Roman',15),bg='#6f6f6f',fg='white')
menu.place(x=1300,y=55)

#==================================================================================================

def DB():
    N=Toplevel(win)
    N.geometry('400x200')
    N.config(bg='#ffead5')
    N.title("GET DATA")

    
    


    def put(*args):
        e_name=i_name.get()
        e_age=i_age.get()
        e_gender=i_gender.get()
        e_contact=i_contact.get()
        e_table=i_table.get()
        e_date=i_date.get()
        e_time=i_time.get()
        conn = mc.connect(user="root", password="", host="localhost", database='tabel_booking')
        cur = conn.cursor()
        cur.execute("insert into process(Name,Age,Gender,Contact,Table_no,Date,Time) values('"+e_name+"', '"+e_age+"', '"+e_gender+"', '"+e_contact+"', '"+e_table+"', '"+e_date+"', '"+e_time+"')")
        conn.close()
        
    mainframe = Frame(N)
    mainframe.config(bg='#ffead5')
    mainframe.place(x=0,y=0)

    i_name = StringVar()
    i_age = StringVar()
    i_gender = StringVar()
    i_contact = StringVar()
    i_table = StringVar()
    i_date = StringVar()
    i_time = StringVar()

    l1=Label(mainframe, text='Name')
    l1.config(bg='#ffead5')
    l1.grid(row=0,column=0)
    l2=Label(mainframe, text='Age')
    l2.config(bg='#ffead5')
    l2.grid(row=2,column=0)
    l3=Label(mainframe, text='Gender')
    l3.config(bg='#ffead5')
    l3.grid(row=4,column=0)
    l4=Label(mainframe, text='Contact')
    l4.config(bg='#ffead5')
    l4.grid(row=6,column=0)
    l5=Label(mainframe, text='Table')


    l5.config(bg='#ffead5')
    l5.grid(row=8,column=0)
    l6=Label(mainframe, text='Date')
    l6.config(bg='#ffead5')
    l6.grid(row=10,column=0)
    l7=Label(mainframe, text='Time')
    l7.config(bg='#ffead5')
    l7.grid(row=12,column=0)


    E1= Entry(mainframe, width=20, textvariable=i_name)
    E1.grid(row=0,column=3)

    E2= Entry(mainframe, width=20, textvariable=i_age)
    E2.grid(row=2,column=3)
    E3= ttk.Combobox(mainframe, width=20, textvariable=i_gender)
    E3['values']=('Male','Female')
    E3.grid(row=4,column=3)
    E4= Entry(mainframe, width=20, textvariable=i_contact)
    E4.grid(row=6,column=3)
    E5= ttk.Combobox(mainframe, width=20, textvariable=i_table)
    E5['values']=('Table-1','Table-2','Table-3','Table-4','Table-5','Table-6','Table-7','Table-8','Table-9','Table-10')
    E5.grid(row=8,column=3)
    E6= Entry(mainframe, width=20, textvariable=i_date)
    E6.grid(row=10,column=3)
    E7= ttk.Combobox(mainframe, width=20, textvariable=i_time)
    E7['values']=('10:00 AM-12:00 AM','01:00 PM-03:00 PM','05:00 PM-07:70 PM','08:00 PM-10:00 PM')
    E7.grid(row=12,column=3)


    B=Button(mainframe, text="Insert my info to sql", command=put).grid(row=16,column=3)

    N.mainloop()
        


    
K=Button(win,text='BOOK YOUR SEAT',command=DB,font=('Times New Roman',15),bg='green',fg='white')
K.place(x=580,y=500)




win.mainloop()
