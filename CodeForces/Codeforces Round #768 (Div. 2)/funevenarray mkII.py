# This is the version that was accepted.

# The only way to ensure the entire array is the same element in the method describe is you have to first ensure that the right most elemment is the same as the one next to it and so on
# Essentially this starts at the right most element and iterates backwards using steps of 1 checking if it is the same element. If it is then the size of the array we can copy over just got bigger without us needing to use an operation.
# If it is not then we copy over all the element to the right of where we are at the array as described in the question. 
# This makes it the most efficient way of doing this, as we ensure before we do an operation we are copying over the maximum amount of elements possible.
# If we reach a differing element and the remaining elements to the left is less than the amount of elements to the right (at all times in this program the elements to the right are all the same element) then we know this is our last operation.
operations=0

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    index=n-1
    while(index>=1):
        if(a[index-1]!=a[index]):     
        # If we find a differing element, we must copy       
            if index<n//2:
                # If the index is on the left half of the array we have at least half of the elements of the entire array to copy over, 
                # so this is our last operation.
                operations+=1
                index=0
            else:
                for j in range(2*index-n,index):
                    a[j]=a[n-1] #copy them over. 
                # To be honest this is unneccesary we could've just kept track of the right most element and compared that to every other element
                # In this case instead of using a for loop we would simply decrease index by the required amount.
                index=2*index-n
                operations+=1
        else:
            index-=1
    print(operations)
    operations=0

        
