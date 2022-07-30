#1st day of OOPS

#class Person:
    #pass


#class Person:
    #def __init__(self,name,surname, emailid,year_of_birth):
        #self.name = name
        #self.surname = surname
        #self.emailid = emailid
        #self.year_of_birth = year_of_birth

#anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994)
#sudh = Person("sudhanshu", "kumar", "sudhanshu@gmail.com", 23424)
#gargi = Person("gargi", "xyz", "gargi@gmail.com", 234242)
#print(anuj_var.name)
#print(anuj_var.surname)
#print(anuj_var.emailid)
#print(anuj_var.year_of_birth)
#print(sudh.year_of_birth)
#print(gargi.surname)
#print(type(sudh))




#class Person:
    #def __init__(rams,name,surname, emailid,year_of_birth):
        #rams.name = name
        #rams.surname = surname
        #rams.emailid = emailid
        #rams.year_of_birth = year_of_birth
    #def age(rams, current_year):
        #return current_year-rams.year_of_birth

#anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994)
#sudh = Person("sudhanshu", "kumar", "sudhanshu@gmail.com", 1985)
#gargi = Person("gargi", "xyz", "gargi@gmail.com", 1975)
#print(anuj_var.name)
#print(anuj_var.surname)
#print(anuj_var.emailid)
#print(anuj_var.year_of_birth)
#print(sudh.year_of_birth)
#print(gargi.surname)
#print(type(sudh))
#print(sudh.name + sudh.surname)
#print(sudh.age(2022))



#the below shows us that latest constructor(in this case constructor with just name, surname and year_of_birth) in the code is considered for execution:
#class Person :

    #def __init__(sudh,name,surname , emailid , year_of_birth):
        #sudh.name1 = name
        #sudh.surname = surname
        #sudh.emailid = emailid
        #sudh.year_of_birth = year_of_birth

    #def __init__(sudh,name,surname, year_of_birth):
        #sudh.name1 = name
        #sudh.surname = surname
        #sudh.year_of_birth = year_of_birth

    #def age(sudh , current_year,year_of_birth):
        #return current_year - year_of_birth

#anuj_var  = Person("anuj" , "bhandari", 1985)
#sudh = Person("sudhanshu " ,"kumar", 1986)
#gargi = Person("gargi" , "xyz", 1987)
#print(anuj_var.age(2022,1985))




#class Person:

    #def age(rams, current_year, year_of_birth):
        #return current_year-rams.year_of_birth
    #def email_id_input(self, email_id):
        #print("take email id from a Person and print it", email_id)
    #def ask_name(self):
        #name = print("tell me your name")
        #return name
    #def ask_dob(self):
        #dob = input("tell me your date of birth")
        #return dob
#anuj = Person()
#sudh = Person()
#gargi = Person()
#sudh.email_id_input("sudhanshu@gmail.com")
#print(gargi.ask_dob())





#2nd day of OOPS

#"_" denotes "protected" variable
#"__" denotes "private" variable
#class person:
    #def __init__(self, name, surname, yob):
        #self._name = name
        #self.__surname = surname
        #self.yob = yob
#sudh = person("sudhanshu", "kumar", 1990)
#print(sudh._name)
#print(sudh._person__surname)




#class person:
    #_name = "sudh"
    #__surname = "kumar"
    #yob = 1990
#obj = person()
#print(obj)
#class employee(person):
    #pass
#obj1 = employee()
#print(obj1)
#print(obj1.yob)
#print(obj1._name)
#print(obj1._person__surname)




#class person:
    #_name = "sudh"
    #__surname = "kumar"
    #yob = 1990
    #def _age(self, current_year):
        #return current_year-self.yob
    #def __age1(self, current_year):
        #return current_year-self.yob
#obj = person()
#print(obj)
#print(obj._age(2022))
#print(obj._person__age1(2022))
#class employee(person):
    #_name = "sudhanshu"
    #__surname = "singh"
    #yob = 1991
