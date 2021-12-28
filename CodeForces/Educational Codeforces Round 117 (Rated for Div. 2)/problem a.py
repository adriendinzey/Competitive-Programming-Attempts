#c1+c2=x/2+y/2=|x-c1|+|y-c2|
 
#9 possible cases
#if x>c1
    #if y>c2
        #both absolute values evalute to the value of the inside
        #c1+c2=x-c1+y-c2
        #2c1+2c2=x+y
        #c1+c2=x/2+y/2 
        
    #if y<c2
        # we have |x-c1|=x-c1 and |y-c2|=-(y-c2)
        #c1+c2=x-c1-y+c2
        #2c1=x-y
        #c1=x/2-y/2
        # => x/2-y/2+c2=x/2+y/2
        # c2=y this is a contradiction because we said y<c2.
    #if y=c2
        #c1+c2=x-c1
        #c1+y=x-c1
        #2c1=x-y
        #c1=x/2-y/2 only when x>y
        # => c2+x/2-y/2=x/2+y/2
        #c2=y checks out
#if x<c1
    #if y>c2
        #c1+c2=-x+c1+y-c2
        #2c2=-x+y
        #c2=-x/2+y/2
        # => -x/2+y/2+c2=x/2+y/2
        # c1=x this is a contradiction because we said x<c1.
    #if y<c2
        #c1+c2=-x+c1-y+c2
        #0=-x-y
        #this is a contradiction because we know x and y are both positive
    #if y=c2
        #c1+c2=-x+c1
        #c2=-x
        # => c1-x=x/2+y/2
        #c1=3x/2+y/2 = 3x/2+c2/2 = 3x/2-x/2=x
        #this is a contradiction since we said x<c1
#if x=c1
    #if y>c2
        #c1+c2=y-c2
        #x+2c2=y
        #c2=-x/2+y/2 only when y>x
        # => c1-x/2+y/2=x/2+y/2
        #c1=x checks out
    #if y<c2
        #c1+c2=-y+c2
        #c1=-y=x contradiction because we know both x and y are positive
    #if y=c2
        #c1+c2=0
        # since these are both non negative integers, c1=c2=0.
 
# so the only possible cases we have are when [x>c1 and y>c2], [x>c1 and y=c2], [x=c1,y>c2] and [x=c1 and y=c2]
#this means we need only to check for possible c1 values that are less than or equal to the given x and c2 values that are less than or equal to the given y
#in the case where there is a value for c2 that satisfies the given conditions and it is equal to y, then we know c1 will simply equal x/2-y/2
#in the case where there is a value for c1 that satisfies the given conditions and it is equal to x, then we know c2 will simply equal -x/2+y/2
#in the case we are given x=0,y=0 then c1=0,c2=0.
 
#since we only need to return one possible soultion
# When x>y I will give the case where c2=y and c1=x/2-y/2
# When y>x I will give the case where c1=x and c2=-x/2+y/2
 
# Then, there is one final condition that needs to be checked, when one number is odd and one number is even
# In this case it causes -x/2+y/2 or x/2-y/2 to be a decimal number instead of an integer. 
# then we must find a case where (x+y)/2=c1+c2, we know this is only possible when x>c1 and y>c2 so we must check all integers where this is possible. 
 
def findSoln(x,y):
    c1=0
    c2=0
    if(x<y):
        c1=x
        c2=-x/2+y/2
    else:
        c1=x/2-y/2
        c2=y
    
    return c1,c2
 
def findHardSoln(x,y):
    c1=-1
    c2=-1
    for i in range(x):
        for j in range(y):
            if(i+j==(x+y)/2):
                c1=i
                c2=j
    return c1,c2
 
def processNums(x,y):
    c1,c2=findSoln(x,y)
    if((c1!=int(c1)) or (c2!=int(c2))):
        c1,c2=findHardSoln(x,y)
    return int(c1),int(c2)
 
numCases=int(input())
for i in range(numCases):
    line=input()
    nums=line.split()
    x=int(nums[0])
    y=int(nums[1])
    c1,c2=processNums(x,y)
    print(c1,c2)