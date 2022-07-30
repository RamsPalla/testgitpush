"""" The below code shows best use of constructor in OOPS_Class to print student details in ineuron against specific batch"""
import logging
logging.basicConfig(filename="constructor.log", level=logging.DEBUG, format=  '%(asctime)s'  ' %(name)s' '  %(levelname)s' ' %(message)s')
try:
    class ineuron:
        def __init__(self, name, email_id, batch_name):
            self.name = name
            self.email_id = email_id
            self.batch_name = batch_name
        def student(self):
            x = int(input("enter number of students : "))
            logging.info(" number of students are %s:", x)
        logging.info(" Total number of students have been entered")
    a = ineuron("Rambabu ", "palla.r7@gmail.com ", "FSDS Bootcamp")
    b = ineuron("Padya ", "palla.r7@gmail.com ", "FSDS Bootcamp")
    a.student()
    print("first student details are :", a.name, a.email_id, a.batch_name)
    logging.info(" first student details are %s %s %s", a.name, a.email_id, a.batch_name)
    print("second student details are :", b.name, b.email_id, b.batch_name)
    logging.info(" second student details are %s %s %s", b.name, b.email_id, b.batch_name)
    logging.info(" student details have been printed successfully")
except Exception as e:
    logging.exception(e)
    logging.error(e)
    logging.critical(" this is the situation for us")


