n=int(input())
m=int(input())
for n in range(n,m):
    if(n>1):
        for i in range(2,n):
            if(n%i) == 0:
                break
        else:
            print(n)
    
        
      