#obj1 = employee()
#print(obj1)
#print(obj1.yob)
#print(obj1._name)
#print(obj1._person__surname)
#print(obj1._age(2022))
#print(obj1._person__age1(2022))




#below code imports "test1" python file to "test2" python file(where we writing the code)
#import test1
#obj = test1.person1("sudhanshu", "kumar", 1994)
#below code imports class "person" from "test1" python file to "test2" python file(where we writing the code)
#from test1 import person
#below code imports class "person" from "utils1" python file(module) from "utils" (package)
#from utils.utils1 import person



#Inheritance:


#concept of simple inheritance
#class car:
    #def __init__(self, body, engine, tyre):
        #self.body = body
        #self.engine = engine
        #self.tyre = tyre
    #def mileage (self):
        #print("mileage of this car")
#c = car("solid", "V6", "radial")
#print(c)
#class tata(car):
    #pass
#t = tata("solid1", "V8", "radial1")
#print(t)
#print(t.mileage())




#concept of "multi-level" inheritance
#class bank:
    #def transaction(self):
        #print("total transaction value")
    #def acc_opening(self):
        #print("this will show you status of your account")
    #def deposite(self):
        #print("this will show deposited amount")

#class HDFC_bank(bank):
    #def hdfc_to_icici(self):
        #print("this will show you all the transactions from hdfc to icici")
#class icici(HDFC_bank):
    #pass
#i = icici()
#i.hdfc_to_icici()
#i.deposite()
#i.acc_opening()
#i.transaction()




#concept of "multiple" inheritance. Below code shows how inheritance works during conflict between functions(functions with same name) that were defined in two different classes
#class bank:
    #def transaction(self):
        #print("total transaction value")
    #def acc_opening(self):
        #print("this will show you status of your account")
    #def deposite(self):
        #print("this will show deposited amount")
    #def test(self):
        #print("this is test method from class bank")

#class HDFC_bank:
    #def hdfc_to_icici(self):
        #print("this will show you all the transactions from hdfc to icici")
    #def test(self):
        #print("this is test method from class HDFC_bank")
#class ineuron_bank:
    #def acc_status_icici(self):
        #print("print account status in icici")

#class icici(bank, HDFC_bank, ineuron_bank):
    #pass
#class icici1(HDFC_bank, bank, ineuron_bank):
    #pass
#i = icici()
#i1 = icici1()
#i.hdfc_to_icici()
#i.deposite()
#i.acc_opening()
#i.transaction()
#i.test()
#i1.test()
#i.acc_status_icici()



#method overriding
#class ineuron:
    #def student(self):
        #print("details of all the students")
    #def achievers(self):
        #print("print the list of all achievers")
    #def hall_of_fame(self):
        #print("print everyone from all of fame")
#class ineuron_vision(ineuron):
    #def student(self):
        #print("this is the list of filtered students")
#iv = ineuron_vision()
#iv.student()



#data abstraction(data hiding/variable hiding)
#class ineuron:
    #__students = "data science"
    #def students(self):
        #print("print the class of these students:", ineuron.__students)
#i = ineuron()
#i.students()
#print(i._ineuron__students)




#Encapsulation: we can change the values of variables using users(objects) if the valriable is public. However, we can't change the value of private variable using objects, instead we should use methods(functions) to do the same.
#class ineuron:
    #def __init__(self):
        #self.student = "data science"
    #def students(self):
        #print(self.student)
#i = ineuron()
#i.students()
#i.student = "data analytics"
#i.students()



#class ineuron1:
    #def __init__(self):
        #self.__student = "data science"
    #def students(self):
        #print(self.__student)
    #def student_change(self):
        #self.__student = "big data by me"
#i1 = ineuron1()
#i1.students()
#i1.__student = "big data"
#i1.students()
#i1.student_change()
#i1.students()




#polymorphism:
#In the below code, function "test(a,b)" does both addition and concatenation depending upon data passed in it
#Similarly, in the below code, function "ineuron_external" throws output differently when data passed in it is different, which is called polymorphism
#class ineuron:
    #def students(self):
        #print("print a student details")
#class class_type:
    #def students(self):
        #print("print the class type of students")
