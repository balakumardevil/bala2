n=int(input())
m=int(input())
for n in range(n,m):
    t=n
    c=0 
    while(n!=0):
        rem=n%10
        a=rem**3
        n=n//10
        c=a+c
    if(c==t):
        print(c,end=' ')
        
        
