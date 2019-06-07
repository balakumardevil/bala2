n=int(input())
m=int(input())
if(n>1):
    for i in range(n,m):
       if(n%i)==0:
            break
    else:
            print(n)
