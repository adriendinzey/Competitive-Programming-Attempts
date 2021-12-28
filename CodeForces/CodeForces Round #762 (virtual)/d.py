t=int(input())
for i in range(t):
    input()
    m,n=map(int,input().split())
    l=[]
    currMax=0
    tot=0
    max2=0
    for j in range(m):
        l2=list(map(int,input().split()))
        l.extend(l2)
        x=max(l2)
        if currMax<x:
            currMax=x
            max2=currMax
            tot=1
        elif currMax==x:
            tot+=1
    if tot==m:
        print(max2)
    else:
        l.sort(reverse=True)
        loop=m-tot
        while loop>0:
            loop-=tot
        # using the frequency dictionary I could calculate whether or not that MEX value was possible
        # but the next step was thinking of a good way to calculate the minimum number of operations
        # ran out of time
            
