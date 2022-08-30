name={"T":1,"i":1,"m":1,"u":1,"r":1}
t = int(input())
for i in range(t):
    n=int(input())
    s=input()
    n2={}
    if n==5:
        for i in range(len(name)):
            n2[s[i]]=1
        if name.keys()==n2.keys():
            print("YES")
        else:
            print("NO")
    else:
        print("NO")