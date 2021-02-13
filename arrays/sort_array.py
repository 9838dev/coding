# sort array which contains 0's,1's,2's

def sort_array(arr):
    count=[0]*3
    for i in arr:
        count[i]+=1

    for i in range(1,3):
        count[i]+=count[i-1]
    temp = arr.copy()
    for i in range(len(arr)):
        arr[count[temp[i]]-1] = temp[i]
        count[temp[i]]-=1 

arr=[2,2,1,1,0,0,0,0,1,2,2,2,0,0,0,0,1]
sort_array(arr)
print(arr)