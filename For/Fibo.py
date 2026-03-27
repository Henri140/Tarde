n=0
for i in range(0,100,n+1):
    if i==0:
        print(i)
        i+=1
        n=i
    elif i==1:
     print(i)
     print(i)
     i+=1
     n = i
    else:       
        print(n)
        n+=i-1
        if n>=8:
           print(n)
           n+=i+1
           
                      