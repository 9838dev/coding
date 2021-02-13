# find the union of sorted array

def find_union(arr1,arr2,n,m):
    i=j=0
    d={}
    while i<n and j<m:
        if arr1[i] == arr2[j]:
            d.setdefault(arr1[i],1)
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            d.setdefault(arr1[i],1)
            i+=1
        else:
            d.setdefault(arr2[j],1)
            j+=1
    while i<n:
        d.setdefault(arr1[i],1)
        i+=1
    while j<n:
        d.setdefault(arr2[j],1)
        j+=1
    return d.keys()

arr1=[1,37,45,67]
arr2=[6,9,13,15,20,25,29,46]
print(find_union(arr1,arr2,len(arr1),len(arr2)))