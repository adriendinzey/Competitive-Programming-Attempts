n,q=map(int,input().split())
colors=[1]*n
a=[0]*n
for i in range(q):
    commands=input().split()
    if(commands[0]=="Color"):
        l,r,c=int(commands[1]),int(commands[2]),int(commands[3])
        chunk=[c]*(r-l+1)
        colors=colors[:l-1]+chunk+colors[r:]
    elif(commands[0]=="Add"):
        c,x=int(commands[1]),int(commands[2])
        for j in range(n):
            if(colors[j]==c):
                a[j]+=x
    else:
        print(a[int(commands[1])-1])
