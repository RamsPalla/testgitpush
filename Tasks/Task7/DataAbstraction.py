""" The below code shows the use of abstraction"""
import logging
logging.basicConfig( filename = "DataAbstraction.log", level=logging.DEBUG, format = '%(asctime)s' ' %(name)s' ' %(levelname)s' '%(message)s' )
try:
    from abc import ABC, abstractmethod


    class Polygon(ABC):

        @abstractmethod
        def noofsides(self):
            pass


    class Triangle(Polygon):

        # overriding abstract method
        def noofsides(self):
            print("I have 3 sides")


    class Pentagon(Polygon):

        # overriding abstract method
        def noofsides(self):
            print("I have 5 sides")


    class Hexagon(Polygon):

        # overriding abstract method
        def noofsides(self):
            print("I have 6 sides")


    class Quadrilateral(Polygon):

        # overriding abstract method
        def noofsides(self):
            print("I have 4 sides")


    # Driver code
    R = Triangle()
    R.noofsides()

    K = Quadrilateral()
    K.noofsides()

    R = Pentagon()
    R.noofsides()

    K = Hexagon()
    K.noofsides()

except Exception as e:
    logging.exception(e)

#https://www.scaler.com/topics/python/data-abstraction-in-python/
#https://www.geeksforgeeks.org/abstract-classes-in-python/


# Python program invoking a method using super()

#from abc import ABC, abstractmethod

#class R(ABC):
    #def rk(self):
        #print("Abstract Base Class")


#class K(R):
    #def rk(self):
        #super().rk()
        #print("subclass ")


# Driver code
#r = K()
#r.rk()