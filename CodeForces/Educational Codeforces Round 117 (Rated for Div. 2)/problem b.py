
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    l=[]
    l.append(a)
    for i in range(n):
        if(n-i != a and n-i != b):
            l.append(n-i)
    l.append(b)
    if(a==min(l[:n//2]) and b==max(l[n//2:])):
        print(*l)
    else:
        print(-1)
# was on the right track with this answer but I ended up needing to look at someone else's
# solution after the contest was over to completely figure it out