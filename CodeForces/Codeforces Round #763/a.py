t = int(input())
for i in range(t):
    n,m,rb,cb,rd,cd = map(int,input().split())
    r=1
    c=1
    time=0
    while True:
        # Runs until we find the spot
        # This assumed that there is no case where we can't find the spot
        # I assumed this because the question didn't detail what to output if the case was impossible
        if rb==rd or cb == cb==cd: #if we are on the spot, stop
            print(time)
            break
        if rb+r==0 or rb+r ==n+1: #if we are about to hit a wall, reflect
            r*=-1
        if cb+c==0 or cb+c==m+1: #if we are about to hit a wall, reflect
            c*=-1
        rb+=r
        cb+=c
        time+=1

