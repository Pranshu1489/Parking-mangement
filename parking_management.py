import os
import platform
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="#Mrverma1489", database = "park")
mycursor=mydb.cursor()
def Add_Record():
               L=[]
               pid1=int(input("Enter the parking number : "))
               L.append(pid1)
               pname1=input("Enter the Parking Name: ")
               L.append(pname1)
               level1=input("Enter level of parking : ")
               L.append(level1)
               freespace1=input("Is there any free space available or not :YES/NO ")
               L.append(freespace1)
               vehicleno1=input("Enter the Vehicle Number : ")
               L.append(vehicleno1)
               vehmodel1=input("Enter the vehicle model:")
               L.append(vehmodel1)
               nod1=int(input("Enter total number of days for parking: "))
               L.append(nod1)
               payment1=int(input("Enter total payable amount : "))
               L.append(payment1)
               stud=(L)
               sql="insert into parkmaster11 (pid1,pnm1,level1,freespace1,vehicleno1,vehmodel1,nod1,payment1) values (%s,%s,%s,%s,%s,%s,%s,%s)"
               mycursor.execute(sql,stud)
               mydb.commit()
                
def RecView():
               def abcd():
                              sql = "select * from parkmaster11"
                              mycursor.execute(sql)
                              res = mycursor.fetchall()
                              print("Details about Parking are as follows :")
                              print("(Parking Id,Parking Name,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
                              for x in res:
                                             print(x)
               abcd()
               
def Vehicle_Detail():
               L=[]
               vid1=input("Enter Vehicle No : ")
               L.append(vid1)
               vnm1=input("Enter Vehicle Name/Model Name : ")
               L.append(vnm1)
               dateofpur1=input("Enter Date of purchase : ")
               L.append(dateofpur1)
               vdt=(L)
               sql="insert into vehicle (vid1,vnm1,dateofpur1) values (%s,%s,%s)"
               mycursor.execute(sql,vdt)
               mydb.commit()
               
def Vehicle_View():
               def abcd():
                              sql = "select * from vehicle"
                              mycursor.execute(sql)
                              res = mycursor.fetchall()
                              print("Details about Vehicle are as follows :")
                              print("Vehicle Id, Vehicle Name, Date of Purchase")
                              for x in res:
                                             print(x)
               abcd()
               
def remove_vehicle():
               vid1= input("Enter the vehicle number of the vehicle to be deleted : ")
               rv=(vid1)
               sql="Delete from vehicle where vid1=%s"
               mycursor.execute(sql,rv)
               print(vid1,"SUCCESSFULLY DELETED FROM VEHICLE !!!")
               mydb.commit()
               
def remove_parking():
               pid1=input("Enter the parking number to be deleted : ")
               rp = (pid1)
               sql="Delete from parkmaster11 where pid1=%s"
               mycursor.execute(sql,rp)
               print(pid1,"SUCCESSFULLY DELETED FROM PARKMASTER11 !!!")
               mydb.commit()
              
def Details():
               def abcd():
                              sql = "Select parkmaster11.pid1, parkmaster11.pnm1, parkmaster11.level1,parkmaster11.nod1,parkmaster11.payment1,vehicle.vid1,vehicle.vnm1,vehicle.dateofpur1 from parkmaster11,vehicle where parkmaster11.vehicleno1=vehicle.vid1"
                              mycursor.execute(sql)
                              res = mycursor.fetchall()
                              print(" All Details are as follows :")
                              print("Parking Id, Parking Name, Level, No of Days for Parking, Payment, Vehicle Id, Vehicle Name, Date of Purchase")
                              for x in res:
                                             print(x)
               abcd()

def create_database():
                
               print(" Creating Parkmaster11 table")
               sql = "CREATE TABLE if not exists parkmaster11 (pid1 int(4) not null PRIMARY KEY,pnm1 varchar(30),level1 varchar(30),freespace1 varchar(4),vehicleno1 varchar(30),vehmodel1 varchar(30),nod1 int(2),payment1 int(9));"
               mycursor.execute(sql)
               print(" Parkmaster11 table created")
               print(" Creating  vehicle table")
               sql = "CREATE TABLE if not exists vehicle (vid1 varchar(30) not null primary key, vnm1 varchar(30),dateofpur1 date );"
               mycursor.execute(sql)
               print(" Vehicle table created")

def list_database():
                
               sql="show tables;"
               mycursor.execute(sql)
               for i in mycursor:
                              print(i)


def db_mgmt( ):
           while True :
                      print("\t\t\t 1. Database creation")
                      print("\t\t\t 2. List Database")
                      print("\t\t\t 3. Back (Main Menu)")
                      p=int (input("\t\tEnter Your Choice :"))
                      if p==1 :
                                 create_database()
                      if p==2 :
                                 list_database()
                      if p== 3 :
                                 break 
               



def Menu():
               print("Enter1 : Database setup")
               print("Enter2 : To Add Parking Detail")
               print ("Enter3 : To Remove Parking Record")
               print("Enter4 :  To view Parking List")
               print("Enter5 :  To Add Vehicle Detail")
               print("Enter6: To Remove Vehicle Record")
               print("Enter7: To  View Vehicle List")
               print("Enter8 : To View All Details")
               
               try: 
                              userInput = int(input("Please Select An Above Option: ")) 
               except ValueError:
                              exit("\nHy! That's Not A Number") 
               if(userInput==1):
                              db_mgmt( )
               if (userInput== 2):
                              Add_Record()
               elif (userInput==3):
                              remove_parking()
               elif (userInput==4):
                                RecView()
               elif (userInput==5):
                              Vehicle_Detail()
               elif (userInput==6):
                              remove_vehicle()
               elif (userInput==7):
                              Vehicle_View()
               elif (userInput==8):
                              Details()
               else:
                              print("Enter correct choice. . . ")

print("-"*125)
print("* * * * * * * * * * * * * * * * * WELCOME TO PARKING MANAGEMENT* * * * * * * * * * * * * * * * *")
print("-"*125)
Menu()

def runAgain():
               runAgn = input("\nwant To Run Again Y/n: ")
               if runAgn == 'y':
                              Menu()
                              userInput = int(input("Please Select An Above Option: "))
                              
                              if(userInput==1):
                                             db_mgmt( )
                              if (userInput== 2):
                                             Add_Record()
                              elif (userInput==3):
                                             remove_parking()
                              elif (userInput==4):
                                             RecView()
                              elif (userInput==5):
                                             Vehicle_Detail()
                              elif (userInput==6):
                                             remove_vehicle()
                              elif (userInput==7):
                                             Vehicle_View()
                              elif (userInput==8):
                                             Details()
                              else:
                                             print("Enter correct choice. . . ")
               else:
                              runAgain()

 
runAgain()
