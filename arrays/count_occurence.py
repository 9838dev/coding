# find the number occurence of a element in an sorted array

# find the first occurence of element
def first_occ(arr,item):
    l,r=0,len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == item and (mid == 0 or arr[mid-1]!=item):
            return mid 
        elif arr[mid]>=item:
            r=mid-1
        else:
            l=mid+1

# last occurence of an element
def last_occ(arr,item):
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid] == item and (mid == len(arr)-1 or arr[mid+1]!=item):
            return mid 
        elif arr[mid]>item:
            r=mid-1
        else:
            l=mid+1 
    
arr=[1,1,3,3,4,5,6,7,7,7,8,9]
item = 1
print(last_occ(arr,item)-first_occ(arr,item)+1)