#Fobonacci series using 'return'
def genfib(n):
    a = 1
    b = 1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b, a+b
    return l
print(genfib(10))

#Fibonacci series using 'yield/generator'
#def genfib1(n):
    #a = 1
    #b = 1
    #l = []
    #for i in range(n):
        #yield(a)
        #a,b = b, a+b
#for i in genfib1(10):
    #print(i)
