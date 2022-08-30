with open('./Meta HackerCup/2022/Qualification Round/A/second_hands_input.txt','r') as f:
    lines = [list(map(int,line.rstrip().split())) for line in f]
    f.close()
t=lines[0][0]
res=""
for i in range(t):
    n,k=lines[i*2+1][0],lines[i*2+1][1]
    s = lines[(i+1)*2]
    works=n<=k*2
    freq={}
    if works:
        for num in s:
            freq[num]=freq.get(num,0)+1
            if freq[num]>2:
                works=False
                break
    ans= "YES" if works else "NO"
    if i!=t-1:
        ans+="\n"
    result = "Case #"+str(i+1)+": "+ans
    print(result)
    res+=result
with open('./Meta HackerCup/2022/Qualification Round/A/A_output.txt', 'w') as f:
    f.write(res)     
