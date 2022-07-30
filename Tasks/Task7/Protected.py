""" The below code shows the use of protected variable. Trying to display student details who has scored top rank and whose class name is different from the current class """
import logging
logging.basicConfig( filename = "protected.log", level=logging.DEBUG, format = '%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s' )
try:
    class class1:
        _name = "Rambabu"
        _batch = "FSDS Bootcamp"
        _emailid = "palla.r7@gmail.com"
    Rambabu = class1()
    class class2(class1):
        def __init__(self, name, batch, emailid):
            self.name = name
            self.batch = batch
            self.emailid = emailid
    Padya = class2("Padya", "MLDL1", "its437@yahoo.co.in")
    Kaavyansh = class2("Kaavyansh", "MLDL2", "its437@rediffmail.com")
    logging.info(" current batch students wants to know the previous batch top ranker, so please display his details %s %s %s ", Rambabu._name, Rambabu._batch, Rambabu._emailid)

except Exception as e:
    logging.exception(e)