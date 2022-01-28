# To minimize this, for each a_i and b_i we want the max to be in one array. We know that the max of both arrays will appear as one of the factors in the product no matter what because it must end up in one of the two arrays. 
# So we are essentially trying to multiple that max by the smallest number possible. If we put all the next largest elements into the array with it, the max of the other array will be as small as possible.

t = int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    d=[]
    for i in range(n):
        twople=[a[i],b[i]]
        c.append(max(twople)) 
        d.append(min(twople))
        # We put the larger one into c and smaller one into d.
    print(max(c)*max(d)) # Multiply their max.