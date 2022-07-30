class practice1:
    _name = "rambabu"
    __surname = "palla"
    yob = "1985"
    def _fun1(self):
        l = []
        for i in range(1,4):
            l.append(i)
        return l
    def __fun2(self):
        l = []
        for i in range(4,7):
            l.append(i)
        return l
rams = practice1()
print(rams.yob)
print(rams._name)
print(rams._practice1__surname)
print(rams._fun1())

class practice2(practice1):
    _name = "gowthami"
    __surname = "latchireddi"
    yob = "1986"
gow = practice2()
print(gow._name)
print(gow._practice2__surname)
print(gow.yob)
print(rams._name)
print(rams._practice1__surname)
print(rams.yob)
print(rams._fun1())
print(rams._practice1__fun2())


