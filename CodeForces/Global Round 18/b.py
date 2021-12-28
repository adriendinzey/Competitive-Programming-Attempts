t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    arr=list(range(l,r+1))
    arr2=list()
    maxL=len(bin(r)[2:])
    for i in arr:
        arr2.append(format(i,"0"+str(maxL)+"b"))
    maxSum=0
    index=0
    for j in range(maxL):
        sum=0
        for i in range(len(arr2)):
            if(arr2[i][j]=='1'):
                sum+=1
        if sum>maxSum:
            maxSum=sum
            index=j
    # getting time exceeded, I think Ineed to figure out how to tell which bit has the most 
    # amount of binary strings where that bit is a 1 than any other position 
    # (aka the most popular position)
    print(len(arr)-maxSum)
