x=0
while x<8:
    content = ""
    y=0
    while y<x:
        z=0
        sum=0
        while z<y:
            sum+=6-z
            z+=1
        if (x + 64 + sum) <= (64 + 26):
            content += " " + chr(x + 64 + sum)
        y+=1
    print(content)
    x+=1

#Below is the another way of writing code for the same problem statement
i=0
while i<7:
    l=7
    k=i+65
    for j in range(i+1):
        if chr(k).isalpha():
         print(chr(k),end=" ")
         l-=1
         k+=l
    i += 1
    print()