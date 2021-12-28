import math as m
t=int(input())
error=10**(-8)
for i in range(t):
    s1=set()
    s2=set()
    n=int(input())
    ans=(m.sqrt(n))
    if ans+error>m.ceil(ans):
        ans=m.ceil(ans)
    else:
        ans=m.floor(ans)
    for i in range(1,ans+1):
        s1.add(i**2)    
    ans2=(n**(1/3))
    if ans2+error>m.ceil(ans2):
        ans2=m.ceil(ans2)
    else:
        ans2=m.floor(ans2)
    for i in range(1,ans2+1):
        s2.add(i**3)
    ans+=ans2
    s3=s1&s2
    ans-=len(s3)
    print(ans)