import mysql.connector as con

db=con.connect(host="localhost", user="root", password="Ayush24")

cur=db.cursor()
cur.execute("show databases")
database=cur.fetchall()
c=0

for i in database:
    if "echallan1" in i:
        print("*************************GOVERNMENT OF INDIA***************************")
        print("                            GUJARAT POLICE                               ")
        print("                                                                         ")
        print("                            CHALLAN DETAILS                              ")
        cur.execute("use echallan1")
        c=1
        break
    
if c==0:
        cur.execute("Create database echallan1")
        cur.execute("use echallan1")
        cur.execute("create table challan(Echallan_No int primary key,date date, time varchar(10),vehicle_no varchar(15),State varchar(10),Location varchar(15),reason varchar(50),challan_amount int(15),payment_mode varchar(30))")
        cur.execute("create table validity(vehicle_no int(10),due_date date)")

def challan():
            Echallan_No=input("Enter Echallan Number")
            date=input("Enter Date")
            time=input("Enter Time")
            vehicle_no=input("Enter Vehicle No")
            State =input("Enter State")
            Location=input("Enter Location")
            reason=input("Enter Reason")
            amount=input("Amount For Cause")
            payment=input("Enter Payement Mode")
            q1="insert into challan values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(Echallan_No,date,time,vehicle_no,State,Location,reason,amount,payment)
            cur.execute(q1,val)
            db.commit()

def validity():
    vehicle_no=input("Enter Vehicle No")
    incident_date=input("Enter Incident Date")
    validity=input("This Challan Form Will Be Invalid After One Week Of Incident")
    q2="insert into validity values(%s,%s,%s)"
    val=(vehicle_no,validity,penalty)
    cur.execute(q2,val)
    db.commit()
    
def amount():
    vn=input("Enter vehicle number")
    q1="select  * from challan"
    cur.execute(q1)
    d=cur.fetchall()
    for data in d:
        if vn in data:
            print("\n1Reason",data[6],"\n2Amount",data[7])
    
        else:
            print("---------------RECORD DOES NOT EXIST-----------------")
           
def precautions():
    print("\n1.Do not drink and drive\n2.Keep a safe distance from vehicles!\n3.Drive within the speed limits.")
    
    
while True:    
    print("\n1. Make Challan\n2.Track old records\n3.Precaution\n4.validity\n5.Generate Challan")
    ch=int(input("Enter your choice"))
    if ch==1:
        challan()
    elif ch==2:
        amount()
    elif ch==3:
        precautions()
    elif ch==4:
        validity()
    elif ch==5:
         cur.execute("select * from challan")
         c=cur.fetchall()
         name=input("Enter vehicle number")
         for i in c:
                if i[2].upper()==name.upper():
                   file=open("challan.txt","w")
                   print("*********************GOVERNMENT OF INDIA***************************")
                   s="Vehicle No:"+str(i[2])+"\nDate:"+str(i[0])+"\nTime:"+str(i[1])+"\nLocation:"+str(i[5])+"\nReason:"+str(i[6])
                   file.write(s)
                   file.close()
    else:
            print("Wrong choice")
            break