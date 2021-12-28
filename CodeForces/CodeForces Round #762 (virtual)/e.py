def countFreq(arr, n):
 
    mp = dict()
 
    # Traverse through array elements
    # and count frequencies
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for i in range(n):
        if i not in mp.keys():
            mp[i]=0
              
    return mp
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=l.sort()
    d=countFreq(l,n)
    nums=d[0]
    atLeast1=nums>0
    ans=''
    for j in range(n):
        if(atLeast1):
            num=0
            for k in range(j):
    # realized with this method I'd need to have another "max2" or "next maximum" 
    # up to n times in a worst case


