#import mysql.connector as conn

#mydb = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1")
#print(mydb)
#cursor = mydb.cursor()
#cursor.execute("show databases")
#print(cursor.fetchall())


#import mysql.connector as conn

#mydb = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1")
#print(mydb)
#cursor = mydb.cursor()
#cursor.execute("create database sudhanshu")
#print(cursor.fetchall())


#import mysql.connector as conn

#mydb = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1")
#print(mydb)
#cursor = mydb.cursor()
#cursor.execute("create table sudhanshu.ineuron(employee_id int(10), emp_name varchar(80), emp_mailid varchar(255), emp_salary int(10), emp_attendence int(30))")
#cursor.execute("show databases")
#print(cursor.fetchall())



#import mysql.connector as conn

#mydb = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1")
#print(mydb)
#cursor = mydb.cursor()
#print(cursor.execute("select * from sudhanshu.ineuron"))




#import mysql.connector as conn

#mydb = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1")
#cursor = mydb.cursor()
#s = "insert into sudhanshu.ineuron values(101, 'rams', 'palla.r7@gmail.com', 100, 30)"
#cursor.execute(s)
#mydb.commit()
#cursor.execute("select * from sudhanshu.ineuron")
#for i in cursor.fetchall():
    #print(i)



#import mysql.connector as conn

#mydb = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1")
#cursor = mydb.cursor()
#cursor.execute("select employee_id, emp_mailid from sudhanshu.ineuron")
#l = []
#for i in cursor.fetchall():
    #l.append(i)
#print(l)
#print(type(l))
#print(type(l[0]))






