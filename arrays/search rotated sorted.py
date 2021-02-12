# search in rotated sorted array 
# technique binary search

# returning index position where element is found otherwise -1
def search_rotated(arr,key):
    n = len(arr)
    l,r=0,n-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == key:
            return mid 
        elif arr[l]<=arr[mid]:
            if arr[mid]>key and arr[l]<=key:
                r=mid-1
                continue 
            l = mid+1 
        elif arr[l]>arr[mid]:
            if arr[mid]<=key and arr[r]>=key:
                l=mid+1
                continue 
            r=mid-1 
    return -1 

arr = [5,6,7,1,2,3]
print(search_rotated(arr,6))

