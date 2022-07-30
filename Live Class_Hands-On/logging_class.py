#import logging
#logging.basicConfig(filename="../test.log", level = logging.DEBUG)
#logging.info("this is my first code for logging")
#l = [1,2,3,4,5,6,7]
#for i in l:
    #if i == 2:
        #logging.info(i)

#If we missed to mention level in 'logging.basicConfig' then we would not be able to see output in the log file



#import logging
#logging.basicConfig(filename="../test.log", level = logging.DEBUG)
#logging.info("this is my first code for logging")
#l = [1,2,3,4,5,6,7]
#for i in l:
    #logging.info(l)



#Logging level Ranking/Numbering/severity level and Hierarchy:
#Debug - 10
#Info -  20
#Warning-30
#Error - 40
#Critical-50



#import logging
#logging.basicConfig(filename="test.log", level = logging.DEBUG)
#logging.info("this is my first code for logging")
#logging.warning("this will try to load warning messages if any")
#logging.error("this is a error message from system")
#l = [1,2,3,4,5,6,7]
#for i in l:
    #if i ==2:
        #logging.info(l)
        #logging.warning("this is a warning message to user that they have found 2 in list l")
#logging.shutdown()

#logging.shutdown() will shutdown the logging, means nothing would be printed when system encounters this piece of code



#'format' eliminates regular/typical formats such as 'INFO', 'WARNING' etc..



#import logging
#logging.basicConfig(filename = "test1.log", level = logging.DEBUG, format= '%(asctime)s %(name)s %(levelname)s %(message)s')
#logging.info("this is message with timestamp")



#import logging
#def devide (a,b):
    #return a/b
#print((devide(3,4)))



#import logging
#logging.basicConfig(filename = "exception.log", level = logging.INFO, format = '%(asctime)s %(name)s %(levelname)s %(message)s')
#def devide (a,b):
    #logging.info("the number entered by user is %s and %s", a, b)
    #try:
        #logging.info("we are into function")
        #div = a/b
        #logging.info("we have completed a division operation")
        #logging.info("the result of the division is %s", div)
        #return div
    #except Exception as e:
        #logging.exception(e)
#(devide(3,1))


#import logging
#logging.basicConfig(filename = "exception.log", level = logging.CRITICAL, format = '%(asctime)s %(name)s %(levelname)s %(message)s')
#def devide (a,b):
    #logging.info("the number entered by user is %s and %s", a, b)
    #try:
        #logging.info("we are into function")
        #div = a/b
        #logging.info("we have completed a division operation")
        #logging.info("the result of the division is %s", div)
        #return div
    #except Exception as e:
        #logging.exception(e)
        #print(e)
#(devide(3,0))



#import logging
#logging.basicConfig(filename = "read.log", level = logging.DEBUG, format = '%(asctime)s %(name)s %(levelname)s %(message)s')
#try:
    #logging.info("I am trying to read a file")
    #with open("rambabu1.txt", 'r'):
        #logging.info("It has read the file successfully")
#except Exception as e:
        #logging.critical("this is a situation for us")
        #logging.error(e)
        #logging.exception(e)
