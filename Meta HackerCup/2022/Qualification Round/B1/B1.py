with open('./Meta HackerCup/2022/Qualification Round/B1/second_friend_input.txt','r') as f:
    lines = [line.rstrip() for line in f]
    f.close()
t=int(lines.pop(0))
res=""
for i in range(t):
    print(lines[0])
    r,c=map(int,lines.pop(0).split())
    print(r,c)
    painting=[]
    for j in range(r):
        painting.append(lines.pop(0))
    if r==1 or c==1:
        booler=True
        for line in painting:
            for letter in line:
                if letter == '^':
                    booler=False
        if booler:            
            res+="Case #"+str(i+1)+": Possible\n"
            if r==1:
                res+=painting[0]
            else:
                res+="\n".join(painting)
            if i!=t-1:
                res+="\n"
        else:
            res+="Case #"+str(i+1)+": Impossible"
            if i!=t-1:
                res+="\n"

    else:
        painting=[]
        for j in range(r):
            line="^"*c
            painting.append(line)
        res+="Case #"+str(i+1)+": Possible\n"
        res+="\n".join(painting)
        if i!=t-1:
            res+="\n"
print(res)

with open('./Meta HackerCup/2022/Qualification Round/B1/B_output.txt', 'w') as f:
    f.write(res)     
