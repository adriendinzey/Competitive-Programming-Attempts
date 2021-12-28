t=int(input())
for i in range(t):
    n=int(input())
    a=input()
    b=input()
    num1=0
    num1sums=0
    num2sums=0
    for i in range(n):
        if a[i]!=b[i]:
            num1+=1
            if(a[i]=='1'):
                num1sums+=1
        elif a[i]=='1':
            num2sums+=1
    num2=n-num1
    ret=-1
    if num1%2==0 and num1sums==num1//2:
        ret=num1
    if num2%2==1 and (num2<num1 or num1%2==1 or num1sums!=num1//2) and int(num2/2+0.5)==num2sums:
        ret=num2
    print(ret)