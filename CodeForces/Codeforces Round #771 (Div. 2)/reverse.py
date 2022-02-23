t=int(input())
for i in range(t):
    n=int(input())
    perm=list(map(int,input().split()))
    for x in range(1,len(perm)+1):
        if perm[x-1]!=x:
            r=perm.index(x)+1
            reversedChunk=perm[x-1:r]
            reversedChunk.reverse()
            perm=perm[:x-1]+reversedChunk+perm[r:]
            break
    print(*perm)