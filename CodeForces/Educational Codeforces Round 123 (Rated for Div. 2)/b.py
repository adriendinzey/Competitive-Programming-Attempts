import itertools
t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for j in range(n,0,-1):
        a.append(j)
    print(*a)
    for j in range(n-1,0,-1):
        temp=a[j]
        a[j]=a[j-1]
        a[j-1]=temp
        print(*a)
    
    