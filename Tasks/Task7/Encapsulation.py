""" The below code shows the use of Encapsulation(public variable)"""
import logging
logging.basicConfig( filename = "Encapsulation.log", level=logging.DEBUG, format = '%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s' )
try:
    class ineuron:
        def __init__(self):
            self.student = "data science"
        def students(self):
            print(self.student)


    print("---Public variable---")
    i = ineuron()
    i.students()
    i.student = "data analytics"
    i.students()
    print("------------------------")

except Exception as e:
    logging.exception(e)





""" The below code shows the use of Encapsulation(protected variable)"""
import logging
logging.basicConfig( filename = "Encapsulation.log", level=logging.DEBUG, format = '%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s' )
try:
    class ineuron:
        def __init__(self):
            self._student = "data science"
        def students(self):
            print(self._student)


    print("---Protected variable---")
    i = ineuron()
    i.students()
    i._student = "data analytics"
    i.students()
    print("------------------------")

except Exception as e:
    logging.exception(e)




""" The below code shows the use of Encapsulation(private variable)"""
import logging

logging.basicConfig(filename="Encapsulation.log", level=logging.DEBUG,format='%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s')
try:
    class ineuron1:
        def __init__(self):
            self.__student = "data science"
        def students(self):
            print(self.__student)
        def student_change(self):
            self.__student = "big data by me"


    print("---Protected variable---")
    i1 = ineuron1()
    i1.students()
    i1.__student = "big data"
    i1.students()
    i1.student_change()
    i1.students()
    print("------------------------")
except Exception as e:
    logging.exception(e)