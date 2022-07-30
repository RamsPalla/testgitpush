#Universal code:
#m = int(input("enter number"))
#c = ((m+1)/2)
#d = int(((7*c)+c))
#for i in range(m+1):
    #if i <= c:
        #n = i
    #else:
        #n = m-i+1
    #print(("ineuron "*n).center(d,' '))

#Second way:
#for i in range(6):
    #if i <= 3:
        #n = i
    #else:
        #n = 6 - i
    #print(("ineuron "*n).center(30,' '))

#Another way(complex code, not preferable as we can write code in simpler way than this):
#m = int(input("enter number of rows you want to print"))
#n = int(((m+1)/2))
#for i in range(n) :
    #for j in range(i, n-1) :
        #print(" " * len("ineuron"), end="")
    #for j in range(i+1) :
        #print("       ineuron", end="")
    #for j in range(i) :
        #print("", end=" ")
    #print("\n")
#m = n-1
#for k in range(m) :
    #for l in range(k+1) :
        #print(" " * len("ineuron"), end="")
    #for l in range(l, m) :
        #print("       ineuron", end="")
    #print("\n")