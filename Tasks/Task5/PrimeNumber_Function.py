def prime(a,b):
    print ("The Prime Numbers in the range 1 to 1000 are: ")
    list = []
    for number in range (a, b + 1):
        if number>1:
            for i in range(2,number):
                if(number % i) == 0:
                    break
            else:
                list.append(number)
    print(list)
prime(1,1000)
