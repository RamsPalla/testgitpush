""" The below code shows the use of Polymorphism"""
"""In the below code, function "test(a,b)" does both addition and concatenation depending upon data passed in it"""
"""Similarly, in the below code, function "ineuron_external" throws output differently when data passed in it is different, which is called polymorphism"""
import logging
logging.basicConfig( filename = "Polymorphism.log", level=logging.DEBUG, format = '%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s' )
try:
    class ineuron:
        def students(self):
            print("print a student details")
    class class_type:
        def students(self):
            print("print the class type of students")
    def ineuron_external(a):
        a.students()
    i = ineuron()
    j = class_type()
    ineuron_external(i)
    ineuron_external(j)
    def test(a,b):
        return a+b
    print(test(3,4))
    print(test("sudhanshu", "kumar"))
except Exception as e:
    logging.exception(e)