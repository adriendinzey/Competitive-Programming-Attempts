t=int(input())
for i in range(t):
    n=int(input())
    a_list = input().split()
    map_object = map(int, a_list)
    l = list(map_object)
    x=sum(l)%n
    print(x if x==0 else 1 )