#def ineuron_external(a):
    #a.students()
#i = ineuron()
#j = class_type()
#ineuron_external(i)
#ineuron_external(j)
#def test(a,b):
    #return a+b
#print(test(3,4))
#print(test("sudhanshu", "kumar"))





#Below entire code is live class code(by sudhanshu) which is similar to code above

#class person :
    #def __init__(self , name ,surname , yob):
        #self._name1 = name
        #self.__surname1 = surname
        #self.yob1 = yob

#sudh = person("sudhanshu" , "kumar" , 1990)
#print(sudh._name1)
#print(sudh._person__surname1)




#class person :

    #_name = "sudh"
    #__surname = "kumar"
    #yob = 1990

    #def _age(self , current_year ):
        #return current_year - self.yob
    #def __age1(self , current_year ):
        #return current_year - self.yob

#obj = person()
#print(obj._age(2022))
#print(obj._person__age1(2022))

#class employee(person) :
    #_name = "sudhanshu"
    #__surname = "singh"
    #yob = 1991

#obj1 = employee()
#print(obj1._age(2022))
#print(obj1._person__age1(2022))
#print(obj1)
#print(obj1.yob)
#print(obj1._name)
#print(obj1._employee__surname)



#test1.py
#======================================
#from utils.utill1 import person2

#obj = person2("sudhansu " , "kumar" , 345345)
#print(obj.yob1)

#class person1 :
    #def __init__(self , name ,surname , yob):
        #self._name1 = name
        #self.__surname1 = surname
        #self.yob1 = yob

#sudh = person1("sudhanshu" , "kumar" , 1990)
#print(sudh._name1)
#print(sudh._person1__surname1)




#utills1.py
#===================================
#class person2:
    #def __init__(self , name ,surname , yob):
        #self._name1 = name
        #self.__surname1 = surname
        #self.yob1 = yob

#sudh = person2("sudhanshu" , "kumar" , 1990)
#print(sudh._name1)
#print(sudh._person2__surname1)



#test2.py
#=============================================
#import test1
#print(test1)
#obj3 = test1.person1("sudhanshu" , "kumar" , 1994)
#print(obj3.yob1)
#print(obj3._name1)
#print(obj3._person1__surname1)


#class person :

    #_name = "sudh"
    #__surname = "kumar"
    #yob = 1990

    #def _age(self , current_year ):
        #return current_year - self.yob
    #def __age1(self , current_year ):
        #return current_year - self.yob

#obj = person()
#print(obj._age(2022))
#print(obj._person__age1(2022))

#class employee(person) :
    #_name = "sudhanshu"
    #__surname = "singh"
    #yob = 1991

#obj1 = employee()
#print(obj1._age(2022))
#print(obj1._person__age1(2022))
#print(obj1)
#print(obj1.yob)
#print(obj1._name)
#print(obj1._employee__surname)

#https://github.com/drsunithaev/OOP_Ex/blob/main/DataStructures_Qn.py
#https://github.com/atharv4git/Ineuron/tree/main/tasks/task4
#https://github.com/BokkisamRohit/task6_02-07-2022/blob/main/stringTasks.py
#https://github.com/BokkisamRohit/task6_02-07-2022/blob/main/listTasks.py
#https://github.com/udayavel/FSDS/blob/main/ds_class.py
#https://github.com/piyush-123/Tasks/blob/main/Task_02Jul2022.py
#https://github.com/piyush-123/Tasks/blob/main/Task_02Jul2022.py
#https://github.com/Arunava-Biswas/Ineuron-FSDS/blob/main/Live%20Classes/Class%20work/task/test.py

#https://github.com/anilpadiyar/Assignment/blob/main/oops1_Task.py
#https://github.com/AnkurYadav00/challenges/blob/main/List_s.py
#https://github.com/AnkurYadav00/challenges/blob/main/Dict_s.py
#https://github.com/AnkurYadav00/challenges/blob/main/String_s.py
#https://github.com/AnkurYadav00/challenges/blob/main/Tuple_s.py



