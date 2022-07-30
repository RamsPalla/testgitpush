""" The below code shows the use of method overriding"""
import logging
logging.basicConfig( filename = "methodoverriding.log", level=logging.DEBUG, format = '%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s' )
try:
    class class1:
        def __init__(self):
            self.name = "Rambabu"
        def methodoverride(self):
            print(self.name)
    Rambabu = class1()
    class class2(class1):
        def __init__(self):
            self.name = "Padya"
        def methodoverride(self):
            print(self.name)

    Padya = class2()
    logging.info(" mehtod in child class 'class2' has overrided method in parent class 'class1' %s")
    Padya.methodoverride()

except Exception as e:
    logging.exception(e)

#https://www.geeksforgeeks.org/method-overriding-in-python/?ref=lbp
