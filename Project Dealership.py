import pandas as pd,numpy as np, sys,matplotlib.pyplot as plt
from tabulate import tabulate
        
# OLD USER SEARCH AND DEPLOY

def ENTRY():
    Admin=pd.read_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv")
    User=pd.read_csv("E:\\Yash\\Pro Project\\Main\\User.csv")
    global name
    print(" "*70)
    print("*"*70)
    print(" "*70)
    print("Kindly, Maintain the first Letter Capital!!")
    name=input("Enter your name:")
    print(" "*70)
    print("*"*70)
    if name in list(Admin['Name']):
        print(" "*70)
        print("You're a admin!!")
        global f
        print(" "*70)
        f=int(input("Enter your password:"))
        ADMIN()
    elif name in list(User['Name']):
        print(" "*70)
        print("You're a User!!")
        USER_STUFF()
    else:
        print(" "*70)
        print("Cannot Locate ur Name Anywhere !!")
        print("To register yourself as anyone, press R!")
        print("To retry Login, press L!")
        print("Else, leave empty to exit!!")
        print(" "*70)
        e=input("Enter Your choice:")
        if e=="R" or e=="r":
            print("Proceeding for Registration...")
            REGISTRATION()
        elif e=="l" or e=="L":
            ENTRY()
        elif e=="":
            sys.exit()
        else:
            print("INVALID INPUT!!")
            ENTRY()


#AUTHENTIC USER, CAN EDIT ITEMS AND USER
        
def ADMIN():
    Admin=pd.read_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv")
    desired_name_row=Admin[Admin['Name']==name]
    t=desired_name_row['Password'].values[0]
    if f==t:
        print("Alright !! U r good to go ,Edit as many thing u want !!")
        ADMIN_STUFF()
    else:
        print("The Password is Invalid !!")
        print("Kindly Retry with a Correct One...")
        ENTRY()
        
    

#ADMIN RIGHTS AND AVAILABLE OPTIONS

