t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    triangles=[]
    for j in range(n):
        triangles.append(list(map(int,input().split())))
        triangles[-1].append(triangles[-1][0]*triangles[-1][1])
    triangles.sort()
    queries=[]
    for j in range(q):
        queries.append(tuple(map(int,input().split())))
    for query in queries:
        tot=0
        for tup in triangles:
            if query[0]<tup[0]<query[2]:
                if query[1]<tup[1]<query[3]:
                    tot+=tup[2]
            elif tup[0]>=query[2]:
                break

        print(tot)
