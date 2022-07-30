""" Below code is written to implement inheritance concept to print student details"""
import logging
logging.basicConfig(filename="inheritance.log", level=logging.DEBUG, format=  '%(asctime)s'  ' %(name)s' '  %(levelname)s' ' %(message)s')
try:
    class name:
        firstname = "Rambabu"
        lastname = "Palla"
        yob = 1985
    class emailid:
        email_id = "palla.r7@gmail.com"
    class years(name, emailid):
        def age(self, current_year):
            return current_year - name.yob
    a = years()
    logging.info("  details of student are %s %s %s %s %s", a.firstname, a.lastname, a.email_id, a.yob, a.age(2022))
except Exception as e:
    logging.exception(e)

