t=int(input())
for i in range(t):
    numChanges=int(input())
    s=input()
    n=len(s)
    l,r=0,n-1
    sum=0
    changes=[]
    while(l<r):
        if s[l]=="L":
            sum+=l
            changes.append(n-1-l-l)
        else:
            sum+=n-1-l
        l+=1
        if s[r]=="R":
            sum+=n-1-r
            changes.append(r-n+1+r)
        else:
            sum+=r
        r-=1
    if(l==r):
        sum+=l

    for i in range(n):
        if i<len(changes):
            changes[i]+=sum
            sum=changes[i]
        else:
            changes.append(sum)
    print(*changes)