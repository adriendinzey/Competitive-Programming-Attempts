n=int(input())
for _ in range(n):
    line=input()
    keys={'r':False,'g':False,'b':False}
    ret=True
    for letter in line:
        if letter.islower():
            keys[letter]=True
        else:
            if not keys[letter.lower()]:
                ret=False
    s= "YES" if ret else "NO"
    print(s)
