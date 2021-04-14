# array contaings 0 to N-1 integer and array is distinct
# find longest length of set S, where
# s[i] = {arr[i],arr[arr[i]],arr[arr[arr[i]]],...}

def find_longest(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i] != float('inf'):
            count=0
            start = arr[i]
            while arr[start]!=float('inf'):
                count+=1
                temp = start
                start = arr[start]
                arr[temp] = float('inf')
            total = max(total,count)
    return total 

arr=[3,5,4,1,0,2]
print(find_longest(arr))