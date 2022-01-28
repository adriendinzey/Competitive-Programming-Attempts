#00
#01
#10
#11

#000
#001 
#010
#011
#100
#101
#110
#111

# As a "base case" for k=0, since [0,n-1] contains every binary number of length log2(n), we can just pair "compliments" where the compliment of a number is just its opposite, that is all 1's become 0 and all 0's become 1. 
# This ensures that every digit of the two numbers is different. We know this compliment exists in the set because the set contains every binary number of the length we are examining.
# We know it is unique (there is exactly 1 compliment for every binary nummber of length log2(n)) because if there were more than one then they would just be equal to the same number.

# If you notice, the & of n-1 (for any n that is a power of 2) and another number less than n-1 is just that number
# This is because n-1 has a 1 in every digit. So if there is any k less than n-1, we can match n-1 with k. 
# But we need to make sure all of the other pairs result in 0. We can simply match the rest of the pairs with their compliments except for k's compliment and n-1's compliment.
# We know that n-1's compliment must be 0 because the only way to get all 0's from an & operation where the first number contains all 1 digits
# is if the second number contains all 0 digits. The thing about 0 is that it can "cancel out" any other number (0 & anything is 0). 
# Therefore, by matching k's compliment with 0 we know the & operation will result in 0 for a total of k when we sum the results of all & operations.

# Finally, our one edge case is when k=n-1. We can't match n-1 with n-1. Instead what we will do is match n-1 with n-2. n-2 is exactly the same as n-1 except n-2 has a 0 in the 1's digit while n-1 has a 1. 
# This results in the & operation yielding n-2 (as we'd expect). So, in this case we just need to get 1 some how. The number 1 is similar to 0 in the sense that it will cancel out all digits except for the 2^0 digit.
# We simply need to match 1 with any number that has a 1 in the 2^0 digit. We will choose 3 arbitrarily, although there are many options. Now we just need to match the rest of the elements so that their & results in 0.
# We know that n-2 and 1 are compliments, but n-1's compliment and 3's compliment are both without compliments. We will match these together since we know 0(n-1's compliment) will give us the results of 0 that we want with any number.
# The only time k=n-1 doesn't work is when log2(n)=2 because there are only 2 numbers with a 1 in its 2^0 digit, which is 1 and n-1 themselves. 1 can not be pared with any remaining arbitrary number with a 1 in its 2^0 digit as there are no such numbers left.

t = int(input())
for i in range(t):
    n,k=map(int,input().split())
    if(n==4 and k==3):
        print(-1)
    elif(k==n-1):
        for i in range(0,n//2):
            if i==0:
                print(0,n-1-3)
            elif i==1:
                print(str(n-1),str(n-2))
            elif i==3:
                print(1,3)
            else:
                print(i,n-i-1) # prints the compliment of the number which is simple (n-1)-i 
                # They are compliments because they sum up to n-1 in decimal
    elif(k>0):        
        for i in range(0,n//2):
            if i==0:
                print(0,n-1-k)
            elif i==n-1-k or i==k:
                print(k,n-1)
            else:
                print(i,n-i-1)
    else:
        for i in range(0,n//2):
            print(i,n-i-1)
