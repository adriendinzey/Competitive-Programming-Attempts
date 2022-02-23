def kwindow(L, k):
    for i in range(len(L)-k+1):
        yield L[i:i+k]
t = int(input())
for i in range(t):
    n,x=map(int,input().split())
    L=list(map(int,input().split()))
    sums=[]
    sums.append(L)
    
    for j in range(2,n+1):
        arr=[]
        for k in range(n-j+1):
            arr.append(sums[-1][k]+L[k+j-1])
        sums.append(arr)
    maxSums=[]
    for j in range(len(sums)):
        maxSums.append(max(sums[j]))
    sums=[]
    sums.append(max(maxSums))
    if sums[0]<0:
        sums[0]=0
    newSum=0
    for k in range(1,n+1):
        for j in range(k,n+1):
            maxSums[j-1]+=x
            if maxSums[j-1]>newSum:
                newSum=maxSums[j-1]        
        sums.append(newSum)
    print(*sums)
