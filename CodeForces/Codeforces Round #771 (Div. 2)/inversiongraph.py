t=int(input())
for i in range(t):
    n=int(input())
    p = list(map(int,input().split()))
    maximums=[]
    maximums.append(p[0])    
    for element in p:
        if(element>maximums[-1]):
            maximums.append(element)
        else:
            for i in range(len(maximums)-1):
                if(element<maximums[i]):
                    tempMax=maximums[-1]
                    maximums=maximums[:i]
                    maximums.append(tempMax)
                    break
    print(len(maximums))