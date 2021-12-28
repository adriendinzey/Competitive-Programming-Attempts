t=int(input())
for i in range(t):
    line=input()
    ans="NO"
    if(len(line)%2==0):
        half=len(line)//2
        if(line[:half]==line[half:]):
            ans="YES"
    print(ans)