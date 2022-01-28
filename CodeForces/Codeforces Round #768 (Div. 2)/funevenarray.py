operations=0

def sameElement(arr):
    global operations
    length=len(arr)
    if(length!=2):
        arr=arr[:length//2]+sameElement(arr[length//2:])
    if(arr[length//2]!=arr[length//2-1]):
        operations+=1
        for i in range(length//2):
            arr[i]=arr[i+length//2]
    return arr

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if(n==1):
        print(0)
    else:
        sameElement(a)
        print(operations)
        operations=0

        
