lower= int(input("enter the lower number"))
higher=int(input("enter the higher number"))

for i in range(lower,higher +1):
    if i>1:
        for x in range (2,i):
         if (i % x)==0:
             
          break
        else:
           print(i)