def ADMIN_STUFF():

    print(" "*70)
    print("*"*70)
    print(" "*70)
    print("[Enter 01] To Display the CARS List")
    print("[Enter 02] To Modify The Vehicle Details !!")
    print("[Enter 03] To Modify The Admins Details !!")
    print("[Enter 04] View the Admin's Count ")
    print("[Enter 05] View the User's Count ")
    print("[Press Enter] To Exit")
    print(" "*70)
    print("*"*70)
    print(" "*70)

    i=int(input("Enter Your choice:"))

    if i==1:
        CSV()
        ADMIN_STUFF()
       
    elif i==2:
        
        print("Choose which Type of Modifiation would u like to make")
        print("Out of Addition (1), Updation (2) and Deletion (3)")
        c=int(input("Enter Your choice:"))

        if c==1:
            NEW()
            ADMIN_STUFF()

        elif c==2:
            UPDATE()
            ADMIN_STUFF()

        elif c==3:
            DELETE()
            ADMIN_STUFF()

        else:
            print("Sorry, Your responce is not acceptable")
            ADMIN_STUFF()
        
        
    elif i==3:
        
        print("Choose which Type of Modifiation would u like to make")
        print("Out of Addition (1), Updation (2) and Deletion (3)")
        c=int(input("Enter Your choice:"))

        if c==1:
            ADMIN_NEW()
            ADMIN_STUFF()

        elif c==2:
            ADMIN_UPDATE()
            ADMIN_STUFF()

        elif c==3:
            ADMIN_DELETE()
            ADMIN_STUFF()
            
        else:
            print("Sorry, Your responce is not acceptable")
            ADMIN_STUFF()
        
    elif i==4:
        Admin=pd.read_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv")
        print(tabulate(Admin,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        ADMIN_STUFF()

    elif i==5:
        User=pd.read_csv("E:\\Yash\\Pro Project\\Main\\User.csv")
        print(tabulate(User,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        ADMIN_STUFF()

    elif i==6:
        ADMIN_LINE()
        
    elif i==7:
        ADMIN_BAR()
        
    elif i==8:
        ADMIN_HISTO()
        
    elif i=='':
        sys.exit()

    else:
        print("Sorry, Your responce is not acceptable")
        ADMIN_STUFF()
        
#LOGIN AS USER

def USER():

    print(" ")
    User=pd.read_csv("E:\\Yash\\Pro Project\\Main\\User.csv")
    print(" ")
    
    print("Login as User")
    print(" ")
    
    print("Kindly, Maintain the first Letter Capital!!")
    u=input("Enter Your Good Name:")
    
    if u in list(User['Name']):
        print(" ")
        print("Alright, You've Got Access!!")
        print(" ")
        USER_STUFF()
        
    else:
        print("USER NOT FOUND !!!")
        print("RETRY")
        USER()
        

#USER KE Choices:
        
def USER_STUFF():
    print(" "*70)
    print("*"*70)
    print("Welcome To AMG TROS. Motor Garage !!!")
    print("AMG brought you to another level of experience!!")
    print(" ")
    print("[Enter 'M'] To Explore Our Models and Features .")
    print("[Enter 'L'] To Display the Line Chart")
    print("[Enter 'B'] To Display the Bar Chart")
    print("[Enter 'H'] To Display the Histogram")
    print("[Enter 'S'] Want to buy some of these Uniques !!!")
    print("[Enter 'A'] To Know More About Us .")
    print("[Hit Enter] To Exit")
    print("*"*70)
    print(" "*70)
    
    h=input("Kindly Enter Your choice -->")
    
    if h=='m' or h=='M':
        MENU()
    elif h=='l' or h=='L':
        USER_LINE()
    elif h=='b' or h=='B':
        USER_BAR()
    elif h=='h' or h=='H':
        USER_HISTO()
    elif h=='s' or h=='S':       
        SHOP()
    elif h=='a' or h=='A':
        ABOUT()
    elif h=='':
        print("*"*70)
        print("Successfully Exit")
        print("*"*70)
        sys.exit()
    else:
        print("Sorry, Your responce is not acceptable")


#NEW USER ADDITION
        
def REGISTRATION():
    User=pd.read_csv("E:\\Yash\\Pro Project\\Main\\User.csv")
    print("Register Yourself as User")
    print(" ")

    uid=User['Id'].max()
    u_name=input("Let me know Your name:") 
    u_age=float(input("How old are you:"))
    u_gender=input("Your Gender:")
    u_city=input("Your City:")
    c=input("Have you purchased anything(y/n):")
    if c=="y" or c=="Y":
        p=float(input("How much item you have purchased:"))
    elif c=="n" or c=="N":
        p=np.NaN
    else:
        print("Sorry, Your responce is not acceptable, RETRY")
        REGISTRATION()

    data={'Id':uid+1,'Name':u_name,'Age':u_age,'Gender':u_gender,'City':u_city,'Items Purchased':p}
    DATA=pd.DataFrame([data])
    User=pd.concat([User,DATA],ignore_index=True)

    print(" ")
    print(tabulate(User,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" ")
    
    User.to_csv("E:\\Yash\\Pro Project\\Main\\User.csv", index=False)

    USER_STUFF()

#MAIN READING
    
def Read():
    
    SUV="E:\\Yash\\Pro Project\\Models\\SUV.csv"
    XUV="E:\\Yash\\Pro Project\\Models\\XUV.csv"
    Coupe="E:\\Yash\\Pro Project\\Models\\Coupe.csv"
    Roadster="E:\\Yash\\Pro Project\\Models\\Roadster.csv"
    Super_Car="E:\\Yash\\Pro Project\\Models\\Super Car.csv"

    return SUV,XUV,Coupe,Roadster,Super_Car


#MAIN CSV

def CSV():

    SUV,XUV,Coupe,Roadster,Super_Car = Read()

    df1=pd.read_csv(SUV)
    df2=pd.read_csv(XUV)
    df3=pd.read_csv(Coupe)
    df4=pd.read_csv(Roadster)
    df5=pd.read_csv(Super_Car)
    
    print(" "*70)
    print("*"*53,"SUVs","*"*53)
    print(" "*70)
    print(tabulate(df1,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" "*70)
    print("*"*53,"XUVs","*"*53)
    print(" "*70)
    print(tabulate(df2,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" "*70)
    print("*"*53,"Coupe","*"*53)
    print(" "*70)
    print(tabulate(df3,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" "*70)
    print("*"*51,"Roadster","*"*51)
    print(" "*70)
    print(tabulate(df4,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" "*70)
    print("*"*50,"Super Cars","*"*50)
    print(" "*70)
    print(tabulate(df5,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" "*70)
    
    
#MENU FOR REVIEW OF ITEMS
def MENU():
    print("Welcome to our MENU")
    print("This is content we have right in here!!")
    
    CSV()

    print(" ")    
    print("Would u like to Shop any of these ? Press Y ")
    print("Or return to the User Menu by pressing N ")
    o=input("Kindly Enter Your Choice :")
    print(" ")
    
    if o=="y" or o=="Y":
        SHOP()
    elif o=="n" or o=="N":
        USER_STUFF()
    
#ABOUT THE PROGRAM

def ABOUT():

    print(" ")    
    print("Our Company is Found by Master Yash during the period of 2023-24 at the School's Computer Lab")
    print("It was executed with the Aim of it being a known for it richness of Codes and quality use of libraries")
    print(" ")
    a=input("Press Enter To Go Back or 'x' to EXIT!!")
    print(" ")

    if a=="X" or a=="x":
        sys.exit()
    else:
        USER_STUFF()

#ADDING A NEW VEHICLE

def NEW():
    
    print(" ")
    print("Adding A New Record to the Car List")
    print(" ")
    print("Choose in which Model u would like to add a RECORD")
    print("Out of SUV (1), XUV (2), Coupe (3), Roadster (4), Super Cars (5)")
    
    c=int(input("Enter Your Choice : "))
    print(c)

    SUV,XUV,Coupe,Roadster,Super_Car = Read()
    
    l=[SUV,XUV,Coupe,Roadster,Super_Car]
    a=len(l)
    
    if c-1<=a:
        df=pd.read_csv(l[c-1])

        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")
        
        cid=max(list(df['ID']))
        cname=input("Enter Model Name:")
        ced=float(input("Enter Engine Displacement:"))
        cts=float(input("Enter Top Speed (kmph):"))
        ca=float(input("Enter Acceleration (in sec):"))
        cp=float(input("Enter Power (bhp):"))
        ct=float(input("Enter Torque (Nm):"))
        cpr=float(input("Enter Price (in $):"))
        print(" ")

        t={"ID":cid+1,"Vehicle Model Name":cname,"Engine Disp.":ced,"Top Speed":cts,"Acceleration":ca,"Power":cp,"Torque":ct,"Price (in $)":cpr}
        dt=pd.DataFrame([t])
        df=pd.concat([df,dt],ignore_index=True)
        
        print("*"*100)
        print("Record Added Successfully")
        print("*"*100)

        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")
        
        print(" ")
        
        df.to_csv(l[c-1],index=False)

    else:
        print(" ")
        print("Sorry, Your responce is not acceptable")
        print(" ")
        NEW()

#UPDATING AN EXISTING VEHICLE

def UPDATE():

    print(" ")
    print("Updating an Existing Record from the Car List")
    print(" ")
    print("Choose in which Model u would like to Update a RECORD")
    print("Out of SUV (1), XUV (2), Coupe (3), Roadster (4), Super Cars (5)")
    
    c=int(input("Enter Your Choice : "))
    print(" ")

    SUV,XUV,Coupe,Roadster,Super_Car = Read()

    l=[SUV,XUV,Coupe,Roadster,Super_Car]
    a=len(l)
    
    if c-1<=a:
        df=pd.read_csv(l[c-1])

        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")

        cid=int(input("Enter Model ID:"))
        cname=input("Enter Model Name:")
        ced=float(input("Enter Engine Displacement:"))
        cts=float(input("Enter Top Speed (kmph):"))
        ca=float(input("Enter Acceleration (in sec):"))
        cp=float(input("Enter Power (bhp):"))
        ct=float(input("Enter Torque (Nm):"))
        cpr=float(input("Enter Price (in $):"))
        print(" ")

        df.loc[cid-1,:]=[cid,cname,ced,cts,ca,cp,ct,cpr]

        print("*"*100)
        print("Record Updated Successfully")
        print("*"*100)
        
        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")
        
        print(" ")
        df.to_csv(l[c-1],index=False)

    else:
        print("Sorry, Your responce is not acceptable")
        UPDATE()

#DELETING A VEHICLE

def DELETE():

    print(" ")
    print("Deleteing an Existing Record from the Car List")
    print(" ")
    print("Choose in which Model u would like to delete a RECORD")
    print("Out of SUV (1), XUV (2), Coupe (3), Roadster (4), Super Cars (5)")
    c=int(input("Enter Your Choice : "))
    print(" ")

    SUV,XUV,Coupe,Roadster,Super_Car = Read()

    l=[SUV,XUV,Coupe,Roadster,Super_Car]
    a=len(l)
    
    if c-1<=a:
        df=pd.read_csv(l[c-1])

        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")
        
        cid=int(input("Enter Model ID:"))
        df.drop(cid-1,axis=0,inplace=True)
        print(" ")

        print("*"*100)
        print("Record Removed Successfully")
        print("*"*100)
        
        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")
        
        print(" ")
        df.to_csv(l[c-1],index=False)

    else:
        print("Sorry, Your responce is not acceptable")
        DELETE()

#ADDING NEW ADMIN

def ADMIN_NEW():

    print(" ")
    print("Adding A New Admin ....")
    print(" ")
    Admin=pd.read_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv")
    print(tabulate(Admin,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" ")

    aid=max(list(Admin['Id']))
    name=input("Enter The New Admin's Name:")
    code=float(input("Enter The New Admin's Password:"))

    t={"Id":aid+1,"Name":name,"Password":code}
    dt=pd.DataFrame([t])
    Admin=pd.concat([Admin,dt],ignore_index=True)
        
    print(" ")
    print("*"*100)
    print("Record Added Successfully")
    print("*"*100)
    print(" ")

    print(" ")
    print(tabulate(Admin,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" ")

    Admin=Admin.to_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv",index=False)

def ADMIN_UPDATE():

    print(" ")
    print("Updating the record of a Existing Admin ....")
    print(" ")
    Admin=pd.read_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv")
    print(tabulate(Admin,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" ")

    aid=float(input("Enter The Admin's ID:"))
    name=input("Enter The Admin's Name:")
    code=float(input("Enter The Admin's Password:"))

    Admin.loc[aid-1,:]=[aid,name,code]
        
    print("*"*100)
    print("Record Updated Successfully")
    print("*"*100)

    print(" ")
    print(tabulate(Admin,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" ")

    Admin=Admin.to_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv",index=False)

def ADMIN_DELETE():

    print(" ")
    print("Deleting the record of a Existing Admin ....")
    print(" ")
    Admin=pd.read_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv")
    print(tabulate(Admin,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" ")

    aid=float(input("Enter The Admin's ID:"))
    Admin.drop(aid-1,axis=0,inplace=True)
        
    print("*"*100)
    print("Record Deleted Successfully")
    print("*"*100)

    print(" ")
    print(tabulate(Admin,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
    print(" ")

    Admin=Admin.to_csv("E:\\Yash\\Pro Project\\Main\\Admin.csv",index=False)   

def USER_LINE():
    LINE()
    USER_STUFF()

def USER_BAR():
    BAR()
    USER_STUFF()
    
def USER_HISTO():
    LINE()
    USER_STUFF()
    
def ADMIN_LINE():
    LINE()
    ADMIN_STUFF()
    
def ADMIN_BAR():
    BAR()
    ADMIN_STUFF()
    
def ADMIN_HISTO():
    HISTO()
    ADMIN_STUFF()


#LINE CHART
        
def LINE():

    print(" ")
    print("Graphing a Line Chart from the Car List .... ")
    print(" ")
    print("Choose Which would you prefer to see the graph for?")
    print("Out of SUV (1), XUV (2), Coupe (3), Roadster (4), Super Cars (5)")
    c=int(input("Enter Your Choice : "))
    print(" ")

    SUV,XUV,Coupe,Roadster,Super_Car = Read()

    l=[SUV,XUV,Coupe,Roadster,Super_Car]
    a=len(l)

    if c-1<=a:
        df=pd.read_csv(l[c-1])

        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")

        print("Which would you prefer to see the graph for? ")
        print("[Enter 'P'] for Price Graph")
        print("[Enter 'D'] for Description Graph ")
        c=input("Kindly Enter Your Choice :")
        
        m=df["Vehicle Model Name"]
        e=df["Engine Disp."]
        ts=df["Top Speed"]
        a=df["Acceleration"]
        p=df["Power"]
        t=df["Torque"]
        pr=df["Price (in $)"]

        if c=="p" or c=="P":

            plt.plot(m,pr,linestyle="dashdot",marker='d',color='k',label="Price (in $)")
            plt.xlabel("Vehicle Name")
            plt.ylabel("Price")
            plt.title("Vehicle Statistics")
            plt.legend()
            plt.show()

        elif c=="d" or c=="D":
            
            plt.plot(m,e,linestyle="dashdot",marker='d',color='maroon',label="Engine Disp.")
            plt.plot(m,ts,linestyle="dashed",marker='o',color='darkorchid',label="Top Speed")
            plt.plot(m,a,linestyle="dotted",marker='*',color='lightpink',label="Acceleration")
            plt.plot(m,p,linestyle="dashdot",marker='+',color='mediumvioletred',label="Power")
            plt.plot(m,t,linestyle="dashed",marker='d',color='magenta',label="Torque")
            
            plt.xlabel("Vehicle Name")
            plt.ylabel("Make and Model")
            plt.title("Vehicle Statistics")
            plt.legend()
            plt.show()

        else:
            print("Sorry, Your responce is not acceptable")
            LINE()

#BAR GRAPH

def BAR():

    print(" ")
    print("Graphing a Bar Chart from the Car List .... ")
    print(" ")
    print("Which would you prefer to see the graph for?")
    print("Out of SUV (1), XUV (2), Coupe (3), Roadster (4), Super Cars (5)")
    c=int(input("Enter Your Choice : "))
    print(" ")

    SUV,XUV,Coupe,Roadster,Super_Car = Read()

    l=[SUV,XUV,Coupe,Roadster,Super_Car]
    a=len(l)
    plt.figure(figsize=(10,7))

    if c-1<=a:
        df=pd.read_csv(l[c-1])

        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")

        print("Which would you prefer to see the graph for? ")
        print("[Enter 'P'] for Price Graph")
        print("[Enter 'D'] for Description Graph ")
        c=input("Kindly Enter Your Choice :")
        
        m=df["Vehicle Model Name"]
        e=df["Engine Disp."]
        ts=df["Top Speed"]
        a=df["Acceleration"]
        p=df["Power"]
        t=df["Torque"]
        pr=df["Price (in $)"]

        x=np.arange(len(m))

        if c=="p" or c=="P":

            plt.bar(m,pr,width=1,ec='w',color='k',label="Price (in $)")
            plt.xlabel("Vehicle Name")
            plt.ylabel("Price")
            plt.title("Vehicle Statistics")
            plt.legend()
            plt.show()

        elif c=="d" or c=="D":
            
            plt.bar(m,e,width=0.2,ec='w',color='maroon',label="Engine Disp.")
            plt.bar(x+0.2,ts,width=0.2,ec='w',color='darkorchid',label="Top Speed")
            plt.bar(x+0.4,a,width=0.2,ec='w',color='lightpink',label="Acceleration")
            plt.bar(x+0.6,p,width=0.2,ec='w',color='mediumvioletred',label="Power")
            plt.bar(x+0.8,t,width=0.2,ec='w',color='magenta',label="Torque")
            
            plt.xlabel("Vehicle Name")
            plt.ylabel("Make and Model")
            plt.title("Vehicle Statistics")
            plt.legend()
            plt.show()

        else:
            print("Sorry, Your responce is not acceptable")
            BAR()

#HISTOGRAM

def HISTO():

    print(" ")
    print("Graphing a Histogram from the Car List .... ")
    print(" ")
    print("Which would you prefer to see the graph for?")
    print("Out of SUV (1), XUV (2), Coupe (3), Roadster (4), Super Cars (5)")
    c=int(input("Enter Your Choice : "))
    print(" ")

    SUV,XUV,Coupe,Roadster,Super_Car = Read()

    l=[SUV,XUV,Coupe,Roadster,Super_Car]
    a=len(l)

    if c-1<=a:
        df=pd.read_csv(l[c-1])

        print(" ")
        print(tabulate(df,showindex=False,headers='keys',tablefmt='orgbtl',numalign='center'))
        print(" ")

        print("Which would you prefer to see the graph for? ")
        print("[Enter 'P'] for Price Graph")
        print("[Enter 'D'] for Description Graph ")
        c=input("Kindly Enter Your Choice :")
        
        m=df["Vehicle Model Name"]
        e=df["Engine Disp."]
        ts=df["Top Speed"]
        a=df["Acceleration"]
        p=df["Power"]
        t=df["Torque"]
        pr=df["Price (in $)"]
        
        if c=="p" or c=="P":

            plt.hist(pr,width=1,ec='w',color='k')
            plt.xlabel("Price")
            plt.title("Vehicle Statistics")
            plt.show()

        elif c=="d" or c=="D":
            
            plt.hist(e,width=10,ec='w',color='maroon',label="Engine Disp.")
            plt.title("Engiine Displacement")
            plt.show()
            plt.hist(ts,width=50,ec='w',color='darkorchid',label="Top Speed")
            plt.title("Top Speed")
            plt.show()
            plt.hist(a,width=50,ec='w',color='lightpink',label="Acceleration")
            plt.title("Acceleration")
            plt.show()
            plt.hist(p,width=50,ec='w',color='mediumvioletred',label="Power")
            plt.title("Power")
            plt.show()
            plt.hist(t,width=50,ec='w',color='magenta',label="Torque")
            plt.title("Toque")
            plt.show()

        else:
            print("Sorry, Your responce is not acceptable")
            HISTO()

#BUYING ITEMS

def SHOP():
    print("Welcome to the SHOP")
    shop=pd.read_csv("E:\\Yash\\Pro Project\\Main\\Shop.csv")


ENTRY()
