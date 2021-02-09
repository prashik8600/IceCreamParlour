import pymysql
from datetime import date

connection = ""
cur =""
global dt,pitemcode,fadd

dt=date.today()
str(dt)

def connectdb():
    global connection, cur
    connection = pymysql.connect(host="localhost", user="root", password="", database="icecream2")
    cur=connection.cursor ()
    print("Database is Connected")


def disconnectDB():
    cur.close()
    connection.close()
    print("Database Disconnected.")

def insertdata(name,id,dt,add):
    try:
    sql = "INSERT INTO data2 (name, pitemcode,date,bill) VALUES (%s,%s,%s,%s);"
    val=(name,id,dt,add)
    cur.execute(sql, val)
    connection.commit()
        return True
    except:
        return False

def updatebill(add,name):
    # try:
    #     sql = "UPDATE data2 SET bill=%s,  WHERE name = %s;"
    #     cur.execute(sql, (name,bill))
    #     connection.commit()
    #     return True
    # except:
    #     return False
    pass
def fetchname(namef):
    
    sql = "SELECT * from data2 WHERE name = %s;"
    h
    print ("{:<8} {:<6} {:<11} {:<12} {:<5} ".format('SRNo','NAME','PURCHASEID','DATE','BILL'))
    for i,j,k,l,m in data:
	    print ("{}\t {}\t {}\t {}\t {}".format(i,j,k,l,m))
def deleteuser(named):
    try:
        sql = "DELETE FROM data2 WHERE name=%s;"
        cur.execute(sql, (named, ))
        connection.commit()
        return True
    except:
        return False

def showdata():
    select_query = "SELECT * FROM data2;"
    cur.execute(select_query)
    data = cur.fetchall()
    print ("{:<9} {:<6} {:<11} {:<12} {:<5} ".format('SRNo','NAME','PURCHASEID','DATE','BILL'))
    for i,j,k,l,m in data:
	    print ("{}\t {}\t\t {}\t {}\t {}".format(i,j,k,l,m))
    
def order():
    global name 
    add=0
    name = input("Continue with your name:")
    # count = int(input("how many ice-creams do you want to purchase:"))
    while True:
        id = int(input("Enter Product Id:"))
        if id in d.keys():
            lst2.append(id)
            d2.update(name=lst2)
            print(d2)
        else:
            print("Invalid Purchase ID!!")
            
        more = input("Add More?(y/n):")
        if more == 'n' or more == 'N':
            bills = input("Want to generate Bill?(y/n)")
            if bills == 'y' or bills == 'Y':
                for key, value in d.items():
                    for i, j in d2.items():
                        for k in j:
                            if key == k:
                                add += value[1]
            else:
                break
            for key, value in d.items():
	            for i, j in d2.items():
		            if j[0]==key:
			            item1=(value[0]) 
            for key, value in d.items():
	            for i, j in d2.items():
		            if j[0]==key:
			            item2=(value[1])  
            connectdb()
            insertdata(name,id,dt,add)
            disconnectDB() 

            print("**************************************Thnak You****************************************************")              
            print("ORDER : {}                        COST : {}\n\n\n\n\n\n\n\n\n                               TOTAL AMOUNT:{}".format(item1,item2,add)) 
            print("***************************************Visit Again**************************************************")                  
            sol=input("Book another fresh order?(y/n)")
            if sol=='y' or 'Y':
                lst2.clear()
                showmenu()
        else:
            continue
        lst2.clear()
        item1=""
        item2=""
        
    else:
        showmenu()
def todayscust(dt):
    sql = "SELECT * from data2 WHERE date = %s;"
    cur.execute(sql, dt)
    data = cur.fetchall()
    print ("{:<8} {:<6} {:<11} {:<12} {:<5} ".format('SRNo','NAME','PURCHASEID','DATE','BILL'))
    for i,j,k,l,m in data:
	    print ("{}\t {}\t {}\t {}\t {}".format(i,j,k,l,m))
       

def showmenu():
    
    print("{:<10} {:<15} {:<10} ".format('productID', 'Flavour', 'Prize'))
    print("-------------------Menu-------------------------")
    for key, value in d.items():
        flavour, prize = value
        print("{:<10} {:<15} {:<10} ".format(key, flavour, prize))
    print("--------------------------------------------")
    od = input("Want ot order Something?(y/n)")
    if od == 'y' or od == 'Y':
        order()
    else :
        exit()


d = {100: ['strawberry', 45],
     101: ['butterscoth', 45],
     102: ['Milkshake', 55],
     103: ['Vannila', 45],
     104: ['Chocolate', 50],
     105:['Bannana',30],
     106:['Cherry',45],
     107:['Apple',40],
     108:['Lemon',40]}
d2 = {}
lst2 = []
while True:
    print("------------------------------------Welcome To Ice-Cream Parlour-----------------------------------------\n\n")
    print('''\t*******************************************\n
              1.Order the Ice_Cream\n
              2.Show today's customer details\n
              3.Show overall Data of shop\n
              4.Fetch data using name\n
              5.Delete data of user(permanent Deletion!)\n
              6.Exit \n
              *********************************************''')
    ch = int(input("Enter the choice:"))
    if ch == 1:
        showmenu()
    elif ch == 2:
        connectdb()
        todayscust(dt)
        disconnectDB()
    elif ch == 3:
        connectdb()
        showdata()
        disconnectDB()
    elif ch==4:
        connectdb()
        namef=input("History Of User (Enter name):")
        fetchname(namef)
        disconnectDB()
    elif ch==5:
        print("WARNING:Data Will be Deleted Permanently from Database:")
        named=input("Enter the name of user Here:")
        connectdb()
        deleteuser(named)
        print("Record Deleted Successfully")
        disconnectDB()
    elif ch == 6:
        exit()
    else:
        print("Invalid Choice..")




