# gap filling algorithm
# merge two sorted array and resultant array is also sorted without any extra space 

# problem link: https://www.geeksforgeeks.org/merge-two-sorted-arrays/

def find_gap(n):
    if n<=1:
        return 0
    return n//2 + n%2 

def merge_sorted_array(arr1,arr2):
    n,m=len(arr1),len(arr2)
    gap = find_gap(n+m)
    j = gap 
    while gap>0:
        i=0
        while j<n:
            if arr1[i]>arr1[j]:
                arr1[i],arr1[j] = arr1[j],arr1[i]
            i+=1
            j+=1
        j=0
        while i<n and j<m:
            if arr1[i]>arr2[j]:
                arr1[i],arr2[j] = arr2[j],arr1[i]
            i+=1
            j+=1
        i=0
        while j<m:
            if arr2[i]>arr2[j]:
                arr2[i],arr2[j] = arr2[j],arr2[i]
            i+=1
            j+=1
        gap = find_gap(gap)
        j=gap 

arr1=[0,2,5,7,13,18]
arr2=[1,3,6,9,10,12,15,34]
merge_sorted_array(arr1,arr2)
print(arr1)
print(arr2)

