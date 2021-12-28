import math
t=int(input())
for i in range(t):
    a,s=map(int,input().split())
    sDigs=int(math.log10(s))+1
    b=''
    for i in range(1,sDigs+1):
            if(s%10>=a%10):
                b=str(s%10-a%10)+b
            elif s%100-a%10<=9 and s%100-a%10>=0:                
                b=str(s%100-a%10)+b
                s=int(s/10) #s//=10
                i+=1
            else:
                b=-1
                break
            s=int(s/10)#s//=10
            a=int(a/10)#a//=10
            #at least the thinking was there!
            print(s,a)
    print(int(b))