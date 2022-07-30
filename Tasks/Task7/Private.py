""" The below code shows the use of private variable. Trying to display student details who has scored top rank and whose class name is different from the current class """
import logging
logging.basicConfig( filename = "private.log", level=logging.DEBUG, format = '%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s' )
try:
    class class1:
        __name = "Rambabu"
        __batch = "FSDS Bootcamp"
        __emailid = "palla.r7@gmail.com"
    Rambabu = class1()
    class class2(class1):
        def __init__(self, name, batch, emailid):
            self.name = name
            self.batch = batch
            self.emailid = emailid
    Padya = class2("Padya", "MLDL1", "its437@yahoo.co.in")
    Kaavyansh = class2("Kaavyansh", "MLDL2", "its437@rediffmail.com")
    logging.info(" current batch students wants to know the previous batch top ranker, so please display his details %s %s %s ", Rambabu._class1__name, Rambabu._class1__batch, Rambabu._class1__emailid)

except Exception as e:
    logging.exception(e)