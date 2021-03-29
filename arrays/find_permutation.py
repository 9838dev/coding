# given an array find all permutaion 
ans=[]
def heap_permutaion(arr,size):
    if size == 1:
        ans.append(list(arr))
        return
    for i in range(size):
        heap_permutaion(arr,size-1)
        if size%2 == 0:
            arr[0],arr[size-1] = arr[size-1],arr[0]
        else:
            arr[i],arr[size-1] = arr[size-1],arr[i]


arr = [1,2,3]
heap_permutaion(arr,abs(len(arr)))
print(ans)