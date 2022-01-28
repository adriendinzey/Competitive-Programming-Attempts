# O(N^2) solution of finding the largest ranges and "coloring" each one inside. Ran out of time to finish this one
n = int(input())
a=list(map(int,input().split()))
colors=[0]*n
total=0
for i in range(n):
    if colors[i]==0:
        element=a[i]
        j=n-1    
        while(a[i]!=a[j] and colors[j]==0):
            j-=1
        if i!=j:
            for k in range(i+1,j):
                if colors[k]==0:
                    colors[k]=1
                    total+=1
print(total)
