n,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(q):
    t,x,y=map(int,input().split())
    if(t==1):
        l[x-1],l[y-1]=l[y-1],l[x-1]
    else:   
        x=l[x-1]
        y=y%n
        if y==0:
            y=n
        for j in range(y-1):
            x=l[x-1]
            if(l[x-1]==x):
                break
        print(x)
