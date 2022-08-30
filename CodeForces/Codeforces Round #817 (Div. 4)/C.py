t=int(input())
for i in range(t):
    n=int(input())
    w1=input().split()
    w2=input().split()
    w3=input().split()
    d={}
    points=[0,0,0]
    for word in w1:
        d[word]=d.get(word,[])+[0]
    for word in w2:
        d[word]=d.get(word,[])+[1]
    for word in w3:
        d[word]=d.get(word,[])+[2]

    for authors in d.values():
        if len(authors)==2:
            for index in authors:
                points[index]+=1
        elif len(authors)==1:
            points[authors[0]]+=3
    print(*points)
