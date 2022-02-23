t=int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    p = "YES"
    for x in range(n,-1,-1):
        for y in range(x,n-1):
            if(a[y]>a[y+1]):
                if(a[y]%2!=a[y+1]%2):
                    temp=a[y]
                    a[y]=a[y+1]
                    a[y+1]=temp
                else:
                    p="NO"
                    break
    print(p)