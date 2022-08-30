import sys
sys.setrecursionlimit(1500000000)
with open('./Meta HackerCup/2022/Qualification Round/B2/second_second_friend_input.txt','r') as f:
    lines = [line.rstrip() for line in f]
    f.close()
t=int(lines.pop(0))
res=""
for i in range(t):
    r,c=map(int,lines.pop(0).split())
    painting=[]
    for j in range(r):
        painting.append(list(lines.pop(0)))  
    if i>=68:
        print(i,painting)
    if r==1 or c==1:
        booler=True
        for line in painting:
            for letter in line:
                if letter == '^':
                    booler=False
        if booler:            
            res+="Case #"+str(i+1)+": Possible\n"
            if r==1:
                res+="".join(painting[0])
                if i!=t-1 or x<len(painting)-1:
                    res+="\n"
            else:
                for x,line in enumerate(painting):
                    res+=line[0]
                    if i!=t-1 or x<len(painting)-1:
                        res+="\n"
        else:
            res+="Case #"+str(i+1)+": Impossible"
            if i!=t-1:
                res+="\n"

    else:
        painting2=[]
        visited=[[False for x in range(c)]for y in range(r)]
        stack=[]
        booler=True
        for x,line in enumerate(painting):
            for y,cell in enumerate(line):
                if cell=="^":
                    stack.append((x,y))
        def recurse(x,y,prevX,prevY):      
            if visited[x][y]:
                if painting[x][y]=="^":
                    neighbs=0
                    for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
                        if 0<=x+dx<r and 0<=y+dy<c and neighbs<2:
                            neighbs+=1 if painting[x+dx][y+dy]=="^" else 0
                    return neighbs>=2
                else:
                    return False 
            visited[x][y]=True  
            if painting[x][y]=="#":
                return False                
            painting[x][y]="^" 
            neighbors=0   
            for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
                if 0<=x+dx<r and 0<=y+dy<c and neighbors<2:
                    if dx!=prevX or dy!=prevY:
                        if visited[x+dx][y+dy]:
                            if painting[x][y]!="#":
                                neighbors+=1
                        else:
                            b=recurse(x+dx,y+dy,-dx,-dy)
                            neighbors= neighbors+1 if b else neighbors
                    else:
                        neighbors+=1
            if neighbors==2:
                return True
            else:
                return False
        for coord in stack:
                booler&=recurse(*coord,0,0)
        if booler:
            res+="Case #"+str(i+1)+": Possible\n"
            for x,line in enumerate(painting):
                res+="".join(line)
                if i!=t-1 or x<len(painting)-1:
                    res+="\n"
        else:
            res+="Case #"+str(i+1)+": Impossible"
        if i!=t-1:
            res+="\n"

with open('./Meta HackerCup/2022/Qualification Round/B2/B2_output.txt', 'w') as f:
    f.write(res)     
