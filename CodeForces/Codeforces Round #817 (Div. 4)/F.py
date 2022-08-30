t=int(input())
for case in range(t):
    n,m=map(int,input().split())
    grid=[]
    visited=[[False for i in range(m)]for j in range(n)]
    for i in range(n):
        grid.append(input())
    t=True
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="*" and not visited[i][j]:
                visited[i][j]=True
                neighbors=[]
                for x,y in (-1,0), (1,0),(0,1),(0,-1):
                    if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y]=="*":
                        if len(neighbors)==1:
                            if neighbors[0][0]==x or neighbors[0][1]==y:
                                t=False
                                break
                        elif len(neighbors)>2:
                            t=False
                            break
                        if visited[x+i][y+j]:
                            t=False
                            break
                        visited[x+i][y+j]=True                        
                        neighbors.append((x,y))
                if len(neighbors)==2:
                    for x,y in (-1,-1), (1,1),(1,-1),(-1,1):
                        if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y]=="*":
                            t=False
                            break
                elif len(neighbors)==1:
                    for x,y in (-1,-1), (1,1),(1,-1),(-1,1):
                        if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y]=="*":
                            if (neighbors[0][0]!=0 and x==neighbors[0][0]) or (neighbors[0][1]!=0 and y==neighbors[0][1]):                                
                                if visited[x+i][y+j]:
                                    t=False
                                    break
                                neighbors.append((x,y))
                                visited[x+i][y+j]=True   
                            else:
                                t=False
                                break
                            if len(neighbors)>2:
                                t=False
                                break        
                    if len(neighbors)!=2:
                        t=False
                        break        
                else:
                    t=False
                    break
            if not t:
                break
        if not t:
            break
    s="YES" if t else "NO"
    print(s)
                        