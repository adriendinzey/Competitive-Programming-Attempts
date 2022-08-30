t=int(input())
for i in range(t):
    n=int(input())
    s1=input()
    s2=input()
    booler=True
    for i in range(n):
        if s1[i]=="R":
            booler&=s2[i]=="R"
        else:
            booler&=s2[i]!="R"
    if booler:
        print("Yes")
    else:
        print("NO")
