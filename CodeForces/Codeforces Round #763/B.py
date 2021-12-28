# answer was accepted but took a very long time so I finished it long after the contest was over
# I definitely over complicated the question by trying to look at the right bound too much
t = int(input())
for j in range(t):
    arr=[]
    n= int(input())
    for i in range(n):
        l,r = map(int,input().split())
        arr.append([l,r])
    # take in a list of lists (should've used a set of lists as order does not matter)
    for i in range(n):
        p=arr[i] # finds the number chosen in the order that we are given the ranges
        l=-1   
        for j in range(n):        
            if j!=i: # looks at all other ranges
                if ((l==-1 or arr[j][1]>arr[l][1]) and arr[j][1]<p[1] and arr[j][0]==p[0]): 
                    # finds the pair that 1. shares the same left bound and 2. the right bound of the one found is lower than the right bound of the pair we are examining
                    # of those pairs we find the one with the maximum right bound
                    # if there are no other pairs that have both 1 and 2, l=-1
                    l=j      
        if l==-1:
            # Say that there are no pairs that has 1 and 2
            # if we do not remove the left bound, we must have removed an element from p[0]+1-p[1]
            # any element we remove means, call it arr[b]
            # if arr[b]<p[1] then we have a contradiction, as we would've found an l such that arr[l][1]<p[1]
            # the fact that l=-1 means we did not find such a range
            # if arr[b]==p[1] that is also a contradiction because we ensured that arr[l]!=p
            # we also know there can't be duplicate ranges because we must remove a number from the chosen range,
            # turning that range into a different one
            # therefore by contradiction we had to remove p[0]
            print(p[0],p[1],p[0])
        else:         
            # Of all the ranges that start at the same left bound and whose right bound is less than the select range's right bound
            # we have the one with the largest right bound (arr[l]), therefore the number that was chosen was arr[l][1]+1
            # We know number higher than arr[l][1] that is within the range of p was not selected in the game because arr[l][1] is the max
            # Say we do not chose this number. Say some number d is chosen and d is smaller than arr[l][1]+1
            # That would mean there would exist the following two ranges, p[0]-d-1 and d+1-p[1]
            # There is no range that can be selected from those two ranges so that arr[l] can exist
            # It can not exist in the game before the point where p is selected because then p could not exist after that point
            # Since we know that this game is linear and one range is selected at a time there is a contradiction here
            # Therefore, we must've chosen arr[l][1]+1 which would create, as expected, 
            # arr[l] (which can also be expressed as p[0]-arr[l][1]) and arr[l][1]+2-p[1]
            print(p[0],p[1],arr[l][1]+1)
                





    

