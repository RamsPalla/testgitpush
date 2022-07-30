#n = 6
#for i in range(n):
    #if i <= (n-1):
        #print("rambabu "*i, end = " ")
        #print("\n")



#n = 3
#for i in range(n):
    #if i <= (n-1):
        #print(("rambabu       "*(i+1)).center(41,' '))
#n = 2
#for i in range(n):
    #if i == (n-2):
        #print(("rambabu       "*(i+2)).center(41,' '))
#n = 1
#for i in range(n):
    #if i == (n-1):
        #print(("rambabu       "*(i+1)).center(41,' '))



#n = int(input("enter number"))
#for i in range(n):
    #if i <= 3:
        #n = i
    #else:
        #n = 6 - i
    #print(("ineuron "*n).center(30,' '))




#m = int(input("enter number"))
#c = ((m+1)/2)
#d = int(((7*c)+c))
#for i in range(m+1):
    #if i <= c:
        #n = i
    #else:
        #n = m-i+1
    #print(("ineuron "*n).center(d,' '))


#n = int(input("enter number"))
#a = 1
#b = 1
#l = []
#for i in range(n):
    #l.append(a)
    #a,b = b, b+a
#print(l)

#def prime(a,b):
    #l = []
    #for i in range(a,b+1):
        #if i>1:
            #for j in range(2,i):
                #if i%j == 0:
                    #break
            #else:
                #l.append(i)
    #print(l)
#prime(1,1000)



#f1 = open("D:/today1.txt", 'r')
#print(f1.read())
#f1.close()



#class list:
    #def sum(self, l):
        #sum = 0
        #for i in l:
            #sum = sum+i
        #return sum
    #def mul(self,l):
        #mul = 1
        #for i in l:
            #mul = mul*i
        #return mul
#rams = list()
#gow = list()
#print(rams.sum([1,2,3,4]))
#print(gow.mul([1,2,3,4]))



#import logging
#logging.basicConfig(filename = "exceptionloggingclass.txt", level = logging.DEBUG, format = '%(name)s %(asctime)s %(levelname)s %(message)s')
#class list:
    #def sum(self, l):
        #sum = 0
        #for i in l:
            #sum = sum+i
        #return sum
    #def mul(self,l):
        #mul = 1
        #for i in l:
            #mul = mul*i
        #return mul
#rams = list()
#gow = list()
#try:
    #print(rams.sum("str"))
#except Exception as e:
    #logging.info("please enter list ")
    #logging.exception(e)
    #print("TypeError")
#try:
    #print(gow.mul([1,2,3,4]))
#except Exception as e:
    #logging.exception(e)





#import logging
#logging.basicConfig(filename = "exceptionloggingclass.txt", level = logging.DEBUG, format = '%(name)s %(asctime)s %(levelname)s %(message)s')
#class basic:
    #def __init__(list, name, age, place):
        #list.name = name
        #list.age = age
        #list.place = place
#rams = basic("Rambabu", 37, "chinakudama")
#gow = basic("gowthami", 35, "sikhabadi")
#try:
    #print(rams.name)
#except Exception as e:
    #logging.exception(e)
#try:
    #print(gow.place)
#except Exception as e:
    #logging.excepti(e)
#try:
    #print(gow.age)
#except Exception as e:
    #logging.excepti(e)









#Start of the code to see how 'iter' and 'next' works
#l = [1,2,3,4]
#a = iter(l)
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#end of the code to see how 'iter' and 'next' works

#f = open("C:/Users/Rambabu/rambabu.txt", 'w')
#f.write("this is my frist pycharm file creation")
#f.close()
#f1 = open("C:/Users/Rambabu/rambabu1.txt", 'w')
#f1.write("this is my second pycharm file creation to learn read function")
#f1.seek(0)
#f1.tell()
#%%writefile rambabu2.txt
#this code is to learn writing code to write filecmp
#that all for now


#l = [1,2]
#def sq(n):
    #return n**2
#print(list(map(sq,l)))

#l = [1,2]
#print(list(map(lambda x: str(x), l)))


#def sum():
    #a = int(input("enter the first number"))
    #l = 0
    #for i in range(a):
        #l = l+i
    #return l
#print(sum())


#from functools import reduce
#l = [1,2,3,4,5,6]
#print(reduce(lambda a,b : a+b, l))

#l = [1,2,3,4,5,6]
#print(reduce(lambda a,b : a*b, l))

#l = [1,2,3,4,5,6]
#print(list(filter(lambda x: x%2, l)))

#l = [1,2,3,4,5,6]
#print(list(filter(lambda x: x%2 == 0, l)))


#l = [1,2,3,4,5,6]
#def check_even(n):
    #if n%2 == 0:
        #return True
#print(list(filter(check_even, l)))


#l = [1,2,3,4,5,6]
#def check_odd(n):
    #if n%2 != 0:
        #return True
#print(list(filter(check_odd, l)))

#def check_odd(n):
    #if n%2 != 0:
        #return True
#print(list(filter(check_odd, [1,2,3,4])))


#import mysql.connector as conn
#db = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1", db = "")
#cursor = db.cursor()
#cursor.execute("sql query")








